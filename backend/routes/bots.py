"""
International Plebeian Academy - Bot Management Routes
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

from flask import Blueprint, request, jsonify
from backend.routes.auth import token_required
from backend.services.bot_coordinator import BotCoordinator

bots_blueprint = Blueprint('bots', __name__)
bot_coordinator = BotCoordinator()

@bots_blueprint.route('/api/bots', methods=['GET'])
@token_required
def get_bots(current_user):
    """
    Get all bots across all divisions
    """
    try:
        bots = bot_coordinator.get_all_bots()
        return jsonify({'bots': bots}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bots_blueprint.route('/api/bots/<bot_id>', methods=['GET'])
@token_required
def get_bot(current_user, bot_id):
    """
    Get specific bot details
    """
    try:
        bot = bot_coordinator.get_bot(bot_id)
        if not bot:
            return jsonify({'error': 'Bot not found'}), 404
        return jsonify(bot), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bots_blueprint.route('/api/bots/<bot_id>/status', methods=['PUT'])
@token_required
def update_bot_status(current_user, bot_id):
    """
    Update bot status
    """
    try:
        data = request.get_json()
        status = data.get('status')
        
        if status not in ['active', 'inactive', 'error']:
            return jsonify({'error': 'Invalid status'}), 400
        
        result = bot_coordinator.update_bot_status(bot_id, status)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@bots_blueprint.route('/api/bots/division/<division_name>', methods=['GET'])
@token_required
def get_division_bots(current_user, division_name):
    """
    Get all bots for a specific division
    """
    try:
        bots = bot_coordinator.get_division_bots(division_name)
        return jsonify({'bots': bots}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
