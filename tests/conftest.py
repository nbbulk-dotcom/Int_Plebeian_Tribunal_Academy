"""
International Plebeian Academy - Pytest Configuration
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def app():
    """
    Create Flask application for testing
    """
    from backend.app import create_app
    
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    return app

@pytest.fixture
def client(app):
    """
    Create test client
    """
    return app.test_client()

@pytest.fixture
def runner(app):
    """
    Create CLI runner
    """
    return app.test_cli_runner()

@pytest.fixture
def auth_headers():
    """
    Create authentication headers for testing
    """
    return {
        'Authorization': 'Bearer test-token',
        'Content-Type': 'application/json'
    }

@pytest.fixture
def sample_user():
    """
    Create sample user data
    """
    return {
        'id': '12345',
        'email': 'test@example.com',
        'name': 'Test User',
        'roles': ['member']
    }

@pytest.fixture
def sample_bot():
    """
    Create sample bot data
    """
    return {
        'id': 'bot_12345',
        'name': 'Test Bot',
        'division': 'communications',
        'status': 'active',
        'tasksCompleted': 42,
        'successRate': 95
    }
