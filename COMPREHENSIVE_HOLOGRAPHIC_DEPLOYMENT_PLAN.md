# COMPREHENSIVE HOLOGRAPHIC DEPLOYMENT PLAN
## International Plebeian Academy - Multi-AI Collaborative Architecture

**Document Version**: 1.0  
**Date**: October 17, 2025  
**Purpose**: AI Collaboration Review (Grok, Devin, Manus, Claude/GPT-4)  
**Author**: Devin AI Session cc9765b328b84b3482c0d8bd7d799c16

---

## EXECUTIVE SUMMARY

This document outlines a revolutionary three-layer holographic deployment architecture for the International Plebeian Academy that leverages the unique strengths of multiple AI platforms (Manus AI, Devin AI, and production infrastructure) to create an inviolable, globally distributed peace advocacy platform with built-in integrity verification.

### Core Innovation
Using Manus AI's static, immutable nature as the foundational "genesis node" for a holographic verification system where all dynamic nodes worldwide verify their integrity against fixed reference hashes stored on the Manus platform.

---

## SYSTEM ARCHITECTURE OVERVIEW

### The Three-Layer Holographic Model

```
┌─────────────────────────────────────────────────────────────────┐
│                   LAYER 1: MANUS STATIC CORE                    │
│              (Immutable Reference & Genesis Node)                │
│                                                                  │
│  • Fixed verification hashes (SHA-256)                          │
│  • Master file registry                                         │
│  • Blockchain genesis anchor points                             │
│  • Core documentation (unchanging)                              │
│  • API endpoint manifest                                        │
│                                                                  │
│  Nature: Single-page static HTML with embedded JSON data        │
│  Role: Immutable truth source for integrity verification        │
└──────────────────────┬──────────────────────────────────────────┘
                       │
                       │ Verification Protocol
                       │ (All nodes check against Manus core)
                       │
         ┌─────────────┴─────────────┬─────────────────────┐
         │                           │                      │
         ▼                           ▼                      ▼
┌────────────────┐         ┌────────────────┐    ┌────────────────┐
│  LAYER 2:      │         │  LAYER 3:      │    │ WORLDWIDE      │
│  DEVIN MIRROR  │◄────────┤  PRODUCTION    │◄───┤ HOLOGRAPHIC    │
│                │         │  MAIN SITE     │    │ NODES          │
│  • Public demo │         │                │    │                │
│  • Permanent   │         │ plebeiantrib.. │    │ • Chapter 1    │
│  • Testing     │         │                │    │ • Chapter 2    │
│  • Backup node │         │ + SA Division  │    │ • Chapter N    │
└────────────────┘         └────────────────┘    └────────────────┘
```

---

## LAYER 1: MANUS AI STATIC CORE

### Purpose
Create an immutable, static reference node that serves as the foundational truth source for the entire holographic network. This leverages Manus AI's inability to perform background processing as a FEATURE rather than a limitation.

### Technical Specifications

#### 1. Single-Page Static Architecture
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>International Plebeian Academy - Genesis Core</title>
    <meta name="description" content="Immutable verification core for holographic network">
</head>
<body>
    <!-- Navigation Links Between Sections -->
    <nav id="core-navigation">
        <a href="#genesis">Genesis Registry</a>
        <a href="#verification">Verification Hashes</a>
        <a href="#blockchain">Blockchain Anchors</a>
        <a href="#documentation">Core Documentation</a>
        <a href="#api">API Manifest</a>
    </nav>

    <!-- Section 1: Genesis Registry -->
    <section id="genesis" data-hash="[MASTER_HASH]">
        <!-- Master file registry with creation timestamps -->
    </section>

    <!-- Section 2: Verification Hashes -->
    <section id="verification">
        <!-- SHA-256 hashes of all core system files -->
    </section>

    <!-- Section 3: Blockchain Anchors -->
    <section id="blockchain">
        <!-- Genesis block references and smart contract addresses -->
    </section>

    <!-- Section 4: Core Documentation -->
    <section id="documentation">
        <!-- Immutable core documentation -->
    </section>

    <!-- Section 5: API Manifest -->
    <section id="api">
        <!-- Expected API endpoints and their signatures -->
    </section>

    <!-- Embedded Verification Data (JSON) -->
    <script type="application/json" id="verification-data">
    {
        "genesis_timestamp": "2025-10-17T00:00:00Z",
        "master_hash": "SHA256_OF_ENTIRE_CORE",
        "file_registry": {
            "README.md": {
                "hash": "SHA256_HASH",
                "size": 7776,
                "timestamp": "2025-10-17T00:00:00Z"
            }
        },
        "blockchain_anchors": {
            "tribal_coin_contract": "0x...",
            "file_verification_contract": "0x...",
            "genesis_block": "0x..."
        },
        "api_manifest": {
            "endpoints": [
                "/api/verify",
                "/api/health"
            ]
        }
    }
    </script>
