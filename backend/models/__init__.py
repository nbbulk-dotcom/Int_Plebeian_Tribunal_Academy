"""
International Plebeian Academy - Database Models Package
SQLAlchemy ORM models for database entities

This package contains all database models organized by domain.

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()


__all__ = [
    'database',
]
