/**
 * International Plebeian Academy - System Management Page
 * 
 * System configuration and monitoring
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
  Button,
  TextField,
  Box,
} from '@mui/material';
import apiService from '../services/api';

const SystemManagement: React.FC = () => {
  const [config, setConfig] = useState<any>(null);
  const [metrics, setMetrics] = useState<any>(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [configData, metricsData] = await Promise.all([
          apiService.getSystemConfiguration(),
          apiService.getSystemMetrics(),
        ]);
        setConfig(configData);
        setMetrics(metricsData);
      } catch (error) {
        console.error('Failed to fetch system data:', error);
      }
    };

    fetchData();
  }, []);

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        System Management
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              System Configuration
            </Typography>
            <TextField
              fullWidth
              label="System Name"
              value="International Plebeian Academy"
              margin="normal"
            />
            <TextField
              fullWidth
              label="Network Mode"
              value="Distributed"
              margin="normal"
            />
            <Button variant="contained" sx={{ mt: 2 }}>
              Update Configuration
            </Button>
          </Paper>
        </Grid>

        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              System Metrics
            </Typography>
            <Box sx={{ mt: 2 }}>
              <Typography>CPU Usage: {metrics?.cpu_usage || 0}%</Typography>
              <Typography>Memory Usage: {metrics?.memory_usage || 0}%</Typography>
              <Typography>Network: {metrics?.network_status || 'Active'}</Typography>
            </Box>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default SystemManagement;
