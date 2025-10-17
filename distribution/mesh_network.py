"""
International Plebeian Academy - Mesh Network
Decentralized mesh networking for peer-to-peer communication

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

import logging
from typing import Dict, List, Optional, Any, Set
from datetime import datetime

logger = logging.getLogger(__name__)


class MeshNetwork:
    """Manages mesh network topology and routing"""
    
    def __init__(self):
        """Initialize mesh network"""
        self.nodes: Dict[str, Dict[str, Any]] = {}
        self.connections: Dict[str, Set[str]] = {}
        self.routing_table: Dict[str, Dict[str, str]] = {}
        logger.info("Mesh network initialized")
    
    def add_node(self, node_id: str, node_info: Dict[str, Any]) -> bool:
        """Add node to mesh network"""
        if node_id in self.nodes:
            return False
        
        self.nodes[node_id] = {
            **node_info,
            'joined_at': datetime.utcnow().isoformat()
        }
        self.connections[node_id] = set()
        
        logger.info(f"Node added to mesh: {node_id}")
        return True
    
    def connect_nodes(self, node_a: str, node_b: str) -> bool:
        """Create connection between nodes"""
        if node_a not in self.nodes or node_b not in self.nodes:
            return False
        
        self.connections[node_a].add(node_b)
        self.connections[node_b].add(node_a)
        
        self._update_routing_table()
        logger.info(f"Nodes connected: {node_a} <-> {node_b}")
        return True
    
    def _update_routing_table(self) -> None:
        """Update routing table using shortest path"""
        for source in self.nodes:
            self.routing_table[source] = {}
            visited = {source}
            queue = [(source, source, 0)]
            
            while queue:
                current, next_hop, distance = queue.pop(0)
                
                for neighbor in self.connections.get(current, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        self.routing_table[source][neighbor] = next_hop if next_hop != source else neighbor
                        queue.append((neighbor, next_hop if next_hop != source else neighbor, distance + 1))
    
    def get_route(self, source: str, destination: str) -> Optional[str]:
        """Get next hop for routing"""
        return self.routing_table.get(source, {}).get(destination)
    
    def get_network_status(self) -> Dict[str, Any]:
        """Get mesh network status"""
        total_connections = sum(len(c) for c in self.connections.values()) // 2
        
        return {
            'total_nodes': len(self.nodes),
            'total_connections': total_connections,
            'average_connections': total_connections / len(self.nodes) if self.nodes else 0
        }


__all__ = ['MeshNetwork']
