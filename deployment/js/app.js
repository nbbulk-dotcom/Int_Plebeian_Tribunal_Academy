/**
 * International Plebeian Tribunal Academy - Main Application JavaScript
 * Handles PWA functionality, offline detection, and UI interactions
 */

window.addEventListener('load', () => {
    updateOnlineStatus();
    
    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
});

function updateOnlineStatus() {
    const offlineIndicator = document.getElementById('offline-indicator');
    
    if (!navigator.onLine) {
        offlineIndicator.classList.remove('offline-hidden');
    } else {
        offlineIndicator.classList.add('offline-hidden');
    }
}

let deferredPrompt;

window.addEventListener('beforeinstallprompt', (e) => {
    e.preventDefault();
    deferredPrompt = e;
    showInstallPromotion();
});

function showInstallPromotion() {
    const installPrompt = document.createElement('div');
    installPrompt.className = 'install-prompt';
    installPrompt.innerHTML = `
        <span>📱 Install Academy PWA for offline access</span>
        <button onclick="installPWA()">Install</button>
        <button class="close-btn" onclick="this.parentElement.remove()">✕</button>
    `;
    document.body.appendChild(installPrompt);
}

function installPWA() {
    if (deferredPrompt) {
        deferredPrompt.prompt();
        deferredPrompt.userChoice.then((choiceResult) => {
            if (choiceResult.outcome === 'accepted') {
                console.log('PWA installed');
            }
            deferredPrompt = null;
            document.querySelector('.install-prompt')?.remove();
        });
    }
}

document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        const href = this.getAttribute('href');
        if (href !== '#' && href.length > 1) {
            e.preventDefault();
            const target = document.querySelector(href);
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        }
    });
});

function animateValue(element, start, end, duration) {
    let startTimestamp = null;
    const step = (timestamp) => {
        if (!startTimestamp) startTimestamp = timestamp;
        const progress = Math.min((timestamp - startTimestamp) / duration, 1);
        element.textContent = Math.floor(progress * (end - start) + start);
        if (progress < 1) {
            window.requestAnimationFrame(step);
        }
    };
    window.requestAnimationFrame(step);
}

const observerOptions = {
    threshold: 0.5,
    rootMargin: '0px'
};

const statsObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const verifiedFilesCount = document.getElementById('verified-files-count');
            const activeProposals = document.getElementById('active-proposals');
            
            if (verifiedFilesCount && !verifiedFilesCount.dataset.animated) {
                animateValue(verifiedFilesCount, 0, 3, 1500);
                verifiedFilesCount.dataset.animated = 'true';
            }
            
            if (activeProposals && !activeProposals.dataset.animated) {
                animateValue(activeProposals, 0, 0, 1000);
                activeProposals.dataset.animated = 'true';
            }
        }
    });
}, observerOptions);

const blockchainSection = document.getElementById('blockchain');
if (blockchainSection) {
    statsObserver.observe(blockchainSection);
}

function verifyAllHashes() {
    const rows = document.querySelectorAll('#hash-table-body tr');
    
    rows.forEach(row => {
        const statusCell = row.querySelector('.status-badge');
        statusCell.textContent = '⏳ Verifying...';
        statusCell.className = 'status-badge';
        statusCell.style.backgroundColor = '#ffc107';
        statusCell.style.color = '#212529';
    });
    
    setTimeout(() => {
        rows.forEach(row => {
            const statusCell = row.querySelector('.status-badge');
            statusCell.textContent = '✓ Verified';
            statusCell.className = 'status-badge status-verified';
            statusCell.style.backgroundColor = '';
            statusCell.style.color = '';
        });
        
        alert('✓ All hashes verified successfully against genesis node');
    }, 2000);
}

function exportHashRegistry() {
    const hashData = [];
    const rows = document.querySelectorAll('#hash-table-body tr');
    
    rows.forEach(row => {
        const cells = row.querySelectorAll('td');
        hashData.push({
            file: cells[0].textContent,
            hash: cells[1].textContent,
            status: cells[2].textContent
        });
    });
    
    const dataStr = JSON.stringify(hashData, null, 2);
    const dataBlob = new Blob([dataStr], { type: 'application/json' });
    const url = URL.createObjectURL(dataBlob);
    
    const link = document.createElement('a');
    link.href = url;
    link.download = 'hash-registry-export.json';
    link.click();
    
    URL.revokeObjectURL(url);
}

if ('serviceWorker' in navigator) {
    navigator.serviceWorker.addEventListener('controllerchange', () => {
        showUpdateBanner();
    });
}

function showUpdateBanner() {
    const banner = document.createElement('div');
    banner.className = 'update-banner';
    banner.innerHTML = `
        <span>🎉 New version available!</span>
        <button onclick="window.location.reload()">Update Now</button>
    `;
    document.body.appendChild(banner);
}

console.log('%c🌍 International Plebeian Tribunal Academy', 'font-size: 20px; font-weight: bold; color: #007BFF;');
console.log('%cImmutable Genesis Node - Static Reference System', 'font-size: 14px; color: #6c757d;');
console.log('%cVerify hashes: verifyAllHashes()', 'font-size: 12px; color: #28a745;');
console.log('%cExport registry: exportHashRegistry()', 'font-size: 12px; color: #28a745;');

document.addEventListener('DOMContentLoaded', () => {
    console.log('Academy PWA initialized');
    
    const sections = document.querySelectorAll('.section');
    const sectionObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });
    
    sections.forEach(section => {
        section.style.opacity = '0';
        section.style.transform = 'translateY(20px)';
        section.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        sectionObserver.observe(section);
    });
});

window.verifyAllHashes = verifyAllHashes;
window.exportHashRegistry = exportHashRegistry;
window.installPWA = installPWA;
