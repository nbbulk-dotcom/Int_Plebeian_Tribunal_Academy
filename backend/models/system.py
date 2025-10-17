"""
International Plebeian Academy - System Models
Database models for system configuration and metrics

Models:
- SystemConfiguration: System-wide configuration settings
- SystemMetrics: Real-time system performance metrics
- SystemAlert: System alerts and notifications
- SystemAuditLog: Audit trail for system changes

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

from datetime import datetime
from typing import Dict, Any, Optional
import json

from . import database


class SystemConfiguration(database.Model):
    """
    System configuration model
    
    Stores system-wide configuration settings that can be
    updated at runtime without code changes.
    """
    
    __tablename__ = 'system_configurations'
    
    configuration_id = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    
    configuration_key = database.Column(
        database.String(100),
        nullable=False,
        unique=True,
        index=True
    )
    
    configuration_value = database.Column(database.Text, nullable=False)
    
    configuration_category = database.Column(
        database.String(50),
        nullable=False,
        index=True
    )  # system, security, blockchain, bots, distribution
    
    configuration_description = database.Column(database.Text)
    configuration_data_type = database.Column(
        database.String(20),
        nullable=False
    )  # string, integer, float, boolean, json
    
    default_value = database.Column(database.Text)
    is_required = database.Column(database.Boolean, default=False, nullable=False)
    is_sensitive = database.Column(database.Boolean, default=False, nullable=False)
    
    is_active = database.Column(database.Boolean, default=True, nullable=False)
    
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
    updated_by = database.Column(database.String(36))  # user_id
    
    def __repr__(self) -> str:
        """String representation of SystemConfiguration"""
        return f'<SystemConfiguration {self.configuration_key}>'
    
    def get_value(self) -> Any:
        """
        Get parsed configuration value
        
        Returns:
            Parsed value based on data type
        """
        if self.configuration_data_type == 'json':
            return json.loads(self.configuration_value)
        elif self.configuration_data_type == 'integer':
            return int(self.configuration_value)
        elif self.configuration_data_type == 'float':
            return float(self.configuration_value)
        elif self.configuration_data_type == 'boolean':
            return self.configuration_value.lower() in ('true', '1', 'yes')
        else:  # string
            return self.configuration_value
    
    def set_value(self, value: Any) -> None:
        """
        Set configuration value with type conversion
        
        Args:
            value: New configuration value
        """
        if self.configuration_data_type == 'json':
            self.configuration_value = json.dumps(value)
        else:
            self.configuration_value = str(value)
        
        self.updated_at = datetime.utcnow()
    
    def to_dict(self, include_sensitive: bool = False) -> dict:
        """
        Convert configuration to dictionary
        
        Args:
            include_sensitive: Whether to include sensitive values
            
        Returns:
            Dictionary representation
        """
        config_dict = {
            'configuration_id': self.configuration_id,
            'configuration_key': self.configuration_key,
            'configuration_category': self.configuration_category,
            'configuration_description': self.configuration_description,
            'configuration_data_type': self.configuration_data_type,
            'is_required': self.is_required,
            'is_sensitive': self.is_sensitive,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }
        
        if not self.is_sensitive or include_sensitive:
            config_dict['configuration_value'] = self.get_value()
        else:
            config_dict['configuration_value'] = '***HIDDEN***'
        
        return config_dict


class SystemMetrics(database.Model):
    """
    System metrics model
    
    Stores time-series system performance metrics for monitoring
    and analysis.
    """
    
    __tablename__ = 'system_metrics'
    
    metric_id = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    
    metric_name = database.Column(
        database.String(100),
        nullable=False,
        index=True
    )
    metric_value = database.Column(database.Float, nullable=False)
    metric_unit = database.Column(database.String(20))
    
    metric_category = database.Column(
        database.String(50),
        nullable=False,
        index=True
    )  # cpu, memory, disk, network, database, application
    
    node_id = database.Column(database.String(50))  # For distributed systems
    component = database.Column(database.String(100))  # Specific component being measured
    
    metadata = database.Column(database.Text)  # JSON encoded additional data
    
    recorded_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow,
        index=True
    )
    
    def __repr__(self) -> str:
        """String representation of SystemMetrics"""
        return f'<SystemMetrics {self.metric_name}={self.metric_value}>'
    
    def to_dict(self) -> dict:
        """
        Convert metric to dictionary
        
        Returns:
            Dictionary representation
        """
        metric_dict = {
            'metric_id': self.metric_id,
            'metric_name': self.metric_name,
            'metric_value': self.metric_value,
            'metric_unit': self.metric_unit,
            'metric_category': self.metric_category,
            'node_id': self.node_id,
            'component': self.component,
            'recorded_at': self.recorded_at.isoformat() if self.recorded_at else None,
        }
        
        if self.metadata:
            try:
                metric_dict['metadata'] = json.loads(self.metadata)
            except json.JSONDecodeError:
                metric_dict['metadata'] = {}
        
        return metric_dict


class SystemAlert(database.Model):
    """
    System alert model
    
    Stores system alerts and notifications for administrators.
    """
    
    __tablename__ = 'system_alerts'
    
    alert_id = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    
    alert_type = database.Column(
        database.String(50),
        nullable=False,
        index=True
    )  # error, warning, info, critical
    
    alert_category = database.Column(
        database.String(50),
        nullable=False
    )  # system, security, performance, blockchain, bots
    
    alert_title = database.Column(database.String(200), nullable=False)
    alert_message = database.Column(database.Text, nullable=False)
    
    component = database.Column(database.String(100))
    node_id = database.Column(database.String(50))
    
    alert_data = database.Column(database.Text)  # JSON encoded details
    
    is_acknowledged = database.Column(database.Boolean, default=False, nullable=False)
    is_resolved = database.Column(database.Boolean, default=False, nullable=False)
    
    created_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow,
        index=True
    )
    acknowledged_at = database.Column(database.DateTime)
    acknowledged_by = database.Column(database.String(36))  # user_id
    resolved_at = database.Column(database.DateTime)
    resolved_by = database.Column(database.String(36))  # user_id
    
    def __repr__(self) -> str:
        """String representation of SystemAlert"""
        return f'<SystemAlert {self.alert_type}: {self.alert_title}>'
    
    def acknowledge(self, user_id: str) -> None:
        """
        Mark alert as acknowledged
        
        Args:
            user_id: ID of user acknowledging the alert
        """
        self.is_acknowledged = True
        self.acknowledged_at = datetime.utcnow()
        self.acknowledged_by = user_id
    
    def resolve(self, user_id: str) -> None:
        """
        Mark alert as resolved
        
        Args:
            user_id: ID of user resolving the alert
        """
        self.is_resolved = True
        self.resolved_at = datetime.utcnow()
        self.resolved_by = user_id
        
        if not self.is_acknowledged:
            self.acknowledge(user_id)
    
    def to_dict(self) -> dict:
        """
        Convert alert to dictionary
        
        Returns:
            Dictionary representation
        """
        alert_dict = {
            'alert_id': self.alert_id,
            'alert_type': self.alert_type,
            'alert_category': self.alert_category,
            'alert_title': self.alert_title,
            'alert_message': self.alert_message,
            'component': self.component,
            'node_id': self.node_id,
            'is_acknowledged': self.is_acknowledged,
            'is_resolved': self.is_resolved,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'acknowledged_at': (
                self.acknowledged_at.isoformat() 
                if self.acknowledged_at else None
            ),
            'resolved_at': (
                self.resolved_at.isoformat() 
                if self.resolved_at else None
            ),
        }
        
        if self.alert_data:
            try:
                alert_dict['alert_data'] = json.loads(self.alert_data)
            except json.JSONDecodeError:
                alert_dict['alert_data'] = {}
        
        return alert_dict


class SystemAuditLog(database.Model):
    """
    System audit log model
    
    Tracks all significant system changes and administrative actions
    for security and compliance.
    """
    
    __tablename__ = 'system_audit_logs'
    
    log_id = database.Column(
        database.Integer,
        primary_key=True,
        autoincrement=True
    )
    
    action_type = database.Column(
        database.String(50),
        nullable=False,
        index=True
    )  # create, update, delete, login, logout, configuration_change
    
    action_category = database.Column(
        database.String(50),
        nullable=False,
        index=True
    )  # authentication, system, user, bot, blockchain
    
    action_description = database.Column(database.String(500), nullable=False)
    
    user_id = database.Column(database.String(36), index=True)
    username = database.Column(database.String(100))
    ip_address = database.Column(database.String(45))
    user_agent = database.Column(database.String(500))
    
    resource_type = database.Column(database.String(50))
    resource_id = database.Column(database.String(100))
    
    old_value = database.Column(database.Text)  # JSON encoded
    new_value = database.Column(database.Text)  # JSON encoded
    
    was_successful = database.Column(database.Boolean, nullable=False)
    error_message = database.Column(database.Text)
    
    created_at = database.Column(
        database.DateTime,
        nullable=False,
        default=datetime.utcnow,
        index=True
    )
    
    def __repr__(self) -> str:
        """String representation of SystemAuditLog"""
        return f'<SystemAuditLog {self.action_type} by {self.username}>'
    
    def to_dict(self, include_values: bool = True) -> dict:
        """
        Convert audit log to dictionary
        
        Args:
            include_values: Whether to include old/new values
            
        Returns:
            Dictionary representation
        """
        log_dict = {
            'log_id': self.log_id,
            'action_type': self.action_type,
            'action_category': self.action_category,
            'action_description': self.action_description,
            'user_id': self.user_id,
            'username': self.username,
            'ip_address': self.ip_address,
            'resource_type': self.resource_type,
            'resource_id': self.resource_id,
            'was_successful': self.was_successful,
            'error_message': self.error_message,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
        
        if include_values:
            if self.old_value:
                try:
                    log_dict['old_value'] = json.loads(self.old_value)
                except json.JSONDecodeError:
                    log_dict['old_value'] = self.old_value
            
            if self.new_value:
                try:
                    log_dict['new_value'] = json.loads(self.new_value)
                except json.JSONDecodeError:
                    log_dict['new_value'] = self.new_value
        
        return log_dict


__all__ = [
    'SystemConfiguration',
    'SystemMetrics',
    'SystemAlert',
    'SystemAuditLog',
]