</body>
</html>
```

#### 2. Core Data Structures

**Master File Registry**
- Every file in the system with its SHA-256 hash
- Creation timestamp (immutable)
- File size for verification
- MIME type
- Version number

**Blockchain Anchors**
- Smart contract addresses (TribalCoin, FileVerification)
- Genesis block hash
- Initial supply and distribution records
- Contract deployment timestamps

**API Manifest**
- Complete list of expected API endpoints
- Request/response signatures
- Authentication requirements
- Rate limits

**Verification Protocol**
- Public keys for signature verification
- Certificate chains
- Trusted node registry (initial seed nodes)

#### 3. Manus-Specific Optimizations

**Single-Page Design**
- All critical data on one scrollable page
- Internal anchor links for navigation
- No external dependencies
- Self-contained HTML/CSS/JSON
- No JavaScript execution required (data only)

**Static Data Embedding**
- JSON-LD structured data for machine readability
- Meta tags for SEO and discovery
- Embedded checksums for self-verification
- Human-readable and machine-parseable

**Inviolability Features**
- Page itself has a master hash published via blockchain
- Any change to the page invalidates the hash
- Acts as a "snapshot in time" of the system's genesis state
- Can never be "updated" - only a new version deployed with new hash

---

## LAYER 2: DEVIN MIRROR DEPLOYMENT

### Purpose
Create a publicly accessible, permanent demonstration and backup node that showcases the full International Plebeian Academy platform while maintaining real-time verification against the Manus static core.

### Technical Specifications

#### 1. Deployment Architecture
- **Platform**: Devin's deployment infrastructure (Fly.io for backend, static hosting for frontend)
- **Persistence**: Permanent public URL
- **Components**: Full React PWA frontend + Flask backend + PostgreSQL database

#### 2. Core Features
- Complete 7-division bot system (35 bots)
- Biometric authentication (demo mode with simulated data)
- Blockchain integration (testnet)
- Holographic distribution visualization
- Real-time WebSocket communication
- Progressive Web App capabilities

#### 3. Verification Integration

**Startup Verification**
```python
# Backend startup verification against Manus core
async def verify_against_manus_core():
    """
    On application startup, fetch Manus static core and verify
    our system files match the registered hashes
    """
    manus_core_url = "https://manus-deployed-site.com"
    
    # Fetch verification data from Manus
    manus_data = await fetch_manus_verification_data(manus_core_url)
    
    # Calculate hashes of our local files
    local_hashes = calculate_local_file_hashes()
    
    # Compare and verify
    verification_result = compare_hashes(manus_data['file_registry'], local_hashes)
    
    if not verification_result.valid:
        log_critical_error("System integrity compromised!")
        send_alert_to_administrators()
        # Continue in read-only mode
        set_read_only_mode()
    
    return verification_result
