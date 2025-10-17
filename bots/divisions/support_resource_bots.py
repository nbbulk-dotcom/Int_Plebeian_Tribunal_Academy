"""
International Plebeian Academy - Support & Resource Division Bots
5 specialized bots for resource management and member support

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

from typing import List, Dict, Any


def get_support_resource_bots() -> List[Dict[str, Any]]:
    """Get Support & Resource Division bot configurations"""
    
    return [
        {
            'bot_id': 'supp_bot_001',
            'bot_name': 'Resource Allocation Bot',
            'specialization': 'resource_management',
            'capabilities': [
                'resource_tracking',
                'allocation_optimization',
                'inventory_management',
                'utilization_analysis'
            ]
        },
        {
            'bot_id': 'supp_bot_002',
            'bot_name': 'Technical Support Bot',
            'specialization': 'technical_assistance',
            'capabilities': [
                'troubleshooting',
                'documentation_assistance',
                'system_guidance',
                'bug_reporting'
            ]
        },
        {
            'bot_id': 'supp_bot_003',
            'bot_name': 'Financial Aid Bot',
            'specialization': 'financial_support',
            'capabilities': [
                'grant_management',
                'funding_opportunities',
                'budget_assistance',
                'financial_planning'
            ]
        },
        {
            'bot_id': 'supp_bot_004',
            'bot_name': 'Legal Aid Bot',
            'specialization': 'legal_assistance',
            'capabilities': [
                'legal_information',
                'document_preparation',
                'rights_education',
                'referral_services'
            ]
        },
        {
            'bot_id': 'supp_bot_005',
            'bot_name': 'Emergency Response Bot',
            'specialization': 'crisis_management',
            'capabilities': [
                'emergency_coordination',
                'rapid_response',
                'resource_mobilization',
                'crisis_communication'
            ]
        }
    ]


__all__ = ['get_support_resource_bots']
