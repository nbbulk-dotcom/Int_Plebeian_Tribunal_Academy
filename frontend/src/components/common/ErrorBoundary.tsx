/**
 * International Plebeian Academy - Error Boundary Component
 * 
 * React Error Boundary for graceful error handling
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT  
 * @version 1.0.0
 */

import React, { Component, ErrorInfo, ReactNode } from 'react';
import { Box, Typography, Button, Paper } from '@mui/material';

interface ErrorBoundaryProps {
  children: ReactNode;
}

interface ErrorBoundaryState {
  hasError: boolean;
  error: Error | null;
  errorInfo: ErrorInfo | null;
}

class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props);
    this.state = {
      hasError: false,
      error: null,
      errorInfo: null,
    };
  }

  static getDerivedStateFromError(error: Error): Partial<ErrorBoundaryState> {
    return { hasError: true };
  }

  componentDidCatch(error: Error, errorInfo: ErrorInfo): void {
    console.error('Error caught by ErrorBoundary:', error, errorInfo);
    this.setState({
      error,
      errorInfo,
    });
  }

  handleReset = (): void => {
    this.setState({
      hasError: false,
      error: null,
      errorInfo: null,
    });
  };

  render(): ReactNode {
    if (this.state.hasError) {
      return (
        <Box
          sx={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            minHeight: '100vh',
            p: 3,
          }}
        >
          <Paper
            sx={{
              p: 4,
              maxWidth: 600,
              textAlign: 'center',
            }}
          >
            <Typography variant="h4" gutterBottom color="error">
              Something went wrong
            </Typography>
            <Typography variant="body1" paragraph color="text.secondary">
              We encountered an unexpected error. Please try refreshing the page.
            </Typography>
            {this.state.error && (
              <Typography variant="body2" sx={{ mt: 2, fontFamily: 'monospace' }}>
                {this.state.error.toString()}
              </Typography>
            )}
            <Box sx={{ mt: 3, display: 'flex', gap: 2, justifyContent: 'center' }}>
              <Button variant="contained" onClick={this.handleReset}>
                Try Again
              </Button>
              <Button variant="outlined" onClick={() => window.location.reload()}>
                Refresh Page
              </Button>
            </Box>
          </Paper>
        </Box>
      );
    }

    return this.props.children;
  }
}

export default ErrorBoundary;
