/**
 * International Plebeian Academy - Distribution Network Redux Slice
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Node {
  id: string;
  location: string;
  status: 'online' | 'offline' | 'syncing';
  version: string;
  peers: number;
}

interface DistributionState {
  nodes: Node[];
  totalNodes: number;
  activeNodes: number;
  loading: boolean;
  error: string | null;
}

const initialState: DistributionState = {
  nodes: [],
  totalNodes: 0,
  activeNodes: 0,
  loading: false,
  error: null,
};

const distributionSlice = createSlice({
  name: 'distribution',
  initialState,
  reducers: {
    fetchNodesStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchNodesSuccess(state, action: PayloadAction<{ nodes: Node[]; total: number; active: number }>) {
      state.nodes = action.payload.nodes;
      state.totalNodes = action.payload.total;
      state.activeNodes = action.payload.active;
      state.loading = false;
      state.error = null;
    },
    fetchNodesFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    updateNodeStatus(state, action: PayloadAction<{ id: string; status: 'online' | 'offline' | 'syncing' }>) {
      const node = state.nodes.find(n => n.id === action.payload.id);
      if (node) {
        node.status = action.payload.status;
      }
    },
    clearError(state) {
      state.error = null;
    },
  },
});

export const { 
  fetchNodesStart, 
  fetchNodesSuccess, 
  fetchNodesFailure, 
  updateNodeStatus,
  clearError 
} = distributionSlice.actions;

export default distributionSlice.reducer;