```

**Periodic Verification**
- Every 1 hour: Re-verify against Manus core
- Every file access: Check hash matches registry
- Every blockchain transaction: Verify against anchors
- Every API call: Validate against manifest

#### 4. Demo-Specific Features
- Pre-populated demo data showing system capabilities
- Interactive tutorials for new users
- System architecture visualization
- Real-time metrics dashboard
- Public read access (no authentication required for viewing)

---

## LAYER 3: PRODUCTION MAIN SITE

### Purpose
Deploy the full production International Plebeian Academy platform at plebeiantribunalsa.co.za while integrating the existing South African site as a specialized division.

### Technical Specifications

#### 1. Main Site Architecture

**Domain Structure**
```
https://www.plebeiantribunalsa.co.za
├── /                                    (International Academy Homepage)
├── /dashboard                           (User Dashboard)
├── /divisions/
│   ├── /communications                  (Division 1)
│   ├── /human-development              (Division 2)
│   ├── /support-resource               (Division 3)
│   ├── /action-project                 (Division 4)
│   ├── /integrity-quality              (Division 5)
│   ├── /membership-voice               (Division 6)
│   └── /strategic-innovation           (Division 7)
├── /sa-division/                        (South African Division - OLD SITE)
│   └── [Entire existing site structure preserved]
├── /chapters/
│   ├── /south-africa                   (New SA chapter page)
│   ├── /namibia
│   ├── /zimbabwe
│   └── ...
└── /blockchain/
    ├── /tribal-coin
    └── /governance
```

#### 2. South African Division Integration

**Preserving Existing Site**
The current plebeiantribunalsa.co.za will be preserved entirely under `/sa-division/`:

```
Current Site Structure → New Structure
─────────────────────────────────────────
/                    → /sa-division/
/about               → /sa-division/about
/cases               → /sa-division/cases
/resources           → /sa-division/resources
/contact             → /sa-division/contact
```

**Migration Strategy**
1. Clone existing site to `/sa-division/` subdirectory
2. Update all internal links to use relative paths
3. Add navigation bridge between old and new sites
4. Preserve all existing functionality
5. Add header banner: "Part of International Plebeian Academy"

**Integration Benefits**
- Existing users maintain access to familiar interface
- All historical data preserved
- South African legal resources remain accessible
- Gradual migration path for users
- SEO preservation through 301 redirects

#### 3. Verification System

**Multi-Layer Verification**
```javascript
// Frontend verification service
class IntegrityVerificationService {
    constructor() {
        this.manusCore = 'https://manus-static-core.com';
        this.verificationInterval = 3600000; // 1 hour
        this.lastVerification = null;
    }

    async verifySystemIntegrity() {
        try {
            // 1. Fetch Manus core verification data
            const coreData = await this.fetchManusCore();
            
            // 2. Verify current file hashes
            const fileVerification = await this.verifyFileHashes(coreData);
            
            // 3. Verify blockchain anchors
            const blockchainVerification = await this.verifyBlockchainAnchors(coreData);
            
            // 4. Verify API endpoints
            const apiVerification = await this.verifyAPIManifest(coreData);
            
            // 5. Aggregate results
            const overallStatus = this.aggregateVerificationResults({
                files: fileVerification,
                blockchain: blockchainVerification,
                api: apiVerification
            });
            
            // 6. Update verification badge
            this.updateVerificationBadge(overallStatus);
            
            return overallStatus;
        } catch (error) {
            console.error('Verification failed:', error);
            this.displayVerificationWarning();
        }
    }

    async fetchManusCore() {
        const response = await fetch(`${this.manusCore}/verification-data`);
        const html = await response.text();
        
        // Parse embedded JSON from Manus static page
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const dataElement = doc.getElementById('verification-data');
        return JSON.parse(dataElement.textContent);
    }
}
```

#### 4. Production Features

**Full Bot System**
- All 35 bots operational with real data
- Machine learning models trained on real cases
- Automated task assignment and tracking
- AI-powered legal research and analysis

**Real Biometric Authentication**
- Integration with device biometric sensors
- Multi-factor authentication
- Secure session management
- Role-based access control

**Production Blockchain**
- Mainnet deployment (Ethereum or Polygon)
- Real TribalCoin trading and governance
- Immutable file verification
- Smart contract auditing

**Global Features**
- Multi-language support (50+ languages)
- Regional chapter management
- Distributed decision-making
- Cross-border coordination

---

## HOLOGRAPHIC VERIFICATION PROTOCOL

### Core Concept
Every node in the network periodically verifies its integrity by checking against the immutable Manus static core. This creates a "holographic" security model where the integrity of the whole is maintained through constant verification against an unchanging reference.

### Verification Workflow

```
┌──────────────────────────────────────────────────────────────┐
│                    VERIFICATION CYCLE                         │
└──────────────────────────────────────────────────────────────┘

