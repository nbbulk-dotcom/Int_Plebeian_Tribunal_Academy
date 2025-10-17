/**
 * International Plebeian Academy - Bot Management Redux Slice
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import { createSlice, PayloadAction } from '@reduxjs/toolkit';

interface Bot {
  id: string;
  name: string;
  division: string;
  status: 'active' | 'inactive' | 'error';
  tasksCompleted: number;
  successRate: number;
}

interface BotState {
  bots: Bot[];
  selectedBot: Bot | null;
  loading: boolean;
  error: string | null;
}

const initialState: BotState = {
  bots: [],
  selectedBot: null,
  loading: false,
  error: null,
};

const botSlice = createSlice({
  name: 'bot',
  initialState,
  reducers: {
    fetchBotsStart(state) {
      state.loading = true;
      state.error = null;
    },
    fetchBotsSuccess(state, action: PayloadAction<Bot[]>) {
      state.bots = action.payload;
      state.loading = false;
      state.error = null;
    },
    fetchBotsFailure(state, action: PayloadAction<string>) {
      state.loading = false;
      state.error = action.payload;
    },
    selectBot(state, action: PayloadAction<Bot>) {
      state.selectedBot = action.payload;
    },
    updateBotStatus(state, action: PayloadAction<{ id: string; status: 'active' | 'inactive' | 'error' }>) {
      const bot = state.bots.find(b => b.id === action.payload.id);
      if (bot) {
        bot.status = action.payload.status;
      }
    },
    clearError(state) {
      state.error = null;
    },
  },
});

export const { 
  fetchBotsStart, 
  fetchBotsSuccess, 
  fetchBotsFailure, 
  selectBot,
  updateBotStatus,
  clearError 
} = botSlice.actions;

export default botSlice.reducer;
