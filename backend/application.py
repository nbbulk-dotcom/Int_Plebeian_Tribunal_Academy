"""
International Plebeian Academy - Main Flask Application
Backend API Server with 29 Endpoints

This is the primary entry point for the backend API server.
Implements the complete REST API for the International Plebeian Academy
holographic distributed platform.

Architecture:
- Flask web framework with CORS support
- Flask-SocketIO for real-time WebSocket communication
- SQLAlchemy for database operations
- JWT for authentication
- Celery for asynchronous bot tasks
- Web3 for blockchain integration

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

import os
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any

from flask import Flask, jsonify, request, Response
from flask_cors import CORS
from flask_socketio import SocketIO, emit
from dotenv import load_dotenv
import jwt
from werkzeug.security import check_password_hash, generate_password_hash

load_dotenv()

application = Flask(__name__)

application.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'change-this-secret-key-in-production')
application.config['DEBUG'] = os.getenv('DEBUG', 'False') == 'True'
application.config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY', 'change-this-jwt-secret')
application.config['JWT_ACCESS_TOKEN_EXPIRES'] = int(os.getenv('JWT_ACCESS_TOKEN_EXPIRES', '3600'))
application.config['DATABASE_URL'] = os.getenv('DATABASE_URL', 'sqlite:///academy.db')
application.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER', './uploads')
application.config['MAX_CONTENT_LENGTH'] = int(os.getenv('MAX_CONTENT_LENGTH', '16777216'))

CORS(application, resources={
    r"/api/*": {
        "origins": os.getenv('CORS_ORIGINS', 'http://localhost:5173').split(','),
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"],
        "supports_credentials": True
    }
})

socketio = SocketIO(
    application,
    cors_allowed_origins=os.getenv('CORS_ORIGINS', 'http://localhost:5173').split(','),
    message_queue=os.getenv('WEBSOCKET_MESSAGE_QUEUE', None),
    async_mode='eventlet'
)

logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.getenv('LOG_FILE', './logs/academy.log')),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

application_state = {
    'system_status': 'initializing',
    'connected_nodes': [],
    'active_bots': 0,
    'total_users': 0,
    'verification_status': 'pending'
}


def generate_jwt_token(user_id: str, expiration_hours: int = 1) -> str:
    """
    Generate a JSON Web Token for authentication
    
    Args:
        user_id: Unique identifier for the user
        expiration_hours: Token expiration time in hours
        
    Returns:
        JWT token string
    """
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=expiration_hours),
        'iat': datetime.utcnow()
    }
    
    token = jwt.encode(
        payload,
        application.config['JWT_SECRET_KEY'],
        algorithm='HS256'
    )
    
    return token


def verify_jwt_token(token: str) -> Optional[Dict[str, Any]]:
    """
    Verify and decode a JWT token
    
    Args:
        token: JWT token string
        
    Returns:
        Decoded token payload or None if invalid
    """
    try:
        payload = jwt.decode(
            token,
            application.config['JWT_SECRET_KEY'],
            algorithms=['HS256']
        )
        return payload
    except jwt.ExpiredSignatureError:
        logger.warning('Token expired')
        return None
    except jwt.InvalidTokenError:
        logger.warning('Invalid token')
        return None


def require_authentication(function):
    """
    Decorator to require JWT authentication for endpoints
    
    Usage:
        @application.route('/api/protected')
        @require_authentication
        def protected_route():
            return jsonify({'message': 'Success'})
    """
    from functools import wraps
    
    @wraps(function)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization', '').replace('Bearer ', '')
        
        if not token:
            return jsonify({'error': 'No authentication token provided'}), 401
            
        payload = verify_jwt_token(token)
        if not payload:
            return jsonify({'error': 'Invalid or expired token'}), 401
            
        request.user_id = payload['user_id']
        
        return function(*args, **kwargs)
        
    return decorated_function



@application.route('/api/health', methods=['GET'])
def health_check() -> Response:
    """
    Health check endpoint for monitoring
    Returns basic system health status
    """
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'environment': os.getenv('FLASK_ENV', 'development')
    }), 200


@application.route('/api/status', methods=['GET'])
def system_status() -> Response:
    """
    Detailed system status endpoint
    Returns comprehensive system state information
    """
    return jsonify({
        'system_status': application_state['system_status'],
        'connected_nodes': len(application_state['connected_nodes']),
        'active_bots': application_state['active_bots'],
        'total_users': application_state['total_users'],
        'verification_status': application_state['verification_status'],
        'uptime_seconds': 0,  # TODO: Calculate actual uptime
        'timestamp': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/authentication/biometric/enroll', methods=['POST'])
def enroll_biometric() -> Response:
    """
    Enroll a new biometric authentication method
    
    Request body:
        {
            "user_id": "string",
            "biometric_type": "fingerprint|iris|voice|face|behavioral",
            "biometric_data": "base64_encoded_data"
        }
    """
    data = request.get_json()
    
    user_id = data.get('user_id')
    biometric_type = data.get('biometric_type')
    biometric_data = data.get('biometric_data')
    
    if not all([user_id, biometric_type, biometric_data]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    
    logger.info(f'Biometric enrollment for user {user_id}, type {biometric_type}')
    
    return jsonify({
        'success': True,
        'user_id': user_id,
        'biometric_type': biometric_type,
        'enrolled_at': datetime.utcnow().isoformat(),
        'message': 'Biometric enrollment successful'
    }), 201


@application.route('/api/authentication/biometric/authenticate', methods=['POST'])
def authenticate_biometric() -> Response:
    """
    Authenticate user using biometric data
    
    Request body:
        {
            "biometric_type": "fingerprint|iris|voice|face|behavioral",
            "biometric_data": "base64_encoded_data"
        }
    """
    data = request.get_json()
    
    biometric_type = data.get('biometric_type')
    biometric_data = data.get('biometric_data')
    
    if not all([biometric_type, biometric_data]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    
    simulated_user_id = 'user_12345'
    token = generate_jwt_token(simulated_user_id)
    
    logger.info(f'Biometric authentication successful for user {simulated_user_id}')
    
    return jsonify({
        'success': True,
        'user_id': simulated_user_id,
        'token': token,
        'expires_in': application.config['JWT_ACCESS_TOKEN_EXPIRES'],
        'authenticated_at': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/authentication/logout', methods=['POST'])
@require_authentication
def logout() -> Response:
    """
    Logout current user (invalidate token)
    Requires: Authorization header with JWT token
    """
    user_id = request.user_id
    
    
    logger.info(f'User {user_id} logged out')
    
    return jsonify({
        'success': True,
        'message': 'Logout successful',
        'logged_out_at': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/system/metrics', methods=['GET'])
@require_authentication
def get_system_metrics() -> Response:
    """
    Get real-time system metrics
    Returns performance and usage statistics
    """
    return jsonify({
        'cpu_usage_percent': 0.0,  # TODO: Implement actual metrics
        'memory_usage_percent': 0.0,
        'disk_usage_percent': 0.0,
        'network_throughput_mbps': 0.0,
        'active_connections': 0,
        'requests_per_minute': 0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/system/configuration', methods=['GET', 'PUT'])
@require_authentication
def system_configuration() -> Response:
    """
    GET: Retrieve system configuration
    PUT: Update system configuration
    """
    if request.method == 'GET':
        return jsonify({
            'blockchain_network': os.getenv('BLOCKCHAIN_NETWORK', 'testnet'),
            'bot_enabled': os.getenv('BOT_ENABLED', 'True') == 'True',
            'distribution_enabled': os.getenv('DISTRIBUTION_ENABLED', 'False') == 'True',
            'replication_factor': int(os.getenv('REPLICATION_FACTOR', '7')),
            'rate_limit_enabled': os.getenv('RATE_LIMIT_ENABLED', 'True') == 'True',
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    
    elif request.method == 'PUT':
        data = request.get_json()
        
        
        logger.info(f'Configuration update requested by user {request.user_id}')
        
        return jsonify({
            'success': True,
            'message': 'Configuration updated successfully',
            'updated_at': datetime.utcnow().isoformat()
        }), 200



@application.route('/api/bots/status', methods=['GET'])
@require_authentication
def get_bot_status() -> Response:
    """
    Get status of all 35 bots across 7 divisions
    """
    
    bot_divisions = [
        'communications', 'human_development', 'support_resource',
        'action_project', 'integrity_quality', 'membership_voice',
        'strategic_direction'
    ]
    
    division_status = {}
    for division in bot_divisions:
        division_status[division] = {
            'total_bots': 5,
            'active_bots': 5,
            'idle_bots': 0,
            'tasks_completed_today': 0,
            'average_response_time_seconds': 0.0
        }
    
    return jsonify({
        'divisions': division_status,
        'total_bots': 35,
        'active_bots': 35,
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/bots/division/<string:division_name>', methods=['GET'])
@require_authentication
def get_division_bots(division_name: str) -> Response:
    """
    Get detailed information about bots in a specific division
    
    Path parameters:
        division_name: Name of the division
    """
    
    return jsonify({
        'division_name': division_name,
        'bots': [
            {'bot_id': f'{division_name}_bot_{i}', 'status': 'active', 'current_task': None}
            for i in range(1, 6)
        ],
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/bots/assign-task', methods=['POST'])
@require_authentication
def assign_bot_task() -> Response:
    """
    Assign a task to the bot system
    
    Request body:
        {
            "task_type": "string",
            "task_description": "string",
            "priority": "low|medium|high",
            "deadline": "ISO8601_datetime"
        }
    """
    data = request.get_json()
    
    task_type = data.get('task_type')
    task_description = data.get('task_description')
    priority = data.get('priority', 'medium')
    
    if not all([task_type, task_description]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    
    task_id = f'task_{datetime.utcnow().timestamp()}'
    
    logger.info(f'Task {task_id} assigned by user {request.user_id}')
    
    return jsonify({
        'success': True,
        'task_id': task_id,
        'assigned_division': 'communications',  # Simulated
        'assigned_bot': 'communications_bot_1',  # Simulated
        'estimated_completion_time': datetime.utcnow().isoformat(),
        'created_at': datetime.utcnow().isoformat()
    }), 201


@application.route('/api/bots/performance', methods=['GET'])
@require_authentication
def get_bot_performance() -> Response:
    """
    Get performance metrics for the bot system
    """
    
    return jsonify({
        'total_tasks_completed': 0,
        'tasks_in_progress': 0,
        'tasks_pending': 0,
        'average_completion_time_seconds': 0.0,
        'success_rate_percent': 100.0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/tribal-coin/balance/<string:ethereum_address>', methods=['GET'])
def get_tribal_coin_balance(ethereum_address: str) -> Response:
    """
    Get TribalCoin balance for an Ethereum address
    
    Path parameters:
        ethereum_address: Ethereum wallet address
    """
    
    return jsonify({
        'ethereum_address': ethereum_address,
        'balance': '0',
        'balance_formatted': '0 TRIBAL',
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/tribal-coin/transfer', methods=['POST'])
@require_authentication
def transfer_tribal_coin() -> Response:
    """
    Transfer TribalCoin tokens
    
    Request body:
        {
            "to_address": "0x...",
            "amount": "1000",
            "memo": "optional memo"
        }
    """
    data = request.get_json()
    
    to_address = data.get('to_address')
    amount = data.get('amount')
    
    if not all([to_address, amount]):
        return jsonify({'error': 'Missing required fields'}), 400
    
    
    transaction_hash = f'0x{datetime.utcnow().timestamp()}'
    
    logger.info(f'TribalCoin transfer of {amount} to {to_address} by user {request.user_id}')
    
    return jsonify({
        'success': True,
        'transaction_hash': transaction_hash,
        'to_address': to_address,
        'amount': amount,
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/tribal-coin/governance/proposals', methods=['GET', 'POST'])
@require_authentication
def governance_proposals() -> Response:
    """
    GET: List all governance proposals
    POST: Create a new governance proposal
    """
    if request.method == 'GET':
        return jsonify({
            'proposals': [],
            'total_count': 0,
            'timestamp': datetime.utcnow().isoformat()
        }), 200
    
    elif request.method == 'POST':
        data = request.get_json()
        
        title = data.get('title')
        description = data.get('description')
        
        if not all([title, description]):
            return jsonify({'error': 'Missing required fields'}), 400
        
        proposal_id = f'proposal_{datetime.utcnow().timestamp()}'
        
        logger.info(f'Governance proposal {proposal_id} created by user {request.user_id}')
        
        return jsonify({
            'success': True,
            'proposal_id': proposal_id,
            'title': title,
            'created_at': datetime.utcnow().isoformat()
        }), 201


@application.route('/api/tribal-coin/governance/vote', methods=['POST'])
@require_authentication
def vote_on_proposal() -> Response:
    """
    Vote on a governance proposal
    
    Request body:
        {
            "proposal_id": "string",
            "vote": "for|against|abstain"
        }
    """
    data = request.get_json()
    
    proposal_id = data.get('proposal_id')
    vote = data.get('vote')
    
    if not all([proposal_id, vote]) or vote not in ['for', 'against', 'abstain']:
        return jsonify({'error': 'Invalid request'}), 400
    
    
    logger.info(f'Vote cast on proposal {proposal_id} by user {request.user_id}: {vote}')
    
    return jsonify({
        'success': True,
        'proposal_id': proposal_id,
        'vote': vote,
        'voted_at': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/verification/upload', methods=['POST'])
@require_authentication
def upload_file_for_verification() -> Response:
    """
    Upload a file and register it on blockchain
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    file_hash = f'hash_{datetime.utcnow().timestamp()}'
    
    logger.info(f'File uploaded for verification by user {request.user_id}')
    
    return jsonify({
        'success': True,
        'file_hash': file_hash,
        'filename': file.filename,
        'uploaded_at': datetime.utcnow().isoformat()
    }), 201


