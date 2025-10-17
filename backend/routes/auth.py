"""
International Plebeian Academy - Authentication Routes
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

from flask import Blueprint, request, jsonify
from functools import wraps
import jwt
import os
from datetime import datetime, timedelta
from backend.models.user import User
from backend.services.biometric_service import BiometricService

auth_blueprint = Blueprint('auth', __name__)
biometric_service = BiometricService()

SECRET_KEY = os.environ.get('JWT_SECRET_KEY', 'development-secret-key')

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization')
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
            
        try:
            token = token.replace('Bearer ', '')
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = User.query.get(data['user_id'])
        except Exception as e:
            return jsonify({'message': 'Token is invalid'}), 401
            
        return f(current_user, *args, **kwargs)
    
    return decorated

@auth_blueprint.route('/api/authentication/biometric/authenticate', methods=['POST'])
def authenticate_biometric():
    """
    Authenticate user using biometric data
    """
    try:
        data = request.get_json()
        biometric_type = data.get('biometric_type')
        biometric_data = data.get('biometric_data')
        device_id = data.get('device_id')
        
        if not biometric_type or not biometric_data:
            return jsonify({'error': 'Missing required fields'}), 400
        
        user = biometric_service.authenticate(
            biometric_type=biometric_type,
            biometric_data=biometric_data,
            device_id=device_id
        )
        
        if not user:
            return jsonify({'error': 'Authentication failed'}), 401
        
        access_token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        refresh_token = jwt.encode({
            'user_id': user.id,
            'exp': datetime.utcnow() + timedelta(days=30)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'access_token': access_token,
            'refresh_token': refresh_token,
            'user': {
                'id': user.id,
                'email': user.email,
                'name': user.name,
                'roles': user.roles
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@auth_blueprint.route('/api/authentication/refresh', methods=['POST'])
def refresh_token():
    """
    Refresh access token
    """
    try:
        data = request.get_json()
        refresh_token = data.get('refresh_token')
        
        if not refresh_token:
            return jsonify({'error': 'Missing refresh token'}), 400
        
        decoded = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])
        user_id = decoded['user_id']
        
        new_access_token = jwt.encode({
            'user_id': user_id,
            'exp': datetime.utcnow() + timedelta(hours=24)
        }, SECRET_KEY, algorithm='HS256')
        
        return jsonify({
            'access_token': new_access_token
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@auth_blueprint.route('/api/authentication/logout', methods=['POST'])
@token_required
def logout(current_user):
    """
    Logout user
    """
    return jsonify({'message': 'Logged out successfully'}), 200
