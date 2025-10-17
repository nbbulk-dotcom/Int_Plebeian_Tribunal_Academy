"""
International Plebeian Academy - System Management Routes
@author International Plebeian Academy Development Team
@license MIT
@version 1.0.0
"""

from flask import Blueprint, request, jsonify
from backend.routes.auth import token_required
import psutil
import os

system_blueprint = Blueprint('system', __name__)

@system_blueprint.route('/api/system/health', methods=['GET'])
@token_required
def get_system_health(current_user):
    """
    Get system health metrics
    """
    try:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')
        network = psutil.net_io_counters()
        
        return jsonify({
            'cpu': {
                'percent': cpu_percent,
                'count': psutil.cpu_count()
            },
            'memory': {
                'total': memory.total,
                'available': memory.available,
                'percent': memory.percent
            },
            'disk': {
                'total': disk.total,
                'used': disk.used,
                'percent': disk.percent
            },
            'network': {
                'bytes_sent': network.bytes_sent,
                'bytes_recv': network.bytes_recv
            }
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@system_blueprint.route('/api/system/versions', methods=['GET'])
@token_required
def get_versions(current_user):
    """
    Get current and available versions
    """
    try:
        current_version = os.environ.get('APP_VERSION', '1.0.0')
        
        available_versions = [
            {
                'number': '1.1.0',
                'description': 'Enhanced security features and performance improvements',
                'releaseDate': '2025-11-01'
            },
            {
                'number': '1.2.0',
                'description': 'New AI-powered analytics and reporting',
                'releaseDate': '2025-12-01'
            }
        ]
        
        return jsonify({
            'current': current_version,
            'available': available_versions
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@system_blueprint.route('/api/system/upgrade', methods=['POST'])
@token_required
def upgrade_system(current_user):
    """
    Initiate system upgrade
    """
    try:
        data = request.get_json()
        version = data.get('version')
        
        if not version:
            return jsonify({'error': 'Version not specified'}), 400
        
        return jsonify({
            'message': f'Upgrade to version {version} initiated successfully',
            'status': 'in_progress'
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
