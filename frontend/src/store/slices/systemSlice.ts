/**
 * International Plebeian Academy - System Management Redux Slice
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface SystemMetrics {
  cpu: number;
  memory: number;
  network: number;
  activeNodes: number;
  totalNodes: number;
}

interface SystemState {
  metrics: SystemMetrics | null;
  healthHistory: any[];
  loading: boolean;
  error: string | null;
}

const initialState: SystemState = {
  metrics: null,
  healthHistory: [],
  loading: false,
  error: null,
};

const systemSlice = createSlice({
  name: 'system',
  initialState,
  reducers: {
    fetchMetricsStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchMetricsSuccess(state, action: PayloadAction<SystemMetrics>) {
      state.metrics = action.payload;
      state.loading = false;
      state.error = null;
    },
    fetchMetricsFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    updateHealthHistory(state, action: PayloadAction<any>) {
      state.healthHistory.push(action.payload);
      if (state.healthHistory.length > 100) {
        state.healthHistory.shift();
      }
    },
    clearError(state) {
      state.error = null;
    },
  },
});

export const { 
  fetchMetricsStart, 
  fetchMetricsSuccess, 
  fetchMetricsFailure, 
  updateHealthHistory,
  clearError 
} = systemSlice.actions;

export default systemSlice.reducer;
