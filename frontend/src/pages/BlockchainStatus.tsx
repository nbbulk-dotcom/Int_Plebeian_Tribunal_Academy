/**
 * International Plebeian Academy - Blockchain Status Page
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
  Card,
  CardContent,
  List,
  ListItem,
  ListItemText,
} from '@mui/material';
import apiService from '../services/api';

const BlockchainStatus: React.FC = () => {
  const [proposals, setProposals] = useState<any[]>([]);

  useEffect(() => {
    const fetchProposals = async () => {
      try {
        const data = await apiService.getGovernanceProposals();
        setProposals(data.proposals || []);
      } catch (error) {
        console.error('Failed to fetch proposals:', error);
      }
    };

    fetchProposals();
  }, []);

  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Typography variant="h4" gutterBottom>
        Blockchain & TribalCoin
      </Typography>

      <Grid container spacing={3}>
        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                Total Supply
              </Typography>
              <Typography variant="h5">1B TRIBAL</Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                Circulating
              </Typography>
              <Typography variant="h5">100M TRIBAL</Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12} md={4}>
          <Card>
            <CardContent>
              <Typography color="text.secondary" gutterBottom>
                Active Proposals
              </Typography>
              <Typography variant="h5">{proposals.length}</Typography>
            </CardContent>
          </Card>
        </Grid>

        <Grid item xs={12}>
          <Paper sx={{ p: 3 }}>
            <Typography variant="h6" gutterBottom>
              Governance Proposals
            </Typography>
            <List>
              {proposals.map((proposal, index) => (
                <ListItem key={index}>
                  <ListItemText
                    primary={proposal.title || 'Proposal'}
                    secondary={proposal.description}
                  />
                </ListItem>
              ))}
              {proposals.length === 0 && (
                <Typography color="text.secondary">No active proposals</Typography>
              )}
            </List>
          </Paper>
        </Grid>
      </Grid>
    </Container>
  );
};

export default BlockchainStatus;
