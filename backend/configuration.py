"""
International Plebeian Academy - Configuration Management
Central configuration module for backend application

This module handles all configuration settings for the backend application,
including database connections, blockchain settings, security parameters,
and feature flags.

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

import os
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()


class ConfigurationBase:
    """Base configuration class with common settings"""
    
    APPLICATION_NAME = 'International Plebeian Academy'
    APPLICATION_VERSION = '1.0.0'
    APPLICATION_DESCRIPTION = 'Holographic Distributed Platform for Global Peace Advocacy'
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'change-this-secret-key-in-production')
    DEBUG = False
    TESTING = False
    
    HOST = os.getenv('HOST', '0.0.0.0')
    PORT = int(os.getenv('PORT', '8000'))
    
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'sqlite:///academy.db'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_RECYCLE = 3600
    SQLALCHEMY_MAX_OVERFLOW = 20
    
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'change-this-jwt-secret')
    JWT_ACCESS_TOKEN_EXPIRES = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '3600'))
    JWT_REFRESH_TOKEN_EXPIRES = int(os.getenv('JWT_REFRESH_TOKEN_EXPIRES', '2592000'))
    JWT_ALGORITHM = 'HS256'
    
    CORS_ORIGINS = os.getenv(
        'CORS_ORIGINS',
        'http://localhost:5173,http://localhost:3000'
    ).split(',')
    CORS_METHODS = ['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS']
    CORS_ALLOW_HEADERS = ['Content-Type', 'Authorization']
    CORS_SUPPORTS_CREDENTIALS = True
    
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER', './uploads')
    MAX_CONTENT_LENGTH = int(os.getenv('MAX_CONTENT_LENGTH', '16777216'))  # 16MB
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'doc', 'docx'}
    
    ETHEREUM_RPC_URL = os.getenv(
        'ETHEREUM_RPC_URL',
        'https://mainnet.infura.io/v3/YOUR_INFURA_KEY'
    )
    POLYGON_RPC_URL = os.getenv(
        'POLYGON_RPC_URL',
        'https://polygon-rpc.com'
    )
    BLOCKCHAIN_NETWORK = os.getenv('BLOCKCHAIN_NETWORK', 'testnet')
    TRIBAL_COIN_CONTRACT_ADDRESS = os.getenv(
        'TRIBAL_COIN_CONTRACT_ADDRESS',
        '0x0000000000000000000000000000000000000000'
    )
    FILE_VERIFICATION_CONTRACT_ADDRESS = os.getenv(
        'FILE_VERIFICATION_CONTRACT_ADDRESS',
        '0x0000000000000000000000000000000000000000'
    )
    GOVERNANCE_CONTRACT_ADDRESS = os.getenv(
        'GOVERNANCE_CONTRACT_ADDRESS',
        '0x0000000000000000000000000000000000000000'
    )
    
    REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
    CELERY_BROKER_URL = os.getenv('CELERY_BROKER_URL', 'redis://localhost:6379/0')
    CELERY_RESULT_BACKEND = os.getenv('CELERY_RESULT_BACKEND', 'redis://localhost:6379/0')
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_RESULT_SERIALIZER = 'json'
    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TIMEZONE = 'UTC'
    CELERY_ENABLE_UTC = True
    
    WEBSOCKET_MESSAGE_QUEUE = os.getenv('WEBSOCKET_MESSAGE_QUEUE', None)
    WEBSOCKET_ASYNC_MODE = 'eventlet'
    
    MANUS_CORE_URL = os.getenv(
        'MANUS_CORE_URL',
        'https://manus-static-core.example.com'
    )
    MANUS_VERIFICATION_ENABLED = os.getenv('MANUS_VERIFICATION_ENABLED', 'True') == 'True'
    MANUS_VERIFICATION_INTERVAL_SECONDS = int(os.getenv('MANUS_VERIFICATION_INTERVAL_SECONDS', '3600'))
    
    BIOMETRIC_ENABLED = os.getenv('BIOMETRIC_ENABLED', 'False') == 'True'
    BIOMETRIC_TIMEOUT_SECONDS = int(os.getenv('BIOMETRIC_TIMEOUT', '30'))
    BIOMETRIC_SUPPORTED_TYPES = ['fingerprint', 'iris', 'voice', 'face', 'behavioral']
    
    BOT_ENABLED = os.getenv('BOT_ENABLED', 'True') == 'True'
    BOT_TASK_TIMEOUT_SECONDS = int(os.getenv('BOT_TASK_TIMEOUT', '300'))
    BOT_MAX_RETRIES = int(os.getenv('BOT_MAX_RETRIES', '3'))
    BOT_TOTAL_COUNT = 35
    BOT_DIVISIONS = [
        'communications',
        'human_development',
        'support_resource',
        'action_project',
        'integrity_quality',
        'membership_voice',
        'strategic_direction'
    ]
    BOT_BOTS_PER_DIVISION = 5
    
    DISTRIBUTION_ENABLED = os.getenv('DISTRIBUTION_ENABLED', 'False') == 'True'
    REPLICATION_FACTOR = int(os.getenv('REPLICATION_FACTOR', '7'))
    NODE_ID = os.getenv('NODE_ID', 'primary-node-1')
    HOLOGRAPHIC_ENGINE_ENABLED = os.getenv('HOLOGRAPHIC_ENGINE_ENABLED', 'False') == 'True'
    
    PASSWORD_MIN_LENGTH = 12
    PASSWORD_REQUIRE_UPPERCASE = True
    PASSWORD_REQUIRE_LOWERCASE = True
    PASSWORD_REQUIRE_NUMBERS = True
    PASSWORD_REQUIRE_SPECIAL_CHARACTERS = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    PERMANENT_SESSION_LIFETIME = 3600
    
    RATE_LIMIT_ENABLED = os.getenv('RATE_LIMIT_ENABLED', 'True') == 'True'
    RATE_LIMIT_PER_MINUTE = int(os.getenv('RATE_LIMIT_PER_MINUTE', '60'))
    RATE_LIMIT_STORAGE_URL = REDIS_URL
    
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    LOG_FILE = os.getenv('LOG_FILE', './logs/academy.log')
    LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOG_MAX_BYTES = 10485760  # 10MB
    LOG_BACKUP_COUNT = 10
    
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.example.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', '587'))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', 'True') == 'True'
    MAIL_USE_SSL = os.getenv('MAIL_USE_SSL', 'False') == 'True'
    MAIL_USERNAME = os.getenv('MAIL_USERNAME', 'your-email@example.com')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD', 'your-email-password')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@plebeiantribunalsa.co.za')
    
    ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', 'admin@plebeiantribunalsa.co.za')
    ADMIN_USERNAME = os.getenv('ADMIN_USERNAME', 'admin')
    
    PROMETHEUS_PORT = int(os.getenv('PROMETHEUS_PORT', '9090'))
    ENABLE_METRICS = os.getenv('ENABLE_METRICS', 'True') == 'True'
    METRICS_ENDPOINT = '/metrics'
    
    ENABLE_BIOMETRIC_AUTH = BIOMETRIC_ENABLED
    ENABLE_BOT_SYSTEM = BOT_ENABLED
    ENABLE_BLOCKCHAIN = True
    ENABLE_HOLOGRAPHIC_DISTRIBUTION = DISTRIBUTION_ENABLED
    ENABLE_WEBSOCKETS = True
    ENABLE_FILE_VERIFICATION = True
    ENABLE_GOVERNANCE = True
    
    DEFAULT_PAGE_SIZE = 20
    MAX_PAGE_SIZE = 100
    
    CACHE_TYPE = 'redis'
    CACHE_REDIS_URL = REDIS_URL
    CACHE_DEFAULT_TIMEOUT = 300
    
    @staticmethod
    def initialize_application(application):
        """
        Initialize application with configuration
        
        Args:
            application: Flask application instance
        """
        os.makedirs(ConfigurationBase.UPLOAD_FOLDER, exist_ok=True)
        os.makedirs(os.path.dirname(ConfigurationBase.LOG_FILE), exist_ok=True)


class DevelopmentConfiguration(ConfigurationBase):
    """Development environment configuration"""
    
    DEBUG = True
    TESTING = False
    SQLALCHEMY_ECHO = True
    
    SESSION_COOKIE_SECURE = False  # Allow non-HTTPS in development
    CORS_ORIGINS = ['http://localhost:5173', 'http://localhost:3000', 'http://127.0.0.1:5173']


class TestingConfiguration(ConfigurationBase):
    """Testing environment configuration"""
    
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_ECHO = False
    
    BIOMETRIC_ENABLED = False
    DISTRIBUTION_ENABLED = False
    MANUS_VERIFICATION_ENABLED = False
    
    JWT_ACCESS_TOKEN_EXPIRES = 60
    BOT_TASK_TIMEOUT_SECONDS = 10


class ProductionConfiguration(ConfigurationBase):
    """Production environment configuration"""
    
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = False
    
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Strict'
    
    BIOMETRIC_ENABLED = True
    DISTRIBUTION_ENABLED = True
    MANUS_VERIFICATION_ENABLED = True
    HOLOGRAPHIC_ENGINE_ENABLED = True
    
    LOG_LEVEL = 'WARNING'


configuration_by_environment = {
    'development': DevelopmentConfiguration,
    'testing': TestingConfiguration,
    'production': ProductionConfiguration,
    'default': DevelopmentConfiguration
}


def get_configuration(environment_name: str = None) -> type:
    """
    Get configuration class for specified environment
    
    Args:
        environment_name: Environment name (development/testing/production)
        
    Returns:
        Configuration class for the environment
    """
    if environment_name is None:
        environment_name = os.getenv('FLASK_ENV', 'development')
    
    return configuration_by_environment.get(
        environment_name,
        configuration_by_environment['default']
    )


current_environment = os.getenv('FLASK_ENV', 'development')
Configuration = get_configuration(current_environment)
