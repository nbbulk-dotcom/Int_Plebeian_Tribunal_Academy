/**
 * International Plebeian Academy - Bot Management Page
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
  List,
  ListItem,
  ListItemText,
  Chip,
} from '@mui/material';
import apiService from '../services/api';

const BotManagement: React.FC = () => {
  const [botStatus, setBotStatus] = useState<any>(null);

  useEffect(() => {
    const fetchBotStatus = async () => {
      try {
        const data = await apiService.getBotStatus();
        setBotStatus(data);
      } catch (error) {
        console.error('Failed to fetch bot status:', error);
      }
    };

    fetchBotStatus();
  }, []);

  const divisions = [
    'Communications',
    'Human Development',
    'Support & Resource',
    'Action & Project',
    'Integrity & Quality',
    'Membership & Voice',
    'Strategic Direction',
  ];

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Bot Management
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={6}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Bot Network Status
            </Typography>
            <Typography>Total Bots: {botStatus?.total_bots || 35}</Typography>
            <Typography>Active: {botStatus?.active_bots || 0}</Typography>
          </Paper>
        </Grid>

        <Grid item xs={12}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Divisions (5 bots each)
            </Typography>
            <List>
              {divisions.map((division) => (
                <ListItem key={division}>
                  <ListItemText primary={division} />
                  <Chip label="Active" color="success" size="small" />
                </ListItem>
              ))}
            </List>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default BotManagement;
