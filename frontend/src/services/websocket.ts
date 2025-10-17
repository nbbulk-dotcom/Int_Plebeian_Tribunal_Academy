/**
 * International Plebeian Academy - WebSocket Service
 * Real-time communication service
 * @author International Plebeian Academy Development Team
 * @license MIT
 * @version 1.0.0
 */

import { io, Socket } from 'socket.io-client';

const WEBSOCKET_URL = import.meta.env.VITE_WS_URL || 'ws://localhost:8000';

class WebSocketService {
  private socket: Socket | null = null;
  private reconnectAttempts = 0;
  private maxReconnectAttempts = 5;

  connect(): void {
    this.socket = io(WEBSOCKET_URL, {
      transports: ['websocket'],
      autoConnect: true,
    });

    this.socket.on('connect', () => {
      console.log('WebSocket connected');
      this.reconnectAttempts = 0;
    });

    this.socket.on('disconnect', () => {
      console.log('WebSocket disconnected');
      this.handleReconnect();
    });

    this.socket.on('error', (error: any) => {
      console.error('WebSocket error:', error);
    });
  }

  private handleReconnect(): void {
    if (this.reconnectAttempts < this.maxReconnectAttempts) {
      this.reconnectAttempts++;
      setTimeout(() => {
        this.connect();
      }, 1000 * this.reconnectAttempts);
    }
  }

  on(event: string, callback: (data: any) => void): void {
    this.socket?.on(event, callback);
  }

  emit(event: string, data: any): void {
    this.socket?.emit(event, data);
  }

  disconnect(): void {
    this.socket?.disconnect();
  }
}

const websocketService = new WebSocketService();
export default websocketService;
