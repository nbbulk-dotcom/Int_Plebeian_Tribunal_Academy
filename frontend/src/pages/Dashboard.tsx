/**
 * International Plebeian Academy - Dashboard Page
 * 
 * Main dashboard with system overview and metrics
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React, { useState, useEffect } from 'react';
import {
  Container,
  Grid,
  Paper,
  Typography,
  Box,
  Card,
  CardContent,
} from '@mui/material';
import apiService from '../services/api';
import LoadingSpinner from '../components/common/LoadingSpinner';

const Dashboard: React.FC = () => {
  const [loading, setLoading] = useState(true);
  const [systemStatus, setSystemStatus] = useState<any>(null);
  const [botStatus, setBotStatus] = useState<any>(null);

  useEffect(() => {
    const fetchDashboardData = async () => {
      try {
        const [statusData, botsData] = await Promise.all([
          apiService.getSystemStatus(),
          apiService.getBotStatus(),
        ]);
        setSystemStatus(statusData);
        setBotStatus(botsData);
      } catch (error) {
        console.error('Failed to fetch dashboard data:', error);
      } finally {
        setLoading(false);
      }
    };

    fetchDashboardData();
  }, []);

  if (loading) {
    return <LoadingSpinner fullScreen message="Loading dashboard..." />;
  }

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        System Dashboard
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                System Status
              </Typography>
              <Typography variant="h5">
                {systemStatus?.system_status || 'Running'}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                Connected Nodes
              </Typography>
              <Typography variant="h5">
                {systemStatus?.connected_nodes || 0}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                Active Bots
              </Typography>
              <Typography variant="h5">
                {botStatus?.active_bots || 0} / {botStatus?.total_bots || 35}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={3}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                Total Users
              </Typography>
              <Typography variant="h5">
                {systemStatus?.total_users || 0}
              </Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              System Overview
            </Typography>
            <Box sx={{ mt: 2 }}>
              <Typography variant="body2" paragraph>
                Welcome to the International Plebeian Academy dashboard. The system is currently operational with all core services running.
              </Typography>
              <Typography variant="body2" color="text.secondary">
                Phase 2 Implementation: Dashboard with real-time system metrics
              </Typography>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default Dashboard;
