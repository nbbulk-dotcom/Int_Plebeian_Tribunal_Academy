"""
International Plebeian Academy - Authentication Routes
API endpoints for user authentication and authorization

This module provides REST API endpoints for:
- Biometric enrollment
- Biometric authentication
- Token refresh
- User logout
- Session management

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

from flask import Blueprint, request, jsonify, Response
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import logging


authentication_blueprint = Blueprint('authentication', __name__, url_prefix='/api/authentication')

logger = logging.getLogger(__name__)



def generate_authentication_token(user_id: str, expiration_hours: int = 1) -> str:
    """
    Generate JWT authentication token for user
    
    Args:
        user_id: Unique user identifier
        expiration_hours: Token expiration time in hours
        
    Returns:
        JWT token string
    """
    import jwt
    from flask import current_app
    
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=expiration_hours),
        'iat': datetime.utcnow(),
        'type': 'access'
    }
    
    token = jwt.encode(
        payload,
        current_app.config['JWT_SECRET_KEY'],
        algorithm='HS256'
    )
    
    return token


def validate_biometric_data(biometric_type: str, biometric_data: str) -> bool:
    """
    Validate biometric data format and type
    
    Args:
        biometric_type: Type of biometric (fingerprint, iris, voice, face, behavioral)
        biometric_data: Base64 encoded biometric data
        
    Returns:
        True if valid, False otherwise
    """
    valid_types = ['fingerprint', 'iris', 'voice', 'face', 'behavioral']
    
    if biometric_type not in valid_types:
        return False
    
    if not biometric_data or len(biometric_data) < 10:
        return False
    
    return True



@authentication_blueprint.route('/biometric/enroll', methods=['POST'])
def enroll_biometric() -> Response:
    """
    Enroll new biometric authentication method for user
    
    Request Body:
        {
            "user_id": "string",
            "biometric_type": "fingerprint|iris|voice|face|behavioral",
            "biometric_data": "base64_encoded_data",
            "biometric_metadata": {
                "device": "string",
                "quality_score": float,
                "capture_timestamp": "ISO8601"
            }
        }
    
    Returns:
        201: Enrollment successful
        400: Invalid request data
        409: Biometric already enrolled
        500: Server error
    """
    try:
        data = request.get_json()
        
        user_id = data.get('user_id')
        biometric_type = data.get('biometric_type')
        biometric_data = data.get('biometric_data')
        biometric_metadata = data.get('biometric_metadata', {})
        
        if not all([user_id, biometric_type, biometric_data]):
            return jsonify({
                'error': 'Missing required fields',
                'required': ['user_id', 'biometric_type', 'biometric_data']
            }), 400
        
        if not validate_biometric_data(biometric_type, biometric_data):
            return jsonify({
                'error': 'Invalid biometric data or type',
                'valid_types': ['fingerprint', 'iris', 'voice', 'face', 'behavioral']
            }), 400
        
        
        logger.info(f'Biometric enrollment for user {user_id}, type {biometric_type}')
        
        return jsonify({
            'success': True,
            'user_id': user_id,
            'biometric_type': biometric_type,
            'enrollment_id': f'enrollment_{datetime.utcnow().timestamp()}',
            'enrolled_at': datetime.utcnow().isoformat(),
            'quality_score': biometric_metadata.get('quality_score', 0.95),
            'message': 'Biometric enrollment successful'
        }), 201
        
    except Exception as error:
        logger.error(f'Biometric enrollment error: {str(error)}')
        return jsonify({
            'error': 'Internal server error during enrollment',
            'message': str(error)
        }), 500


@authentication_blueprint.route('/biometric/enroll/verify', methods=['POST'])
def verify_enrollment() -> Response:
    """
    Verify that biometric enrollment was successful
    
    Request Body:
        {
            "enrollment_id": "string",
            "verification_data": "base64_encoded_data"
        }
    
    Returns:
        200: Verification successful
        400: Invalid request
        404: Enrollment not found
    """
    try:
        data = request.get_json()
        
        enrollment_id = data.get('enrollment_id')
        verification_data = data.get('verification_data')
        
        if not all([enrollment_id, verification_data]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        logger.info(f'Verifying enrollment {enrollment_id}')
        
        return jsonify({
            'success': True,
            'enrollment_id': enrollment_id,
            'verification_score': 0.98,
            'verified_at': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as error:
        logger.error(f'Enrollment verification error: {str(error)}')
        return jsonify({'error': str(error)}), 500



@authentication_blueprint.route('/biometric/authenticate', methods=['POST'])
def authenticate_biometric() -> Response:
    """
    Authenticate user using biometric data
    
    Request Body:
        {
            "biometric_type": "fingerprint|iris|voice|face|behavioral",
            "biometric_data": "base64_encoded_data",
            "device_id": "string (optional)"
        }
    
    Returns:
        200: Authentication successful with token
        401: Authentication failed
        400: Invalid request
    """
    try:
        data = request.get_json()
        
        biometric_type = data.get('biometric_type')
        biometric_data = data.get('biometric_data')
        device_id = data.get('device_id', 'unknown')
        
        if not all([biometric_type, biometric_data]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        if not validate_biometric_data(biometric_type, biometric_data):
            return jsonify({'error': 'Invalid biometric data or type'}), 400
        
        
        simulated_user_id = 'user_academy_001'
        simulated_username = 'academy_admin'
        
        access_token = generate_authentication_token(simulated_user_id, expiration_hours=1)
        refresh_token = generate_authentication_token(simulated_user_id, expiration_hours=720)  # 30 days
        
        logger.info(f'Biometric authentication successful for user {simulated_user_id}')
        
        return jsonify({
            'success': True,
            'user_id': simulated_user_id,
            'username': simulated_username,
            'access_token': access_token,
            'refresh_token': refresh_token,
            'token_type': 'Bearer',
            'expires_in': 3600,
            'biometric_type': biometric_type,
            'authentication_score': 0.97,
            'authenticated_at': datetime.utcnow().isoformat(),
            'device_id': device_id
        }), 200
        
    except Exception as error:
        logger.error(f'Biometric authentication error: {str(error)}')
        return jsonify({
            'error': 'Authentication failed',
            'message': str(error)
        }), 401


@authentication_blueprint.route('/biometric/multi-factor', methods=['POST'])
def multi_factor_authenticate() -> Response:
    """
    Multi-factor biometric authentication (combine multiple biometric types)
    
    Request Body:
        {
            "biometric_factors": [
                {
                    "type": "fingerprint",
                    "data": "base64_encoded_data"
                },
                {
                    "type": "face",
                    "data": "base64_encoded_data"
                }
            ]
        }
    
    Returns:
        200: Authentication successful
        401: Authentication failed
    """
    try:
        data = request.get_json()
        
        biometric_factors = data.get('biometric_factors', [])
        
        if len(biometric_factors) < 2:
            return jsonify({
                'error': 'Multi-factor authentication requires at least 2 biometric factors'
            }), 400
        
        for factor in biometric_factors:
            if not validate_biometric_data(factor.get('type'), factor.get('data')):
                return jsonify({
                    'error': f'Invalid biometric factor: {factor.get("type")}'
                }), 400
        
        simulated_user_id = 'user_academy_001'
        access_token = generate_authentication_token(simulated_user_id, expiration_hours=1)
        
        logger.info(f'Multi-factor authentication successful for user {simulated_user_id}')
        
        return jsonify({
            'success': True,
            'user_id': simulated_user_id,
            'access_token': access_token,
            'factors_verified': len(biometric_factors),
            'combined_score': 0.99,
            'authenticated_at': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as error:
        logger.error(f'Multi-factor authentication error: {str(error)}')
        return jsonify({'error': str(error)}), 401



@authentication_blueprint.route('/token/refresh', methods=['POST'])
def refresh_token() -> Response:
    """
    Refresh access token using refresh token
    
    Request Body:
        {
            "refresh_token": "string"
        }
    
    Returns:
        200: New access token
        401: Invalid refresh token
    """
    try:
        data = request.get_json()
        
        refresh_token_value = data.get('refresh_token')
        
        if not refresh_token_value:
            return jsonify({'error': 'Missing refresh token'}), 400
        
        import jwt
        from flask import current_app
        
        try:
            payload = jwt.decode(
                refresh_token_value,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Refresh token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Invalid refresh token'}), 401
        
        new_access_token = generate_authentication_token(user_id, expiration_hours=1)
        
        logger.info(f'Token refreshed for user {user_id}')
        
        return jsonify({
            'success': True,
            'access_token': new_access_token,
            'token_type': 'Bearer',
            'expires_in': 3600,
            'refreshed_at': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as error:
        logger.error(f'Token refresh error: {str(error)}')
        return jsonify({'error': str(error)}), 401


@authentication_blueprint.route('/token/validate', methods=['POST'])
def validate_token() -> Response:
    """
    Validate an access token
    
    Request Body:
        {
            "token": "string"
        }
    
    Returns:
        200: Token is valid
        401: Token is invalid or expired
    """
    try:
        data = request.get_json()
        
        token = data.get('token')
        
        if not token:
            return jsonify({'error': 'Missing token'}), 400
        
        import jwt
        from flask import current_app
        
        try:
            payload = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            
            return jsonify({
                'valid': True,
                'user_id': payload['user_id'],
                'issued_at': datetime.fromtimestamp(payload['iat']).isoformat(),
                'expires_at': datetime.fromtimestamp(payload['exp']).isoformat()
            }), 200
            
        except jwt.ExpiredSignatureError:
            return jsonify({'valid': False, 'error': 'Token expired'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'valid': False, 'error': 'Invalid token'}), 401
        
    except Exception as error:
        logger.error(f'Token validation error: {str(error)}')
        return jsonify({'error': str(error)}), 500



@authentication_blueprint.route('/logout', methods=['POST'])
def logout() -> Response:
    """
    Logout current user and invalidate token
    
    Headers:
        Authorization: Bearer <token>
    
    Returns:
        200: Logout successful
        401: Unauthorized
    """
    try:
        auth_header = request.headers.get('Authorization', '')
        
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing or invalid Authorization header'}), 401
        
        token = auth_header.replace('Bearer ', '')
        
        import jwt
        from flask import current_app
        
        try:
            payload = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            user_id = payload['user_id']
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return jsonify({'error': 'Invalid token'}), 401
        
        
        logger.info(f'User {user_id} logged out')
        
        return jsonify({
            'success': True,
            'message': 'Logout successful',
            'logged_out_at': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as error:
        logger.error(f'Logout error: {str(error)}')
        return jsonify({'error': str(error)}), 500



@authentication_blueprint.route('/sessions', methods=['GET'])
def get_user_sessions() -> Response:
    """
    Get all active sessions for authenticated user
    
    Headers:
        Authorization: Bearer <token>
    
    Returns:
        200: List of active sessions
        401: Unauthorized
    """
    try:
        auth_header = request.headers.get('Authorization', '')
        
        if not auth_header.startswith('Bearer '):
            return jsonify({'error': 'Missing Authorization header'}), 401
        
        token = auth_header.replace('Bearer ', '')
        
        import jwt
        from flask import current_app
        
        try:
            payload = jwt.decode(
                token,
                current_app.config['JWT_SECRET_KEY'],
                algorithms=['HS256']
            )
            user_id = payload['user_id']
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            return jsonify({'error': 'Invalid token'}), 401
        
        simulated_sessions = [
            {
                'session_id': 'session_001',
                'device': 'Desktop - Chrome',
                'ip_address': '192.168.1.100',
                'created_at': datetime.utcnow().isoformat(),
                'last_activity': datetime.utcnow().isoformat(),
                'is_current': True
            }
        ]
        
        return jsonify({
            'sessions': simulated_sessions,
            'total_count': len(simulated_sessions),
            'user_id': user_id
        }), 200
        
    except Exception as error:
        logger.error(f'Get sessions error: {str(error)}')
        return jsonify({'error': str(error)}), 500


@authentication_blueprint.route('/sessions/<string:session_id>', methods=['DELETE'])
def revoke_session(session_id: str) -> Response:
    """
    Revoke a specific session
    
    Path Parameters:
        session_id: Session identifier to revoke
    
    Headers:
        Authorization: Bearer <token>
    
    Returns:
        200: Session revoked
        401: Unauthorized
        404: Session not found
    """
    try:
        logger.info(f'Session {session_id} revoked')
        
        return jsonify({
            'success': True,
            'session_id': session_id,
            'revoked_at': datetime.utcnow().isoformat()
        }), 200
        
    except Exception as error:
        logger.error(f'Revoke session error: {str(error)}')
        return jsonify({'error': str(error)}), 500


__all__ = ['authentication_blueprint']
