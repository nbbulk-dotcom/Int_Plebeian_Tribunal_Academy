"""
International Plebeian Academy - Strategic Direction Division Bots
5 specialized bots for strategic planning and decision support

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

from typing import List, Dict, Any


def get_strategic_direction_bots() -> List[Dict[str, Any]]:
    """Get Strategic Direction Division bot configurations"""
    
    return [
        {
            'bot_id': 'strat_bot_001',
            'bot_name': 'Strategic Planning Bot',
            'specialization': 'long_term_planning',
            'capabilities': [
                'goal_setting',
                'strategic_analysis',
                'roadmap_development',
                'vision_articulation'
            ]
        },
        {
            'bot_id': 'strat_bot_002',
            'bot_name': 'Policy Development Bot',
            'specialization': 'policy_formulation',
            'capabilities': [
                'policy_research',
                'framework_design',
                'stakeholder_consultation',
                'implementation_planning'
            ]
        },
        {
            'bot_id': 'strat_bot_003',
            'bot_name': 'Intelligence Analysis Bot',
            'specialization': 'data_intelligence',
            'capabilities': [
                'trend_analysis',
                'predictive_modeling',
                'competitive_intelligence',
                'scenario_planning'
            ]
        },
        {
            'bot_id': 'strat_bot_004',
            'bot_name': 'Innovation Management Bot',
            'specialization': 'innovation_development',
            'capabilities': [
                'innovation_scouting',
                'idea_evaluation',
                'pilot_coordination',
                'scaling_strategy'
            ]
        },
        {
            'bot_id': 'strat_bot_005',
            'bot_name': 'Decision Support Bot',
            'specialization': 'decision_assistance',
            'capabilities': [
                'option_analysis',
                'recommendation_generation',
                'consensus_building',
                'decision_documentation'
            ]
        }
    ]


__all__ = ['get_strategic_direction_bots']
