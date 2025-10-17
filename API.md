# International Plebeian Academy API Documentation

## Overview

The International Plebeian Academy API provides a RESTful interface for interacting with the platform. All endpoints require authentication unless otherwise specified.

**Base URL:** `http://localhost:8000/api` (development)  
**Production URL:** `https://api.plebeianacademy.org/api`

**Authentication:** Bearer token in Authorization header  
**Content-Type:** `application/json`

---

## Authentication Endpoints

### Biometric Authentication

**POST** `/authentication/biometric/authenticate`

Authenticate user using biometric data.

**Request Body:**
```json
{
  "biometric_type": "fingerprint|iris|voice|face|behavioral",
  "biometric_data": "base64_encoded_data",
  "device_id": "string (optional)"
}
```

**Response (200 OK):**
```json
{
  "access_token": "jwt_token",
  "refresh_token": "jwt_token",
  "user": {
    "id": "user_id",
    "email": "user@example.com",
    "name": "User Name",
    "roles": ["member", "admin"]
  }
}
```

**Error Responses:**
- `400 Bad Request` - Missing required fields
- `401 Unauthorized` - Authentication failed

---

### Refresh Token

**POST** `/authentication/refresh`

Refresh access token using refresh token.

**Request Body:**
```json
{
  "refresh_token": "jwt_token"
}
```

**Response (200 OK):**
```json
{
  "access_token": "new_jwt_token"
}
```

---

### Logout

**POST** `/authentication/logout`

Logout current user.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "message": "Logged out successfully"
}
```

---

## System Management Endpoints

### Get System Health

**GET** `/system/health`

Retrieve current system health metrics.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "cpu": {
    "percent": 45.2,
    "count": 8
  },
  "memory": {
    "total": 16000000000,
    "available": 8000000000,
    "percent": 50.0
  },
  "disk": {
    "total": 500000000000,
    "used": 250000000000,
    "percent": 50.0
  },
  "network": {
    "bytes_sent": 1000000000,
    "bytes_recv": 2000000000
  }
}
```

---

### Get Version Information

**GET** `/system/versions`

Get current and available system versions.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "current": "1.0.0",
  "available": [
    {
      "number": "1.1.0",
      "description": "Enhanced security features",
      "releaseDate": "2025-11-01"
    }
  ]
}
```

---

### Initiate System Upgrade

**POST** `/system/upgrade`

Initiate system upgrade to specified version.

**Headers:** `Authorization: Bearer {access_token}`

**Request Body:**
```json
{
  "version": "1.1.0"
}
```

**Response (200 OK):**
```json
{
  "message": "Upgrade to version 1.1.0 initiated successfully",
  "status": "in_progress"
}
```

---

## Bot Management Endpoints

### List All Bots

**GET** `/bots`

Get all bots across all divisions.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "bots": [
    {
      "id": "bot_12345",
      "name": "Communications Bot 1",
      "division": "communications",
      "status": "active|inactive|error",
      "tasksCompleted": 42,
      "successRate": 95
    }
  ]
}
```

---

### Get Bot Details

**GET** `/bots/{bot_id}`

Get specific bot details.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "id": "bot_12345",
  "name": "Communications Bot 1",
  "division": "communications",
  "status": "active",
  "tasksCompleted": 42,
  "successRate": 95,
  "currentTask": "Processing user feedback",
  "lastActive": "2025-10-17T12:00:00Z"
}
```

**Error Responses:**
- `404 Not Found` - Bot not found

---

### Update Bot Status

**PUT** `/bots/{bot_id}/status`

Update bot status.

**Headers:** `Authorization: Bearer {access_token}`

**Request Body:**
```json
{
  "status": "active|inactive|error"
}
```

**Response (200 OK):**
```json
{
  "message": "Bot bot_12345 status updated to active",
  "bot": {
    "id": "bot_12345",
    "status": "active"
  }
}
```

**Error Responses:**
- `400 Bad Request` - Invalid status value
- `404 Not Found` - Bot not found

---

### Get Division Bots

**GET** `/bots/division/{division_name}`

Get all bots for a specific division.

**Headers:** `Authorization: Bearer {access_token}`

**Divisions:**
- `communications`
- `human_development`
- `support_resource`
- `action_project`
- `integrity_quality`
- `membership_voice`
- `strategic_direction`

**Response (200 OK):**
```json
{
  "bots": [
    {
      "id": "communications_bot_1",
      "name": "Communications Bot 1",
      "division": "communications",
      "status": "active"
    }
  ]
}
```

---

## Blockchain Endpoints

### Get Blockchain Status

**GET** `/blockchain/status`

Get current blockchain network status.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "blockHeight": 1234567,
  "transactionCount": 9876543,
  "gasPrice": "20 gwei",
  "networkStatus": "connected|disconnected|syncing",
  "nodeCount": 150,
  "lastBlockTime": "2025-10-17T12:00:00Z"
}
```

