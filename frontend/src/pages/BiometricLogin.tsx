/**
 * International Plebeian Academy - Biometric Login Page
 * 
 * Multi-modal biometric authentication interface
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Container,
  Paper,
  Typography,
  Button,
  Box,
  Alert,
  Select,
  MenuItem,
  FormControl,
  InputLabel,
} from '@mui/material';
import FingerprintIcon from '@mui/icons-material/Fingerprint';
import apiService from '../services/api';

const BiometricLogin: React.FC = () => {
  const navigate = useNavigate();
  const [biometricType, setBiometricType] = useState<string>('fingerprint');
  const [isAuthenticating, setIsAuthenticating] = useState(false);
  const [error, setError] = useState<string>('');

  const handleBiometricLogin = async () => {
    setIsAuthenticating(true);
    setError('');

    try {
      const simulatedBiometricData = btoa(`simulated_${biometricType}_${Date.now()}`);

      const response = await apiService.authenticateBiometric({
        biometric_type: biometricType as any,
        biometric_data: simulatedBiometricData,
        device_id: 'web_browser',
      });

      if (response.success) {
        navigate('/dashboard');
      }
    } catch (err: any) {
      setError(err.response?.data?.error || 'Authentication failed');
    } finally {
      setIsAuthenticating(false);
    }
  };

  return (
    <Container maxWidth="sm" sx={{ mt: 8 }}>
      <Paper sx={{ p: 4 }}>
        <Box sx={{ textAlign: 'center', mb: 4 }}>
          <FingerprintIcon sx={{ fontSize: 80, color: 'primary.main', mb: 2 }} />
          <Typography variant="h4" gutterBottom>
            Biometric Login
          </Typography>
          <Typography variant="body2" color="text.secondary">
            International Plebeian Academy
          </Typography>
        </Box>

        {error && (
          <Alert severity="error" sx={{ mb: 3 }}>
            {error}
          </Alert>
        )}

        <FormControl fullWidth sx={{ mb: 3 }}>
          <InputLabel>Biometric Type</InputLabel>
          <Select
            value={biometricType}
            label="Biometric Type"
            onChange={(e) => setBiometricType(e.target.value)}
          >
            <MenuItem value="fingerprint">Fingerprint</MenuItem>
            <MenuItem value="face">Face Recognition</MenuItem>
            <MenuItem value="iris">Iris Scan</MenuItem>
            <MenuItem value="voice">Voice Recognition</MenuItem>
            <MenuItem value="behavioral">Behavioral</MenuItem>
          </Select>
        </FormControl>

        <Button
          fullWidth
          variant="contained"
          size="large"
          onClick={handleBiometricLogin}
          disabled={isAuthenticating}
        >
          {isAuthenticating ? 'Authenticating...' : 'Authenticate'}
        </Button>

        <Typography variant="caption" color="text.secondary" sx={{ mt: 2, display: 'block', textAlign: 'center' }}>
          Phase 2: Simulated biometric authentication
        </Typography>
      </Paper>
    </Container>
  );
};

export default BiometricLogin;
