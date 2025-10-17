"""
International Plebeian Academy - Torrent Manager
BitTorrent-based file distribution system

Author: International Plebeian Academy Development Team
License: MIT
Version: 1.0.0
"""

import hashlib
import logging
from typing import Dict, List, Optional, Any
from datetime import datetime

logger = logging.getLogger(__name__)


class TorrentManager:
    """Manages torrent-based file distribution"""
    
    def __init__(self):
        """Initialize torrent manager"""
        self.active_torrents: Dict[str, Dict[str, Any]] = {}
        self.seeders: Dict[str, List[str]] = {}
        self.leechers: Dict[str, List[str]] = {}
        logger.info("Torrent manager initialized")
    
    def create_torrent(
        self,
        file_data: bytes,
        file_name: str,
        piece_length: int = 262144
    ) -> Dict[str, Any]:
        """Create torrent for file distribution"""
        info_hash = hashlib.sha256(file_data).hexdigest()
        
        torrent = {
            'info_hash': info_hash,
            'file_name': file_name,
            'file_size': len(file_data),
            'piece_length': piece_length,
            'created_at': datetime.utcnow().isoformat(),
            'seeders': 0,
            'leechers': 0
        }
        
        self.active_torrents[info_hash] = torrent
        self.seeders[info_hash] = []
        self.leechers[info_hash] = []
        
        logger.info(f"Torrent created: {file_name} ({info_hash})")
        return torrent
    
    def add_seeder(self, info_hash: str, peer_id: str) -> bool:
        """Add seeder to torrent"""
        if info_hash not in self.active_torrents:
            return False
        
        if peer_id not in self.seeders[info_hash]:
            self.seeders[info_hash].append(peer_id)
            self.active_torrents[info_hash]['seeders'] += 1
            logger.info(f"Seeder added to {info_hash}: {peer_id}")
        
        return True
    
    def get_torrent_status(self) -> Dict[str, Any]:
        """Get torrent system status"""
        return {
            'active_torrents': len(self.active_torrents),
            'total_seeders': sum(len(s) for s in self.seeders.values()),
            'total_leechers': sum(len(l) for l in self.leechers.values())
        }


__all__ = ['TorrentManager']