---

### Get Recent Transactions

**GET** `/blockchain/transactions?limit=50`

Get recent blockchain transactions.

**Headers:** `Authorization: Bearer {access_token}`

**Query Parameters:**
- `limit` (optional): Number of transactions to retrieve (default: 50, max: 100)

**Response (200 OK):**
```json
{
  "transactions": [
    {
      "hash": "0x123...",
      "from": "0xabc...",
      "to": "0xdef...",
      "value": "1.5 ETH",
      "timestamp": "2025-10-17T12:00:00Z",
      "status": "confirmed"
    }
  ]
}
```

---

### Verify File

**POST** `/blockchain/verify`

Verify file integrity using blockchain.

**Headers:** `Authorization: Bearer {access_token}`

**Request Body:**
```json
{
  "file_hash": "sha256_hash"
}
```

**Response (200 OK):**
```json
{
  "verified": true,
  "fileHash": "sha256_hash",
  "registeredAt": "2025-10-17T12:00:00Z",
  "blockNumber": 1234567,
  "transactionHash": "0x123..."
}
```

**Error Responses:**
- `400 Bad Request` - File hash required
- `404 Not Found` - File hash not found on blockchain

---

### Register File

**POST** `/blockchain/register`

Register file hash on blockchain.

**Headers:** `Authorization: Bearer {access_token}`

**Request Body:**
```json
{
  "file_hash": "sha256_hash",
  "metadata": {
    "filename": "document.pdf",
    "size": 1024000,
    "author": "user@example.com"
  }
}
```

**Response (200 OK):**
```json
{
  "success": true,
  "fileHash": "sha256_hash",
  "transactionHash": "0x123...",
  "blockNumber": 1234567,
  "metadata": {},
  "registeredAt": "2025-10-17T12:00:00Z"
}
```

---

## Distribution Network Endpoints

### Get Network Nodes

**GET** `/distribution/nodes`

Get all distribution network nodes.

**Headers:** `Authorization: Bearer {access_token}`

**Response (200 OK):**
```json
{
  "nodes": [
    {
      "id": "node_12345",
      "location": "New York, USA",
      "status": "online|offline|syncing",
      "version": "1.0.0",
      "peers": 42
    }
  ],
  "total": 150,
  "active": 142
}
```

---

## Error Responses

All endpoints may return the following error responses:

### 400 Bad Request
```json
{
  "error": "Invalid request parameters"
}
```

### 401 Unauthorized
```json
{
  "message": "Token is missing or invalid"
}
```

### 403 Forbidden
```json
{
  "error": "Insufficient permissions"
}
```

### 404 Not Found
```json
{
  "error": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "error": "Internal server error message"
}
```

---

## Rate Limiting

API requests are rate-limited to prevent abuse:
- **Authenticated requests:** 1000 requests per hour
- **Unauthenticated requests:** 100 requests per hour

Rate limit headers are included in all responses:
```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1634567890
```

---

## WebSocket API

The platform also provides WebSocket connections for real-time updates.

**WebSocket URL:** `ws://localhost:8000/ws` (development)

### Events

**System Health Updates:**
```json
{
  "event": "system_health",
  "data": {
    "cpu": 45.2,
    "memory": 50.0
  }
}
```

**Bot Status Updates:**
```json
{
  "event": "bot_status",
  "data": {
    "bot_id": "bot_12345",
    "status": "active"
  }
}
```

**Blockchain Updates:**
```json
{
  "event": "new_transaction",
  "data": {
    "hash": "0x123...",
    "from": "0xabc...",
    "to": "0xdef..."
  }
}
```

---

## SDK Support

Official SDKs are available for:
- Python
- JavaScript/TypeScript
- Go
- Rust

For SDK documentation, visit: https://docs.plebeianacademy.org/sdk

---

## Support

For API support and questions:
- Documentation: https://docs.plebeianacademy.org
- GitHub Issues: https://github.com/nbbulk-dotcom/Int_Plebeian_Tribunal_Academy/issues
- Email: api-support@plebeianacademy.org
