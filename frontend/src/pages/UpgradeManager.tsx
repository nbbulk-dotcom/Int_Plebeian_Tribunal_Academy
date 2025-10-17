/**
 * International Plebeian Academy - Upgrade Manager Page
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React, { useEffect, useState } from 'react';
import apiService from '../services/api';

const UpgradeManager: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [currentVersion, setCurrentVersion] = useState('');
  const [availableVersions, setAvailableVersions] = useState<any[]>([]);
  const [upgradeStatus, setUpgradeStatus] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchVersionInfo();
  }, []);

  const fetchVersionInfo = async () => {
    try {
      setLoading(true);
      const response = await apiService.get('/api/system/versions');
      setCurrentVersion(response.data.current || '1.0.0');
      setAvailableVersions(response.data.available || []);
      setError(null);
    } catch (err: any) {
      setError(err.message || 'Failed to fetch version info');
    } finally {
      setLoading(false);
    }
  };

  const handleUpgrade = async (version: string) => {
    try {
      setUpgradeStatus('Initiating upgrade...');
      const response = await apiService.post('/api/system/upgrade', { version });
      setUpgradeStatus(response.data.message || 'Upgrade completed successfully');
      fetchVersionInfo();
    } catch (err: any) {
      setError(err.message || 'Upgrade failed');
      setUpgradeStatus(null);
    }
  };

  if (loading) {
    return <div className="loading">Loading upgrade manager...</div>;
  }

  if (error) {
    return <div className="error">Error: {error}</div>;
  }

  return (
    <div className="upgrade-manager-page">
      <h1>Upgrade Manager</h1>
      
      <div className="current-version-card">
        <h2>Current Version</h2>
        <p className="version-number">{currentVersion}</p>
      </div>

      {upgradeStatus && (
        <div className="upgrade-status">
          <p>{upgradeStatus}</p>
        </div>
      )}

      <div className="available-versions">
        <h2>Available Versions</h2>
        {availableVersions.length === 0 ? (
          <p>No updates available. You are running the latest version.</p>
        ) : (
          <div className="versions-list">
            {availableVersions.map(version => (
              <div key={version.number} className="version-card">
                <h3>Version {version.number}</h3>
                <p>{version.description}</p>
                <p className="version-date">Released: {version.releaseDate}</p>
                <button 
                  onClick={() => handleUpgrade(version.number)}
                  className="upgrade-button"
                >
                  Upgrade to {version.number}
                </button>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  );
};

export default UpgradeManager;
