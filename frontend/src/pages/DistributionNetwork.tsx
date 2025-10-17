/**
 * International Plebeian Academy - Distribution Network Management Page
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import apiService from '../services/api';

const DistributionNetwork: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [nodes, setNodes] = useState<any[]>([]);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchNodes();
  }, []);

  const fetchNodes = async () => {
    try {
      setLoading(true);
      const response = await apiService.get('/api/distribution/nodes');
      setNodes(response.data.nodes || []);
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch nodes');
    } finally {
      setLoading(false);
    }
  };

  if (loading) {
    return <div className="loading">Loading distribution network...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="distribution-network-page">
      <h1>Distribution Network</h1>
      
      <div className="network-summary">
        <div className="stat-card">
          <h3>Total Nodes</h3>
          <p className="stat-value">{nodes.length}</p>
        </div>
        <div className="stat-card">
          <h3>Active Nodes</h3>
          <p className="stat-value">{nodes.filter(n => n.status === 'online').length}</p>
        </div>
        <div className="stat-card">
          <h3>Syncing Nodes</h3>
          <p className="stat-value">{nodes.filter(n => n.status === 'syncing').length}</p>
        </div>
      </div>

      <div className="nodes-list">
        <h2>Network Nodes</h2>
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Location</th>
              <th>Status</th>
              <th>Version</th>
              <th>Peers</th>
            </tr>
          </thead>
          <tbody>
            {nodes.map(node => (
              <tr key={node.id}>
                <td>{node.id}</td>
                <td>{node.location}</td>
                <td>
                  <span className={`status-badge status-${node.status}`}>
                    {node.status}
                  </span>
                </td>
                <td>{node.version}</td>
                <td>{node.peers}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default DistributionNetwork;
