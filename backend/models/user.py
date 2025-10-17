"""
International Plebeian Academy - User Models
Database models for user management and authentication

Models:
- User: Core user account information
- BiometricTemplate: Stored biometric authentication templates
- UserSession: Active user session tracking
- UserRole: User roles and permissions

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

from datetime import datetime
from typing import List, Optional
from werkzeug.security import generate_password_hash, check_password_hash
import json

from . import database


class User(database.Model):
    """
    User account model
    
    Stores core user information including credentials,
    profile data, and authentication settings.
    """
    
    __tablename__ = 'users'
    
    user_id = database.Column(
        database.String(36),
        primary_key=True,
        nullable=False,
        unique=True
    )
    
    username = database.Column(
        database.String(100),
        nullable=False,
        unique=True,
        index=True
    )
    email = database.Column(
        database.String(255),
        nullable=False,
        unique=True,
        index=True
    )
    password_hash = database.Column(
        database.String(255),
        nullable=True  # Nullable for biometric-only users
    )
    
    first_name = database.Column(database.String(100))
    last_name = database.Column(database.String(100))
    display_name = database.Column(database.String(200))
    avatar_url = database.Column(database.String(500))
    bio = database.Column(database.Text)
    
    phone_number = database.Column(database.String(20))
    country = database.Column(database.String(100))
    timezone = database.Column(database.String(50), default='UTC')
    language = database.Column(database.String(10), default='en')
    
    is_active = database.Column(database.Boolean, default=True, nullable=False)
    is_verified = database.Column(database.Boolean, default=False, nullable=False)
    is_admin = database.Column(database.Boolean, default=False, nullable=False)
    
    biometric_enabled = database.Column(database.Boolean, default=False, nullable=False)
    two_factor_enabled = database.Column(database.Boolean, default=False, nullable=False)
    two_factor_secret = database.Column(database.String(32))
    
    created_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    updated_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    last_login_at = database.Column(database.DateTime)
    email_verified_at = database.Column(database.DateTime)
    
    biometric_templates = database.relationship(
        'BiometricTemplate',
        back_populates='user',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )
    sessions = database.relationship(
        'UserSession',
        back_populates='user',
        cascade='all, delete-orphan',
        lazy='dynamic'
    )
    
    def __repr__(self) -> str:
        """String representation of User"""
        return f'<User {self.username}>'
    
    def set_password(self, password: str) -> None:
        """
        Hash and set user password
        
        Args:
            password: Plain text password
        """
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password: str) -> bool:
        """
        Verify password against stored hash
        
        Args:
            password: Plain text password to verify
            
        Returns:
            True if password matches, False otherwise
        """
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, password)
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """
        Convert user to dictionary
        
        Args:
            include_sensitive: Whether to include sensitive fields
            
        Returns:
            Dictionary representation of user
        """
        user_dict = {
            'user_id': self.user_id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'display_name': self.display_name,
            'avatar_url': self.avatar_url,
            'bio': self.bio,
            'phone_number': self.phone_number,
            'country': self.country,
            'timezone': self.timezone,
            'language': self.language,
            'is_active': self.is_active,
            'is_verified': self.is_verified,
            'is_admin': self.is_admin,
            'biometric_enabled': self.biometric_enabled,
            'two_factor_enabled': self.two_factor_enabled,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
            'last_login_at': self.last_login_at.isoformat() if self.last_login_at else None,
        }
        
        if include_sensitive:
            user_dict['email_verified_at'] = (
                self.email_verified_at.isoformat() 
                if self.email_verified_at else None
            )
        
        return user_dict


class BiometricTemplate(database.Model):
    """
    Biometric authentication template model
    
    Stores biometric feature templates for multi-modal authentication.
    """
    
    __tablename__ = 'biometric_templates'
    
    template_id = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    
    user_id = database.Column(
        database.String(36),
        database.ForeignKey('users.user_id'),
        nullable=False,
        index=True
    )
    
    biometric_type = database.Column(
        database.String(50),
        nullable=False
    )  # fingerprint, iris, voice, face, behavioral
    
    template_data = database.Column(database.Text, nullable=False)
    template_hash = database.Column(database.String(64), nullable=False, unique=True)
    
    quality_score = database.Column(database.Float, nullable=False)
    feature_count = database.Column(database.Integer)
    
    device_type = database.Column(database.String(100))
    capture_environment = database.Column(database.String(100))
    
    is_active = database.Column(database.Boolean, default=True, nullable=False)
    is_primary = database.Column(database.Boolean, default=False, nullable=False)
    
    enrolled_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    last_verified_at = database.Column(database.DateTime)
    expires_at = database.Column(database.DateTime)  # For periodic re-enrollment
    
    user = database.relationship('User', back_populates='biometric_templates')
    
    def __repr__(self) -> str:
        """String representation of BiometricTemplate"""
        return f'<BiometricTemplate {self.biometric_type} for user {self.user_id}>'
    
    def to_dict(self, include_template: bool = False) -> dict:
        """
        Convert biometric template to dictionary
        
        Args:
            include_template: Whether to include template data (sensitive)
            
        Returns:
            Dictionary representation
        """
        template_dict = {
            'template_id': self.template_id,
            'user_id': self.user_id,
            'biometric_type': self.biometric_type,
            'template_hash': self.template_hash,
            'quality_score': self.quality_score,
            'feature_count': self.feature_count,
            'device_type': self.device_type,
            'is_active': self.is_active,
            'is_primary': self.is_primary,
            'enrolled_at': self.enrolled_at.isoformat() if self.enrolled_at else None,
            'last_verified_at': (
                self.last_verified_at.isoformat() 
                if self.last_verified_at else None
            ),
        }
        
        if include_template:
            template_dict['template_data'] = self.template_data
        
        return template_dict


class UserSession(database.Model):
    """
    User session model for tracking active sessions
    
    Tracks user login sessions for security and multi-device management.
    """
    
    __tablename__ = 'user_sessions'
    
    session_id = database.Column(
        database.String(36),
        primary_key=True,
        nullable=False
    )
    
    user_id = database.Column(
        database.String(36),
        database.ForeignKey('users.user_id'),
        nullable=False,
        index=True
    )
    
    access_token_hash = database.Column(database.String(64), nullable=False)
    refresh_token_hash = database.Column(database.String(64))
    
    device_type = database.Column(database.String(100))
    device_name = database.Column(database.String(200))
    user_agent = database.Column(database.String(500))
    
    ip_address = database.Column(database.String(45))  # IPv6 compatible
    geolocation = database.Column(database.String(200))
    
    authentication_method = database.Column(
        database.String(50),
        nullable=False
    )  # password, biometric, multi_factor
    
    is_active = database.Column(database.Boolean, default=True, nullable=False)
    
    created_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow
    )
    last_activity_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )
    expires_at = database.Column(database.DateTime, nullable=False)
    revoked_at = database.Column(database.DateTime)
    
    user = database.relationship('User', back_populates='sessions')
    
    def __repr__(self) -> str:
        """String representation of UserSession"""
        return f'<UserSession {self.session_id} for user {self.user_id}>'
    
    def is_expired(self) -> bool:
        """
        Check if session is expired
        
        Returns:
            True if session has expired, False otherwise
        """
        if not self.is_active:
            return True
        
        if self.expires_at and datetime.utcnow() > self.expires_at:
            return True
        
        return False
    
    def revoke(self) -> None:
        """Revoke the session"""
        self.is_active = False
        self.revoked_at = datetime.utcnow()
    
    def to_dict(self) -> dict:
        """
        Convert session to dictionary
        
        Returns:
            Dictionary representation
        """
        return {
            'session_id': self.session_id,
            'user_id': self.user_id,
            'device_type': self.device_type,
            'device_name': self.device_name,
            'ip_address': self.ip_address,
            'geolocation': self.geolocation,
            'authentication_method': self.authentication_method,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'last_activity_at': (
                self.last_activity_at.isoformat() 
                if self.last_activity_at else None
            ),
            'expires_at': self.expires_at.isoformat() if self.expires_at else None,
            'is_expired': self.is_expired(),
        }


__all__ = [
    'User',
    'BiometricTemplate',
    'UserSession',
]
