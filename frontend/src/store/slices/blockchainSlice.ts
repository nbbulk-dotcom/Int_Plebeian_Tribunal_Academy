/**
 * International Plebeian Academy - Blockchain Redux Slice
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface BlockchainMetrics {
  blockHeight: number;
  transactionCount: number;
  gasPrice: string;
  networkStatus: 'connected' | 'disconnected' | 'syncing';
}

interface BlockchainState {
  metrics: BlockchainMetrics | null;
  transactions: any[];
  loading: boolean;
  error: string | null;
}

const initialState: BlockchainState = {
  metrics: null,
  transactions: [],
  loading: false,
  error: null,
};

const blockchainSlice = createSlice({
  name: 'blockchain',
  initialState,
  reducers: {
    fetchMetricsStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchMetricsSuccess(state, action: PayloadAction<BlockchainMetrics>) {
      state.metrics = action.payload;
      state.loading = false;
      state.error = null;
    },
    fetchMetricsFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    addTransaction(state, action: PayloadAction<any>) {
      state.transactions.unshift(action.payload);
      if (state.transactions.length > 50) {
        state.transactions.pop();
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
  addTransaction,
  clearError 
} = blockchainSlice.actions;

export default blockchainSlice.reducer;