1. NODE STARTUP
   │
   ├─► Fetch Manus Core Data
   ├─► Calculate Local Hashes
   ├─► Compare Against Registry
   └─► Log Verification Result
       │
       ├─► PASS → Continue Normal Operation
       └─► FAIL → Enter Read-Only Mode + Alert Admins

2. PERIODIC VERIFICATION (Every Hour)
   │
   ├─► Re-verify All Core Files
   ├─► Check Blockchain Anchors
   ├─► Validate API Endpoints
   └─► Update Verification Badge

3. ON-DEMAND VERIFICATION
   │
   ├─► User clicks "Verify Integrity" button
   ├─► Real-time hash calculation
   ├─► Display detailed verification report
   └─► Show trust score

4. FILE ACCESS VERIFICATION
   │
   ├─► Before serving any critical file
   ├─► Calculate current hash
   ├─► Compare to Manus registry
   └─► Serve only if verified

5. BLOCKCHAIN TRANSACTION VERIFICATION
   │
   ├─► Before submitting transaction
   ├─► Verify contract address against Manus anchors
   ├─► Verify transaction format
   └─► Submit only if verified
```

### Verification API

```python
# Backend verification API
from flask import Flask, jsonify
import hashlib
import requests

app = Flask(__name__)

MANUS_CORE_URL = "https://manus-static-core.com"

@app.route('/api/verify/integrity', methods=['GET'])
def verify_integrity():
    """
    Comprehensive system integrity check against Manus core
    """
    # Fetch Manus verification data
    manus_data = fetch_manus_core_data()
    
    # Perform verification
    results = {
        'files': verify_file_hashes(manus_data['file_registry']),
        'blockchain': verify_blockchain_anchors(manus_data['blockchain_anchors']),
        'api': verify_api_manifest(manus_data['api_manifest']),
        'timestamp': datetime.utcnow().isoformat(),
        'manus_core_hash': calculate_manus_page_hash()
    }
    
    # Calculate overall trust score
    results['trust_score'] = calculate_trust_score(results)
    results['status'] = 'verified' if results['trust_score'] >= 95 else 'warning'
    
    return jsonify(results)

@app.route('/api/verify/file/<path:filename>', methods=['GET'])
def verify_file(filename):
    """
    Verify a specific file against Manus registry
    """
    manus_data = fetch_manus_core_data()
    
    if filename not in manus_data['file_registry']:
        return jsonify({'error': 'File not in registry'}), 404
    
    expected_hash = manus_data['file_registry'][filename]['hash']
    actual_hash = calculate_file_hash(filename)
    
    return jsonify({
        'filename': filename,
        'expected_hash': expected_hash,
        'actual_hash': actual_hash,
        'verified': expected_hash == actual_hash
    })

def fetch_manus_core_data():
    """
    Fetch and parse verification data from Manus static core
    """
    response = requests.get(MANUS_CORE_URL, timeout=30)
    html = response.text
    
    # Extract JSON from script tag
    import re
    match = re.search(r'<script type="application/json" id="verification-data">(.*?)</script>', 
                     html, re.DOTALL)
    if match:
        return json.loads(match.group(1))
    raise ValueError("Could not parse Manus core data")

