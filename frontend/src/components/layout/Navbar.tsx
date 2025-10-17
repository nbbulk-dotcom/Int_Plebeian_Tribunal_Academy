/**
 * International Plebeian Academy - Navigation Bar Component
 * 
 * Main navigation component with biometric authentication status
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import React, { useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import {
  AppBar,
  Toolbar,
  Typography,
  Button,
  IconButton,
  Menu,
  MenuItem,
  Box,
  Chip,
} from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import AccountCircleIcon from '@mui/icons-material/AccountCircle';
import FingerprintIcon from '@mui/icons-material/Fingerprint';

const Navbar: React.FC = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
  
  const isAuthenticated = localStorage.getItem('access_token') !== null;

  const handleMenuOpen = (event: React.MouseEvent<HTMLElement>) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    navigate('/login');
    handleMenuClose();
  };

  const navItems = [
    { label: 'Dashboard', path: '/dashboard' },
    { label: 'System', path: '/system' },
    { label: 'Bots', path: '/bots' },
    { label: 'Blockchain', path: '/blockchain' },
    { label: 'Distribution', path: '/distribution' },
  ];

  return (
    <AppBar position="sticky">
      <Toolbar>
        <IconButton
          edge="start"
          color="inherit"
          aria-label="menu"
          onClick={handleMenuOpen}
          sx={{ mr: 2 }}
        >
          <MenuIcon />
        </IconButton>
        
        <Typography
          variant="h6"
          component="div"
          sx={{ flexGrow: 1, cursor: 'pointer' }}
          onClick={() => navigate('/')}
        >
          International Plebeian Academy
        </Typography>

        {isAuthenticated && (
          <Chip
            icon={<FingerprintIcon />}
            label="Authenticated"
            color="success"
            size="small"
            sx={{ mr: 2 }}
          />
        )}

        {isAuthenticated ? (
          <IconButton color="inherit" onClick={handleMenuOpen}>
            <AccountCircleIcon />
          </IconButton>
        ) : (
          <Button color="inherit" onClick={() => navigate('/login')}>
            Login
          </Button>
        )}

        <Menu
          anchorEl={anchorEl}
          open={Boolean(anchorEl)}
          onClose={handleMenuClose}
        >
          {navItems.map((item) => (
            <MenuItem
              key={item.path}
              onClick={() => {
                navigate(item.path);
                handleMenuClose();
              }}
              selected={location.pathname === item.path}
            >
              {item.label}
            </MenuItem>
          ))}
          {isAuthenticated && [
            <MenuItem key="divider-1" divider />,
            <MenuItem key="logout" onClick={handleLogout}>
              Logout
            </MenuItem>
          ]}
        </Menu>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar;
