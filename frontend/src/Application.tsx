/**
 * International Plebeian Academy - Main Application Component
 * 
 * Root component that handles routing and global layout.
 * This component orchestrates the entire frontend application structure.
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React, { useEffect, useState } from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import { Box, Container, CircularProgress, Typography } from '@mui/material';




/**
 * Placeholder component for routes not yet implemented
 */
const PlaceholderPage: React.FC<{ pageName: string }> = ({ pageName }) => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: '60vh',
          textAlign: 'center',
        }}
      >
        <Typography variant="h3" component="h1" gutterBottom>
          {pageName}
        </Typography>
        <Typography variant="body1" color="text.secondary" sx={{ mt: 2 }}>
          This page is currently under development.
        </Typography>
        <Typography variant="body2" color="text.secondary" sx={{ mt: 1 }}>
          Phase 1: Foundation implementation in progress
        </Typography>
      </Box>
    </Container>
  );
};

/**
 * Home page component
 */
const HomePage: React.FC = () => {
  return (
    <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          py: 8,
        }}
      >
        <Typography
          variant="h2"
          component="h1"
          gutterBottom
          sx={{
            background: 'linear-gradient(45deg, #2071a1 30%, #4a9fd8 90%)',
            WebkitBackgroundClip: 'text',
            WebkitTextFillColor: 'transparent',
            fontWeight: 700,
          }}
        >
          International Plebeian Academy
        </Typography>
        
        <Typography variant="h5" color="text.secondary" sx={{ mt: 2, mb: 4 }}>
          Revolutionary Holographic Distributed Platform
        </Typography>
        
        <Typography variant="body1" paragraph sx={{ maxWidth: 800, mb: 3 }}>
          Welcome to the International Plebeian Academy - a revolutionary platform
          for global peace advocacy combining state-of-the-art holographic distribution,
          blockchain governance, and AI-powered automation.
        </Typography>
        
        <Box
          sx={{
            display: 'grid',
            gridTemplateColumns: { xs: '1fr', md: 'repeat(3, 1fr)' },
            gap: 3,
            mt: 6,
            width: '100%',
          }}
        >
          <Box
            sx={{
              p: 3,
              backgroundColor: 'background.paper',
              borderRadius: 2,
              border: '1px solid rgba(255, 255, 255, 0.1)',
            }}
          >
            <Typography variant="h6" gutterBottom color="primary">
              Holographic Distribution
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Everywhere and nowhere at once - quantum-inspired data distribution
            </Typography>
          </Box>
          
          <Box
            sx={{
              p: 3,
              backgroundColor: 'background.paper',
              borderRadius: 2,
              border: '1px solid rgba(255, 255, 255, 0.1)',
            }}
          >
            <Typography variant="h6" gutterBottom color="primary">
              Blockchain Governance
            </Typography>
            <Typography variant="body2" color="text.secondary">
              TribalCoin-based democratic decision making with immutable records
            </Typography>
          </Box>
          
          <Box
            sx={{
              p: 3,
              backgroundColor: 'background.paper',
              borderRadius: 2,
              border: '1px solid rgba(255, 255, 255, 0.1)',
            }}
          >
            <Typography variant="h6" gutterBottom color="primary">
              35 AI Bots
            </Typography>
            <Typography variant="body2" color="text.secondary">
              Seven divisions with 5 specialized bots each handling automated tasks
            </Typography>
          </Box>
        </Box>
        
        <Box sx={{ mt: 6 }}>
          <Typography variant="body2" color="text.secondary">
            Phase 1: Foundation Implementation
          </Typography>
          <Typography variant="caption" color="text.secondary">
            Backend API: ✓ | Frontend Foundation: ✓ | Database: Pending | Full Features: Pending
          </Typography>
        </Box>
      </Box>
    </Container>
  );
};

/**
 * Main Application Component
 */
