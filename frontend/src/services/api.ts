/**
 * International Plebeian Academy - API Service
 * 
 * Centralized API client for backend communication.
 * Handles all HTTP requests to the Flask backend API.
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import axios, { AxiosInstance, AxiosError, AxiosResponse } from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';
const API_TIMEOUT = 30000; // 30 seconds

export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface BiometricEnrollmentRequest {
  user_id: string;
  biometric_type: 'fingerprint' | 'iris' | 'voice' | 'face' | 'behavioral';
  biometric_data: string;
  biometric_metadata?: {
    device?: string;
    quality_score?: number;
    capture_timestamp?: string;
  };
}

export interface BiometricAuthenticationRequest {
  biometric_type: 'fingerprint' | 'iris' | 'voice' | 'face' | 'behavioral';
  biometric_data: string;
  device_id?: string;
}

export interface AuthenticationResponse {
  success: boolean;
  user_id: string;
  username: string;
  access_token: string;
  refresh_token: string;
  token_type: string;
  expires_in: number;
  biometric_type?: string;
  authentication_score?: number;
  authenticated_at: string;
}

/**
 * API Service Class
 */
class ApiService {
  private client: AxiosInstance;
  private accessToken: string | null = null;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: API_TIMEOUT,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.client.interceptors.request.use(
      (config) => {
        if (this.accessToken) {
          config.headers.Authorization = `Bearer ${this.accessToken}`;
        }
        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    this.client.interceptors.response.use(
      (response) => response,
      async (error: AxiosError) => {
        if (error.response?.status === 401) {
          await this.handleTokenExpiration();
        }
        return Promise.reject(error);
      }
    );
  }

  /**
   * Set access token for authenticated requests
   */
  setAccessToken(token: string): void {
    this.accessToken = token;
    localStorage.setItem('access_token', token);
  }

  /**
   * Clear access token
   */
  clearAccessToken(): void {
    this.accessToken = null;
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
  }

  /**
   * Handle token expiration by attempting refresh
   */
  private async handleTokenExpiration(): Promise<void> {
    const refreshToken = localStorage.getItem('refresh_token');
    if (refreshToken) {
      try {
        const response = await this.refreshToken(refreshToken);
        this.setAccessToken(response.access_token);
      } catch (error) {
        this.clearAccessToken();
        window.location.href = '/login';
      }
    }
  }


  async healthCheck(): Promise<any> {
    const response = await this.client.get('/api/health');
    return response.data;
  }

  async getSystemStatus(): Promise<any> {
    const response = await this.client.get('/api/status');
    return response.data;
  }


  async enrollBiometric(data: BiometricEnrollmentRequest): Promise<any> {
    const response = await this.client.post('/api/authentication/biometric/enroll', data);
    return response.data;
  }

  async authenticateBiometric(data: BiometricAuthenticationRequest): Promise<AuthenticationResponse> {
    const response = await this.client.post('/api/authentication/biometric/authenticate', data);
    const authData = response.data;
    
    if (authData.access_token) {
      this.setAccessToken(authData.access_token);
      localStorage.setItem('refresh_token', authData.refresh_token);
    }
    
    return authData;
  }

  async refreshToken(refreshToken: string): Promise<any> {
    const response = await this.client.post('/api/authentication/token/refresh', {
      refresh_token: refreshToken,
    });
    return response.data;
  }

  async logout(): Promise<void> {
    try {
      await this.client.post('/api/authentication/logout');
    } finally {
      this.clearAccessToken();
    }
  }


  async getSystemMetrics(): Promise<any> {
    const response = await this.client.get('/api/system/metrics');
    return response.data;
  }

  async getSystemConfiguration(): Promise<any> {
    const response = await this.client.get('/api/system/configuration');
    return response.data;
  }

  async updateSystemConfiguration(config: any): Promise<any> {
    const response = await this.client.put('/api/system/configuration', config);
    return response.data;
  }


  async getBotStatus(): Promise<any> {
    const response = await this.client.get('/api/bots/status');
    return response.data;
  }

  async getDivisionBots(divisionName: string): Promise<any> {
    const response = await this.client.get(`/api/bots/division/${divisionName}`);
    return response.data;
  }

  async assignBotTask(task: {
    task_type: string;
    task_description: string;
    priority?: 'low' | 'medium' | 'high';
    deadline?: string;
  }): Promise<any> {
    const response = await this.client.post('/api/bots/assign-task', task);
    return response.data;
  }

  async getBotPerformance(): Promise<any> {
    const response = await this.client.get('/api/bots/performance');
    return response.data;
  }


  async getTribalCoinBalance(ethereumAddress: string): Promise<any> {
    const response = await this.client.get(`/api/tribal-coin/balance/${ethereumAddress}`);
    return response.data;
  }

  async transferTribalCoin(data: {
    to_address: string;
    amount: string;
    memo?: string;
  }): Promise<any> {
    const response = await this.client.post('/api/tribal-coin/transfer', data);
    return response.data;
  }

  async getGovernanceProposals(): Promise<any> {
    const response = await this.client.get('/api/tribal-coin/governance/proposals');
    return response.data;
  }

  async createGovernanceProposal(data: {
    title: string;
    description: string;
  }): Promise<any> {
    const response = await this.client.post('/api/tribal-coin/governance/proposals', data);
    return response.data;
  }

  async voteOnProposal(data: {
    proposal_id: string;
    vote: 'for' | 'against' | 'abstain';
  }): Promise<any> {
    const response = await this.client.post('/api/tribal-coin/governance/vote', data);
    return response.data;
  }


  async uploadFileForVerification(file: File): Promise<any> {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await this.client.post('/api/verification/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  }

  async verifyFile(fileHash: string): Promise<any> {
    const response = await this.client.get(`/api/verification/verify/${fileHash}`);
    return response.data;
  }

  async getVerificationHistory(): Promise<any> {
    const response = await this.client.get('/api/verification/history');
    return response.data;
  }


  async getDistributionNodes(): Promise<any> {
    const response = await this.client.get('/api/distribution/nodes');
    return response.data;
  }

  async uploadToDistributionNetwork(file: File): Promise<any> {
    const formData = new FormData();
    formData.append('file', file);
    
    const response = await this.client.post('/api/distribution/upload', formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    });
    return response.data;
  }

  async downloadFromDistributionNetwork(fileId: string): Promise<Blob> {
    const response = await this.client.get(`/api/distribution/download/${fileId}`, {
      responseType: 'blob',
    });
    return response.data;
  }

  async replicateFile(data: {
    file_id: string;
    target_nodes?: string[];
  }): Promise<any> {
    const response = await this.client.post('/api/distribution/replicate', data);
    return response.data;
  }


  async getAvailableUpgrades(): Promise<any> {
    const response = await this.client.get('/api/upgrades/available');
    return response.data;
  }

  async initiateUpgrade(data: {
    upgrade_id: string;
    schedule_time?: string;
  }): Promise<any> {
    const response = await this.client.post('/api/upgrades/initiate', data);
    return response.data;
  }

  async getUpgradeStatus(upgradeId: string): Promise<any> {
    const response = await this.client.get(`/api/upgrades/status/${upgradeId}`);
    return response.data;
  }


  async createQuantumSession(): Promise<any> {
    const response = await this.client.post('/api/quantum/create-session');
    return response.data;
  }

  async exchangeQuantumKeys(data: {
    session_id: string;
    public_key: string;
  }): Promise<any> {
    const response = await this.client.post('/api/quantum/exchange-keys', data);
    return response.data;
  }

  async quantumEncrypt(data: {
    session_id: string;
    plaintext: string;
  }): Promise<any> {
    const response = await this.client.post('/api/quantum/encrypt', data);
    return response.data;
  }

  async quantumDecrypt(data: {
    session_id: string;
    ciphertext: string;
  }): Promise<any> {
    const response = await this.client.post('/api/quantum/decrypt', data);
    return response.data;
  }


  async getMonitoringMetrics(): Promise<any> {
    const response = await this.client.get('/api/monitoring/metrics');
    return response.data;
  }

  async getMonitoringAlerts(): Promise<any> {
    const response = await this.client.get('/api/monitoring/alerts');
    return response.data;
  }
}

const apiService = new ApiService();

const storedToken = localStorage.getItem('access_token');
if (storedToken) {
  apiService.setAccessToken(storedToken);
}

export default apiService;