def calculate_file_hash(filename):
    """
    Calculate SHA-256 hash of a file
    """
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()
```

---

## WORLDWIDE HOLOGRAPHIC NODES

### Node Types

#### 1. Chapter Nodes
Each local chapter (South Africa, Namibia, Zimbabwe, etc.) operates its own node:
- Local instance of the Academy platform
- Regional customization (language, laws, cases)
- Autonomous operation with periodic sync
- Verifies against both Manus core and parent nodes

#### 2. Division Nodes
Each of the 7 divisions can operate specialized nodes:
- Division-specific functionality
- Specialized bot configurations
- Division data isolation
- Cross-division communication protocols

#### 3. Mirror Nodes
Public mirror nodes for redundancy:
- Read-only access
- Geographic distribution
- Load balancing
- DDoS protection

### Node Registration Protocol

```javascript
// Node registration with verification
class HolographicNode {
    async registerNode() {
        // 1. Verify against Manus core
        const verification = await this.verifyAgainstManusCore();
        
        if (!verification.valid) {
            throw new Error('Failed Manus core verification');
        }
        
        // 2. Generate node credentials
        const nodeCredentials = await this.generateNodeCredentials();
        
        // 3. Register with parent node
        const registration = await this.registerWithParent({
            nodeId: nodeCredentials.id,
            publicKey: nodeCredentials.publicKey,
            verification: verification,
            capabilities: this.getNodeCapabilities(),
            geolocation: this.getGeolocation()
        });
        
        // 4. Receive authorization token
        this.authToken = registration.token;
        
        // 5. Join holographic network
        await this.joinHolographicNetwork();
        
        return registration;
    }
}
```

---

## SECURITY ARCHITECTURE

### Multi-Layer Security Model

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: Manus Static Core (Immutable Truth)               │
│          • No dynamic code execution                        │
│          • Blockchain-anchored page hash                    │
│          • Read-only HTTP access                            │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: Verification Protocol (Integrity Checking)        │
│          • Periodic hash verification                       │
│          • Certificate pinning                              │
│          • Signature validation                             │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: Node Security (Individual Protection)             │
│          • Biometric authentication                         │
│          • Encrypted communications (TLS 1.3)               │
│          • Rate limiting                                    │
│          • DDoS protection                                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│ LAYER 4: Blockchain Security (Immutable Records)           │
│          • Smart contract auditing                          │
│          • Multi-signature requirements                     │
│          • Time-locked transactions                         │
└─────────────────────────────────────────────────────────────┘
```

### Attack Mitigation Strategies

**Scenario 1: Compromised Node**
- Node fails Manus verification
- Automatically enters read-only mode
- Alerts sent to all connected nodes
- Node quarantined from network
- Admin notified for investigation

**Scenario 2: Manus Core Tampering**
- Manus page hash published on blockchain
- Any change invalidates blockchain reference
- Nodes detect hash mismatch
- Network-wide alert triggered
- Emergency protocol activated

**Scenario 3: Man-in-the-Middle Attack**
- Certificate pinning prevents MITM
- All communications over TLS 1.3
- Public key infrastructure
- Encrypted node-to-node communication

**Scenario 4: Blockchain Attack**
- Multi-signature requirements for critical operations
- Time-locked transactions prevent rapid theft
- Community governance can freeze suspicious contracts
- Backup contracts ready for deployment

---

## DEPLOYMENT SEQUENCE

### Phase 1: Foundation (Week 1)
1. **Create Manus Static Core**
   - Generate complete file registry with hashes
   - Document all blockchain anchors
   - Create API manifest
   - Deploy to Manus AI platform
   - Publish page hash to blockchain

2. **Verification System Development**
   - Implement hash calculation utilities
   - Create verification API
   - Build monitoring dashboard
   - Test verification protocol

### Phase 2: Devin Mirror (Week 2)
1. **Backend Deployment**
   - Deploy Flask API to Fly.io
   - Configure PostgreSQL database
   - Set up environment variables
   - Deploy bot system

2. **Frontend Deployment**
   - Build React PWA
   - Deploy to static hosting
   - Configure service workers
   - Enable offline capabilities

3. **Integration Testing**
   - Test verification against Manus core
   - Verify all 29 API endpoints
   - Test bot coordination
   - Load testing

### Phase 3: Production Site (Week 3-4)
1. **SA Division Integration**
   - Clone existing plebeiantribunalsa.co.za
   - Restructure under `/sa-division/`
   - Update all links and references
   - Test existing functionality

2. **Main Site Deployment**
   - Deploy International Academy platform
   - Configure domain and SSL
   - Set up CDN
   - Deploy monitoring

3. **Data Migration**
   - Migrate existing SA user data
   - Import historical cases
   - Preserve all records
   - Verify data integrity

### Phase 4: Worldwide Rollout (Week 5+)
1. **Chapter Node Deployment**
   - Provide node deployment guide
   - Assist chapters with setup
   - Register nodes in network
   - Verify connectivity

2. **Network Testing**
   - Test inter-node communication
   - Verify holographic distribution
   - Load balancing validation
   - Failover testing

---

