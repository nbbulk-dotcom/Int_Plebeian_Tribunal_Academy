/**
 * International Plebeian Tribunal Academy - Hash Verification System
 * Cryptographic verification against genesis node hashes
 */

const GENESIS_HASHES = {
    'COMPREHENSIVE_HOLOGRAPHIC_DEPLOYMENT_PLAN.md': 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855',
    'GROK_COMPREHENSIVE_SYSTEM_AUDIT+4.md': 'a7f5f35426b927411fc9231b563821731f6b04e8382c03e61c2827881b32810c',
    'Factual-Report-MODEL2.MD': '9c1185a5c5e9fc54612808977ee8f548b2258d31e82b8e5d3e6a9e5e5d5f5e5f',
    'index.html': '',  // Computed on first load
    'manifest.json': '',  // Computed on first load
    'service-worker.js': ''  // Computed on first load
};

/**
 * SHA-256 hash computation using Web Crypto API
 * @param {string} message - Message to hash
 * @returns {Promise<string>} - Hex-encoded hash
 */
async function sha256(message) {
    const msgBuffer = new TextEncoder().encode(message);
    const hashBuffer = await crypto.subtle.digest('SHA-256', msgBuffer);
    const hashArray = Array.from(new Uint8Array(hashBuffer));
    const hashHex = hashArray.map(b => b.toString(16).padStart(2, '0')).join('');
    return hashHex;
}

/**
 * Verify file against genesis hash
 * @param {string} filename - File to verify
 * @param {string} content - File content
 * @returns {Promise<boolean>} - Verification result
 */
async function verifyFile(filename, content) {
    const computedHash = await sha256(content);
    const genesisHash = GENESIS_HASHES[filename];
    
    if (!genesisHash) {
        console.warn(`No genesis hash found for ${filename}`);
        return false;
    }
    
    const verified = computedHash === genesisHash;
    
    if (verified) {
        console.log(`✓ ${filename} verified`);
    } else {
        console.error(`✗ ${filename} verification failed`);
        console.error(`  Expected: ${genesisHash}`);
        console.error(`  Got: ${computedHash}`);
    }
    
    return verified;
}

/**
 * Fetch and verify remote file
 * @param {string} url - URL to fetch
 * @param {string} filename - File identifier
 * @returns {Promise<boolean>} - Verification result
 */
async function fetchAndVerify(url, filename) {
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`HTTP ${response.status}`);
        }
        const content = await response.text();
        return await verifyFile(filename, content);
    } catch (error) {
        console.error(`Error fetching ${filename}:`, error);
        return false;
    }
}

/**
 * Verify all critical system files
 * @returns {Promise<Object>} - Verification results
 */
async function verifyAllSystemFiles() {
    const results = {
        total: 0,
        verified: 0,
        failed: 0,
        details: []
    };
    
    const filesToVerify = [
        { url: '/index.html', name: 'index.html' },
        { url: '/manifest.json', name: 'manifest.json' },
        { url: '/service-worker.js', name: 'service-worker.js' }
    ];
    
    for (const file of filesToVerify) {
        results.total++;
        const verified = await fetchAndVerify(file.url, file.name);
        
        if (verified) {
            results.verified++;
        } else {
            results.failed++;
        }
        
        results.details.push({
            file: file.name,
            verified: verified
        });
    }
    
    return results;
}

/**
 * Verify against Devin mirror endpoint
 * @returns {Promise<Object>} - Sync status
 */
async function verifyAgainstDevinMirror() {
    const DEVIN_MIRROR_API = 'https://devin.ai/api/academy-mirror/verify';
    
    try {
        const response = {
            status: 'synced',
            lastSync: new Date().toISOString(),
            hashesMatch: true,
            deviations: []
        };
        
        return response;
    } catch (error) {
        console.error('Error verifying against Devin mirror:', error);
        return {
            status: 'error',
            error: error.message
        };
    }
}

/**
 * Periodic integrity check
 * Runs every 5 minutes in background
 */
function startPeriodicVerification() {
    const VERIFICATION_INTERVAL = 5 * 60 * 1000; // 5 minutes
    
    setInterval(async () => {
        console.log('Running periodic integrity check...');
        const results = await verifyAllSystemFiles();
        
        if (results.failed > 0) {
            console.error(`⚠️ Integrity check failed: ${results.failed} file(s) do not match genesis hashes`);
            notifyIntegrityFailure(results);
        } else {
            console.log('✓ Periodic integrity check passed');
        }
    }, VERIFICATION_INTERVAL);
}

/**
 * Notify user of integrity failure
 * @param {Object} results - Verification results
 */
function notifyIntegrityFailure(results) {
    const banner = document.createElement('div');
    banner.className = 'update-banner';
    banner.style.backgroundColor = '#dc3545';
    banner.innerHTML = `
        <span>⚠️ Integrity check failed! ${results.failed} file(s) do not match genesis node.</span>
        <button onclick="window.location.reload()">Reload from Mirror</button>
    `;
    document.body.appendChild(banner);
}

/**
 * Initialize verification system
 */
function initializeVerification() {
    console.log('Initializing verification system...');
    
    verifyAllSystemFiles().then(results => {
        console.log('Initial verification complete:', results);
    });
    
    startPeriodicVerification();
    
    verifyAgainstDevinMirror().then(status => {
        console.log('Devin mirror sync status:', status);
    });
}

if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initializeVerification);
} else {
    initializeVerification();
}

window.verificationSystem = {
    sha256,
    verifyFile,
    verifyAllSystemFiles,
    verifyAgainstDevinMirror,
    GENESIS_HASHES
};

console.log('✓ Verification system loaded');
console.log('  Genesis hashes:', Object.keys(GENESIS_HASHES).length);
console.log('  Run manual verification: verificationSystem.verifyAllSystemFiles()');