const Application: React.FC = () => {
  const [isLoading, setIsLoading] = useState(true);
  const [backendHealthy, setBackendHealthy] = useState(false);
  
  useEffect(() => {
    const checkBackend = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/health');
        if (response.ok) {
          setBackendHealthy(true);
          console.log('Backend connection successful');
        } else {
          setBackendHealthy(false);
          console.warn('Backend responded with non-200 status');
        }
      } catch (error) {
        setBackendHealthy(false);
        console.error('Backend connection failed:', error);
      } finally {
        setIsLoading(false);
      }
    };
    
    checkBackend();
  }, []);
  
  if (isLoading) {
    return (
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          justifyContent: 'center',
          minHeight: '100vh',
          backgroundColor: 'background.default',
        }}
      >
        <CircularProgress size={60} />
        <Typography variant="h6" sx={{ mt: 3 }}>
          Initializing Academy Platform...
        </Typography>
      </Box>
    );
  }
  
  const BackendStatusWarning = () => {
    if (backendHealthy) return null;
    
    return (
      <Box
        sx={{
          backgroundColor: 'error.dark',
          color: 'white',
          p: 1,
          textAlign: 'center',
        }}
      >
        <Typography variant="body2">
          ⚠️ Backend API not connected. Make sure the backend server is running on http://localhost:8000
        </Typography>
      </Box>
    );
  };
  
  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
      {/* Backend Status Warning */}
      <BackendStatusWarning />
      
      {/* Navigation Bar (will be implemented in Phase 2) */}
      {/* <Navbar /> */}
      
      {/* Main Content Area */}
      <Box component="main" sx={{ flexGrow: 1 }}>
        <Routes>
          {/* Home Page */}
          <Route path="/" element={<HomePage />} />
          
          {/* Authentication Routes */}
          <Route path="/login" element={<PlaceholderPage pageName="Biometric Login" />} />
          
          {/* Dashboard Routes */}
          <Route path="/dashboard" element={<PlaceholderPage pageName="Dashboard" />} />
          
          {/* System Management Routes */}
          <Route path="/system" element={<PlaceholderPage pageName="System Management" />} />
          
          {/* Bot Management Routes */}
          <Route path="/bots" element={<PlaceholderPage pageName="Bot Management" />} />
          <Route path="/bots/:divisionName" element={<PlaceholderPage pageName="Division Bots" />} />
          
          {/* Blockchain Routes */}
          <Route path="/blockchain" element={<PlaceholderPage pageName="Blockchain Status" />} />
          <Route path="/blockchain/tribal-coin" element={<PlaceholderPage pageName="TribalCoin" />} />
          <Route path="/blockchain/governance" element={<PlaceholderPage pageName="Governance" />} />
          
          {/* Distribution Network Routes */}
          <Route path="/distribution" element={<PlaceholderPage pageName="Distribution Network" />} />
          
          {/* Upgrade Management Routes */}
          <Route path="/upgrades" element={<PlaceholderPage pageName="Upgrade Manager" />} />
          
          {/* Ethics Foundation Routes */}
          <Route path="/ethics" element={<PlaceholderPage pageName="Ethics Foundation" />} />
          
          {/* Catch-all redirect to home */}
          <Route path="*" element={<Navigate to="/" replace />} />
        </Routes>
      </Box>
      
      {/* Footer */}
      <Box
        component="footer"
        sx={{
          py: 3,
          px: 2,
          mt: 'auto',
          backgroundColor: 'background.paper',
          borderTop: '1px solid rgba(255, 255, 255, 0.1)',
        }}
      >
        <Container maxWidth="lg">
          <Typography variant="body2" color="text.secondary" align="center">
            © 2025 International Plebeian Academy. All rights reserved.
          </Typography>
          <Typography variant="caption" color="text.secondary" align="center" display="block" sx={{ mt: 1 }}>
            Version 1.0.0 | Phase 1: Foundation
          </Typography>
        </Container>
      </Box>
    </Box>
  );
};

export default Application;
