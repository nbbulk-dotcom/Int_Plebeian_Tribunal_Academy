"""
International Plebeian Academy - Blockchain Routes
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

from flask import Blueprint, request, jsonify
from backend.routes.auth import token_required
from backend.services.blockchain_service import BlockchainService

blockchain_blueprint = Blueprint('blockchain', __name__)
blockchain_service = BlockchainService()

@blockchain_blueprint.route('/api/blockchain/status', methods=['GET'])
@token_required
def get_blockchain_status(current_user):
    """
    Get blockchain network status
    """
    try:
        status = blockchain_service.get_network_status()
        return jsonify(status), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blockchain_blueprint.route('/api/blockchain/transactions', methods=['GET'])
@token_required
def get_transactions(current_user):
    """
    Get recent blockchain transactions
    """
    try:
        limit = request.args.get('limit', 50, type=int)
        transactions = blockchain_service.get_recent_transactions(limit)
        return jsonify({'transactions': transactions}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blockchain_blueprint.route('/api/blockchain/verify', methods=['POST'])
@token_required
def verify_file(current_user):
    """
    Verify file integrity using blockchain
    """
    try:
        data = request.get_json()
        file_hash = data.get('file_hash')
        
        if not file_hash:
            return jsonify({'error': 'File hash required'}), 400
        
        verification = blockchain_service.verify_file(file_hash)
        return jsonify(verification), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@blockchain_blueprint.route('/api/blockchain/register', methods=['POST'])
@token_required
def register_file(current_user):
    """
    Register file hash on blockchain
    """
    try:
        data = request.get_json()
        file_hash = data.get('file_hash')
        metadata = data.get('metadata', {})
        
        if not file_hash:
            return jsonify({'error': 'File hash required'}), 400
        
        result = blockchain_service.register_file(file_hash, metadata)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