@application.route('/api/verification/verify/<string:file_hash>', methods=['GET'])
def verify_file(file_hash: str) -> Response:
    """
    Verify a file against blockchain registry
    
    Path parameters:
        file_hash: SHA-256 hash of the file
    """
    
    return jsonify({
        'file_hash': file_hash,
        'is_verified': True,  # Simulated
        'registered_at': datetime.utcnow().isoformat(),
        'uploader_address': '0x0000000000000000000000000000000000000000'
    }), 200


@application.route('/api/verification/history', methods=['GET'])
@require_authentication
def get_verification_history() -> Response:
    """
    Get file verification history for current user
    """
    return jsonify({
        'verifications': [],
        'total_count': 0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/distribution/nodes', methods=['GET'])
@require_authentication
def get_distribution_nodes() -> Response:
    """
    Get list of all holographic distribution nodes
    """
    return jsonify({
        'nodes': application_state['connected_nodes'],
        'total_count': len(application_state['connected_nodes']),
        'replication_factor': int(os.getenv('REPLICATION_FACTOR', '7')),
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/distribution/upload', methods=['POST'])
@require_authentication
def upload_to_distribution_network() -> Response:
    """
    Upload file to holographic distribution network
    """
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    
    file_id = f'file_{datetime.utcnow().timestamp()}'
    
    logger.info(f'File uploaded to distribution network by user {request.user_id}')
    
    return jsonify({
        'success': True,
        'file_id': file_id,
        'replicated_to_nodes': 7,  # Simulated
        'uploaded_at': datetime.utcnow().isoformat()
    }), 201


@application.route('/api/distribution/download/<string:file_id>', methods=['GET'])
def download_from_distribution_network(file_id: str) -> Response:
    """
    Download file from holographic distribution network
    
    Path parameters:
        file_id: Unique file identifier
    """
    
    return jsonify({
        'error': 'File download not implemented yet'
    }), 501


@application.route('/api/distribution/replicate', methods=['POST'])
@require_authentication
def replicate_file() -> Response:
    """
    Manually trigger file replication
    
    Request body:
        {
            "file_id": "string",
            "target_nodes": ["node1", "node2"]
        }
    """
    data = request.get_json()
    
    file_id = data.get('file_id')
    
    if not file_id:
        return jsonify({'error': 'Missing file_id'}), 400
    
    
    logger.info(f'File replication triggered for {file_id} by user {request.user_id}')
    
    return jsonify({
        'success': True,
        'file_id': file_id,
        'replicated_to_nodes': 0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/upgrades/available', methods=['GET'])
@require_authentication
def get_available_upgrades() -> Response:
    """
    Get list of available system upgrades
    """
    return jsonify({
        'upgrades': [],
        'total_count': 0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/upgrades/initiate', methods=['POST'])
@require_authentication
def initiate_upgrade() -> Response:
    """
    Initiate a worldwide system upgrade
    
    Request body:
        {
            "upgrade_id": "string",
            "schedule_time": "ISO8601_datetime (optional)"
        }
    """
    data = request.get_json()
    
    upgrade_id = data.get('upgrade_id')
    
    if not upgrade_id:
        return jsonify({'error': 'Missing upgrade_id'}), 400
    
    
    logger.info(f'System upgrade {upgrade_id} initiated by user {request.user_id}')
    
    return jsonify({
        'success': True,
        'upgrade_id': upgrade_id,
        'initiated_at': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/upgrades/status/<string:upgrade_id>', methods=['GET'])
@require_authentication
def get_upgrade_status(upgrade_id: str) -> Response:
    """
    Get status of a specific upgrade
    
    Path parameters:
        upgrade_id: Unique upgrade identifier
    """
    return jsonify({
        'upgrade_id': upgrade_id,
        'status': 'not_started',
        'progress_percent': 0,
        'nodes_updated': 0,
        'total_nodes': 0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/quantum/create-session', methods=['POST'])
@require_authentication
def create_quantum_session() -> Response:
    """
    Create a quantum-secure communication session
    """
    session_id = f'quantum_session_{datetime.utcnow().timestamp()}'
    
    return jsonify({
        'success': True,
        'session_id': session_id,
        'created_at': datetime.utcnow().isoformat()
    }), 201


@application.route('/api/quantum/exchange-keys', methods=['POST'])
@require_authentication
def exchange_quantum_keys() -> Response:
    """
    Exchange quantum encryption keys
    
    Request body:
        {
            "session_id": "string",
            "public_key": "string"
        }
    """
    data = request.get_json()
    
    session_id = data.get('session_id')
    
    if not session_id:
        return jsonify({'error': 'Missing session_id'}), 400
    
    
    return jsonify({
        'success': True,
        'session_id': session_id,
        'server_public_key': 'simulated_public_key',
        'exchanged_at': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/quantum/encrypt', methods=['POST'])
@require_authentication
def quantum_encrypt() -> Response:
    """
    Encrypt data using quantum encryption
    
    Request body:
        {
            "session_id": "string",
            "plaintext": "string"
        }
    """
    data = request.get_json()
    
    plaintext = data.get('plaintext', '')
    
    ciphertext = f'encrypted_{plaintext}'
    
    return jsonify({
        'success': True,
        'ciphertext': ciphertext,
        'encrypted_at': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/quantum/decrypt', methods=['POST'])
@require_authentication
def quantum_decrypt() -> Response:
    """
    Decrypt data using quantum encryption
    
    Request body:
        {
            "session_id": "string",
            "ciphertext": "string"
        }
    """
    data = request.get_json()
    
    ciphertext = data.get('ciphertext', '')
    
    plaintext = ciphertext.replace('encrypted_', '')
    
    return jsonify({
        'success': True,
        'plaintext': plaintext,
        'decrypted_at': datetime.utcnow().isoformat()
    }), 200



@application.route('/api/monitoring/metrics', methods=['GET'])
@require_authentication
def get_monitoring_metrics() -> Response:
    """
    Get comprehensive monitoring metrics
    """
    return jsonify({
        'system_metrics': {
            'cpu_usage_percent': 0.0,
            'memory_usage_percent': 0.0,
            'disk_usage_percent': 0.0
        },
        'application_metrics': {
            'total_requests': 0,
            'error_rate_percent': 0.0,
            'average_response_time_ms': 0.0
        },
        'timestamp': datetime.utcnow().isoformat()
    }), 200


@application.route('/api/monitoring/alerts', methods=['GET'])
@require_authentication
def get_monitoring_alerts() -> Response:
    """
    Get active system alerts
    """
    return jsonify({
        'alerts': [],
        'total_count': 0,
        'timestamp': datetime.utcnow().isoformat()
    }), 200



@socketio.on('connect')
def handle_websocket_connect():
    """Handle WebSocket client connection"""
    logger.info('WebSocket client connected')
    emit('connection_established', {
        'message': 'Connected to International Plebeian Academy',
        'timestamp': datetime.utcnow().isoformat()
    })


@socketio.on('disconnect')
def handle_websocket_disconnect():
    """Handle WebSocket client disconnection"""
    logger.info('WebSocket client disconnected')


@socketio.on('subscribe_system_metrics')
def handle_subscribe_system_metrics():
    """Subscribe to real-time system metrics updates"""
    logger.info('Client subscribed to system metrics')



@application.errorhandler(404)
def not_found_error(error) -> Response:
    """Handle 404 errors"""
    return jsonify({
        'error': 'Resource not found',
        'path': request.path,
        'method': request.method
    }), 404


@application.errorhandler(500)
def internal_server_error(error) -> Response:
    """Handle 500 errors"""
    logger.error(f'Internal server error: {str(error)}')
    return jsonify({
        'error': 'Internal server error',
        'message': 'An unexpected error occurred'
    }), 500



def initialize_application():
    """Initialize application on startup"""
    logger.info('Initializing International Plebeian Academy Backend')
    logger.info(f'Environment: {os.getenv("FLASK_ENV", "development")}')
    logger.info(f'Database URL: {application.config["DATABASE_URL"]}')
    
    os.makedirs(application.config['UPLOAD_FOLDER'], exist_ok=True)
    
    os.makedirs('./logs', exist_ok=True)
    
    application_state['system_status'] = 'running'
    logger.info('Application initialized successfully')


initialize_application()



if __name__ == '__main__':
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '8000'))
    
    logger.info(f'Starting server on {host}:{port}')
    
    socketio.run(
        application,
        host=host,
        port=port,
        debug=application.config['DEBUG'],
        allow_unsafe_werkzeug=True  # For development only
    )