## TECHNICAL REQUIREMENTS

### Manus AI Platform
- Single HTML file (with embedded CSS and JSON)
- Maximum file size: TBD based on Manus limits
- No external dependencies
- No JavaScript execution required
- Optimized for static hosting

### Devin AI Platform
- Backend: Python 3.10+, Flask, PostgreSQL
- Frontend: Node.js 18+, React 18, TypeScript
- Deployment: Fly.io (backend), Static hosting (frontend)
- Database: PostgreSQL 14+

### Production Platform (plebeiantribunalsa.co.za)
- Server: Ubuntu 22.04 LTS or similar
- Web Server: Nginx + Gunicorn
- Database: PostgreSQL 14+ with PostGIS
- Caching: Redis
- CDN: Cloudflare or similar
- SSL: Let's Encrypt certificates

### Blockchain
- Network: Ethereum Mainnet or Polygon
- Smart Contracts: Solidity ^0.8.19
- Tools: Hardhat, Ethers.js
- Wallet: MetaMask integration

---

## QUESTIONS FOR AI COLLABORATION REVIEW

Please have each AI (Grok, Devin, Manus, Claude/GPT-4) review and provide feedback on:

### Architecture Questions
1. Is the three-layer holographic model sound?
2. Are there better ways to leverage Manus AI's static nature?
3. Should we add additional verification layers?
4. What are potential security vulnerabilities?

### Implementation Questions
1. Is the Manus static core design optimal?
2. Should the verification protocol be more frequent/less frequent?
3. Are there better hash algorithms than SHA-256?
4. Should we use blockchain more extensively?

### Integration Questions
1. Is the SA Division integration strategy sound?
2. Should existing users be migrated automatically or opt-in?
3. How do we handle data conflicts between old and new systems?
4. What's the best way to preserve SEO during migration?

### Scalability Questions
1. Can this architecture scale to 1000+ nodes?
2. What are bandwidth concerns for verification protocol?
3. Should we implement caching for Manus core data?
4. How do we handle Manus platform going offline?

### Innovation Opportunities
1. Could we use IPFS for Manus core distribution?
2. Should we implement quantum-resistant cryptography?
3. Can we leverage zero-knowledge proofs for privacy?
4. Should we add AI-powered anomaly detection?

---

## SUCCESS METRICS

### Technical Metrics
- **Verification Success Rate**: >99.9% of verifications pass
- **Node Uptime**: >99.5% availability
- **Response Time**: <500ms for API calls
- **Verification Time**: <10 seconds for full integrity check

### User Metrics
- **User Retention**: >80% monthly active users
- **Chapter Adoption**: >50 chapters within 6 months
- **Transaction Volume**: >1000 TribalCoin transactions/day
- **Bot Utilization**: >70% of tasks automated

### Security Metrics
- **Zero Successful Attacks**: No node compromises
- **Alert Response Time**: <5 minutes to critical alerts
- **Verification Failures**: <0.1% false positives
- **Patch Deployment**: <24 hours for critical updates

---

## CONCLUSION

This comprehensive holographic deployment plan leverages the unique strengths of three platforms:

1. **Manus AI**: Immutable static core for integrity verification
2. **Devin AI**: Rapid deployment and public demonstration
3. **Production**: Full-featured, scalable global platform

By using Manus's immutability as a security feature rather than a limitation, we create an innovative verification system that ensures the integrity of a globally distributed network.

The integration of the existing South African site preserves years of work while enabling expansion to international scale. The holographic model ensures that no single point of failure can compromise the entire network.

This is a revolutionary approach to building resilient, verifiable, globally distributed systems for peace advocacy.

---

## NEXT STEPS

1. **Distribute this document** to Grok, Devin (other sessions), Manus, and Claude/GPT-4
2. **Collect feedback** and suggestions from each AI
3. **Synthesize responses** into a unified implementation plan
4. **Create detailed technical specifications** for each component
5. **Begin phased development** starting with Manus static core

---

**Document prepared for AI collaboration by:**  
Devin AI Session: cc9765b328b84b3482c0d8bd7d799c16  
User: @nbbulk-dotcom (nbbulk@gmail.com)  
Date: October 17, 2025
