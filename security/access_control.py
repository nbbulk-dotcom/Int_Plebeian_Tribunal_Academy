"""
International Plebeian Academy - Access Control Module
Role-based access control (RBAC) and permission management

Features:
- Role-based access control
- Permission management
- Resource-level access control
- Hierarchical roles
- Dynamic permission evaluation

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

import logging
from typing import Dict, List, Set, Optional, Any
from datetime import datetime
from enum import Enum

logger = logging.getLogger(__name__)


class Permission(Enum):
    """System permissions"""
    USER_CREATE = "user:create"
    USER_READ = "user:read"
    USER_UPDATE = "user:update"
    USER_DELETE = "user:delete"
    
    SYSTEM_CONFIG_READ = "system:config:read"
    SYSTEM_CONFIG_WRITE = "system:config:write"
    SYSTEM_MANAGE = "system:manage"
    
    BOT_CREATE = "bot:create"
    BOT_READ = "bot:read"
    BOT_UPDATE = "bot:update"
    BOT_DELETE = "bot:delete"
    BOT_ASSIGN_TASK = "bot:assign_task"
    
    BLOCKCHAIN_READ = "blockchain:read"
    BLOCKCHAIN_WRITE = "blockchain:write"
    BLOCKCHAIN_ADMIN = "blockchain:admin"
    
    FILE_VERIFY = "file:verify"
    FILE_REGISTER = "file:register"
    
    DISTRIBUTION_READ = "distribution:read"
    DISTRIBUTION_WRITE = "distribution:write"
    DISTRIBUTION_MANAGE = "distribution:manage"
    
    GOVERNANCE_PROPOSE = "governance:propose"
    GOVERNANCE_VOTE = "governance:vote"
    GOVERNANCE_EXECUTE = "governance:execute"


class Role:
    """Role definition"""
    
    def __init__(
        self,
        role_id: str,
        role_name: str,
        permissions: Set[Permission],
        description: Optional[str] = None,
        parent_role: Optional['Role'] = None
    ):
        self.role_id = role_id
        self.role_name = role_name
        self.permissions = permissions
        self.description = description
        self.parent_role = parent_role
        self.created_at = datetime.utcnow()
    
    def has_permission(self, permission: Permission) -> bool:
        """Check if role has specific permission"""
        if permission in self.permissions:
            return True
        
        if self.parent_role:
            return self.parent_role.has_permission(permission)
        
        return False
    
    def get_all_permissions(self) -> Set[Permission]:
        """Get all permissions including inherited"""
        all_permissions = self.permissions.copy()
        
        if self.parent_role:
            all_permissions.update(self.parent_role.get_all_permissions())
        
        return all_permissions


class AccessControl:
    """Access control system"""
    
    def __init__(self):
        """Initialize access control system"""
        self.roles: Dict[str, Role] = {}
        self.user_roles: Dict[str, Set[str]] = {}
        self.resource_permissions: Dict[str, Dict[str, Set[Permission]]] = {}
        
        self._initialize_default_roles()
        
        logger.info("Access control system initialized")
    
    def _initialize_default_roles(self) -> None:
        """Initialize default system roles"""
        guest_role = Role(
            role_id='guest',
            role_name='Guest',
            permissions={
                Permission.USER_READ,
                Permission.BLOCKCHAIN_READ,
                Permission.FILE_VERIFY
            },
            description='Guest user with read-only access'
        )
        
        member_role = Role(
            role_id='member',
            role_name='Member',
            permissions={
                Permission.USER_UPDATE,
                Permission.BOT_READ,
                Permission.FILE_REGISTER,
                Permission.GOVERNANCE_VOTE,
                Permission.DISTRIBUTION_READ
            },
            description='Regular member',
            parent_role=guest_role
        )
        
        division_leader_role = Role(
            role_id='division_leader',
            role_name='Division Leader',
            permissions={
                Permission.BOT_ASSIGN_TASK,
                Permission.BOT_UPDATE,
                Permission.GOVERNANCE_PROPOSE
            },
            description='Division leadership',
            parent_role=member_role
        )
        
        admin_role = Role(
            role_id='admin',
            role_name='Administrator',
            permissions={
                Permission.USER_CREATE,
                Permission.USER_DELETE,
                Permission.SYSTEM_CONFIG_WRITE,
                Permission.SYSTEM_MANAGE,
                Permission.BOT_CREATE,
                Permission.BOT_DELETE,
                Permission.BLOCKCHAIN_ADMIN,
                Permission.DISTRIBUTION_MANAGE,
                Permission.GOVERNANCE_EXECUTE
            },
            description='System administrator',
            parent_role=division_leader_role
        )
        
        self.roles['guest'] = guest_role
        self.roles['member'] = member_role
        self.roles['division_leader'] = division_leader_role
        self.roles['admin'] = admin_role
        
        logger.info("Default roles initialized")
    
    def assign_role(self, user_id: str, role_id: str) -> bool:
        """
        Assign role to user
        
        Args:
            user_id: User identifier
            role_id: Role identifier
            
        Returns:
            True if successful, False otherwise
        """
        if role_id not in self.roles:
            logger.warning(f"Role {role_id} not found")
            return False
        
        if user_id not in self.user_roles:
            self.user_roles[user_id] = set()
        
        self.user_roles[user_id].add(role_id)
        logger.info(f"Role {role_id} assigned to user {user_id}")
        
        return True
    
    def revoke_role(self, user_id: str, role_id: str) -> bool:
        """
        Revoke role from user
        
        Args:
            user_id: User identifier
            role_id: Role identifier
            
        Returns:
            True if successful, False otherwise
        """
        if user_id not in self.user_roles:
            return False
        
        if role_id in self.user_roles[user_id]:
            self.user_roles[user_id].remove(role_id)
            logger.info(f"Role {role_id} revoked from user {user_id}")
            return True
        
        return False
    
    def check_permission(
        self,
        user_id: str,
        permission: Permission
    ) -> bool:
        """
        Check if user has specific permission
        
        Args:
            user_id: User identifier
            permission: Permission to check
            
        Returns:
            True if user has permission, False otherwise
        """
        if user_id not in self.user_roles:
            return False
        
        for role_id in self.user_roles[user_id]:
            if role_id in self.roles:
                role = self.roles[role_id]
                if role.has_permission(permission):
                    return True
        
        return False
    
    def check_resource_access(
        self,
        user_id: str,
        resource_type: str,
        resource_id: str,
        permission: Permission
    ) -> bool:
        """
        Check if user has permission for specific resource
        
        Args:
            user_id: User identifier
            resource_type: Type of resource (e.g., 'bot', 'file')
            resource_id: Resource identifier
            permission: Required permission
            
        Returns:
            True if user has access, False otherwise
        """
        if not self.check_permission(user_id, permission):
            return False
        
        resource_key = f"{resource_type}:{resource_id}"
        
        if resource_key in self.resource_permissions:
            if user_id in self.resource_permissions[resource_key]:
                return permission in self.resource_permissions[resource_key][user_id]
        
        return True
    
    def grant_resource_permission(
        self,
        user_id: str,
        resource_type: str,
        resource_id: str,
        permission: Permission
    ) -> None:
        """
        Grant resource-specific permission to user
        
        Args:
            user_id: User identifier
            resource_type: Type of resource
            resource_id: Resource identifier
            permission: Permission to grant
        """
        resource_key = f"{resource_type}:{resource_id}"
        
        if resource_key not in self.resource_permissions:
            self.resource_permissions[resource_key] = {}
        
        if user_id not in self.resource_permissions[resource_key]:
            self.resource_permissions[resource_key][user_id] = set()
        
        self.resource_permissions[resource_key][user_id].add(permission)
        
        logger.info(
            f"Granted {permission.value} on {resource_key} to user {user_id}"
        )
    
    def get_user_permissions(self, user_id: str) -> Set[Permission]:
        """
        Get all permissions for user
        
        Args:
            user_id: User identifier
            
        Returns:
            Set of all user permissions
        """
        all_permissions = set()
        
        if user_id in self.user_roles:
            for role_id in self.user_roles[user_id]:
                if role_id in self.roles:
                    role = self.roles[role_id]
                    all_permissions.update(role.get_all_permissions())
        
        return all_permissions
    
    def get_user_roles(self, user_id: str) -> List[Dict[str, Any]]:
        """
        Get all roles assigned to user
        
        Args:
            user_id: User identifier
            
        Returns:
            List of role information
        """
        if user_id not in self.user_roles:
            return []
        
        user_role_info = []
        
        for role_id in self.user_roles[user_id]:
            if role_id in self.roles:
                role = self.roles[role_id]
                user_role_info.append({
                    'role_id': role.role_id,
                    'role_name': role.role_name,
                    'description': role.description,
                    'permissions': [p.value for p in role.get_all_permissions()]
                })
        
        return user_role_info
    
    def create_custom_role(
        self,
        role_id: str,
        role_name: str,
        permissions: List[Permission],
        description: Optional[str] = None,
        parent_role_id: Optional[str] = None
    ) -> bool:
        """
        Create custom role
        
        Args:
            role_id: Role identifier
            role_name: Role name
            permissions: List of permissions
            description: Role description
            parent_role_id: Parent role identifier
            
        Returns:
            True if successful, False otherwise
        """
        if role_id in self.roles:
            logger.warning(f"Role {role_id} already exists")
            return False
        
        parent_role = None
        if parent_role_id and parent_role_id in self.roles:
            parent_role = self.roles[parent_role_id]
        
        new_role = Role(
            role_id=role_id,
            role_name=role_name,
            permissions=set(permissions),
            description=description,
            parent_role=parent_role
        )
        
        self.roles[role_id] = new_role
        logger.info(f"Custom role created: {role_id}")
        
        return True


__all__ = ['AccessControl', 'Permission', 'Role']
