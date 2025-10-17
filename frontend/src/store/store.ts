/**
 * International Plebeian Academy - Redux Store Configuration
 * 
 * Central Redux store for state management across the application.
 * 
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import { configureStore } from '@reduxjs/toolkit';
import { TypedUseSelectorHook, useDispatch, useSelector } from 'react-redux';


const placeholderReducer = () => ({
  status: 'initialized',
  message: 'Reducer will be implemented in Phase 2',
});

/**
 * Configure and create the Redux store
 */
export const store = configureStore({
  reducer: {
    authentication: placeholderReducer,
    system: placeholderReducer,
    bots: placeholderReducer,
    blockchain: placeholderReducer,
    distribution: placeholderReducer,
    
  },
  middleware: (getDefaultMiddleware) =>
    getDefaultMiddleware({
      serializableCheck: {
        ignoredActions: ['persist/PERSIST', 'persist/REHYDRATE'],
      },
    }),
  devTools: import.meta.env.DEV,
});

export type RootState = ReturnType<typeof store.getState>;
export type ApplicationDispatch = typeof store.dispatch;

export const useApplicationDispatch: () => ApplicationDispatch = useDispatch;
export const useApplicationSelector: TypedUseSelectorHook<RootState> = useSelector;

export default store;
