/**
 * International Plebeian Tribunal Academy - Service Worker
 * Enables offline functionality and caching for PWA
 */

const CACHE_NAME = 'academy-v1.0.0';
const RUNTIME_CACHE = 'academy-runtime-v1.0.0';

const PRECACHE_ASSETS = [
    '/',
    '/index.html',
    '/css/main.css',
    '/css/pwa.css',
    '/js/app.js',
    '/js/verification.js',
    '/manifest.json',
    '/images/academy-logo.svg',
    '/images/icons/icon-192.png',
    '/fonts/OpenSans-Regular.woff2'
];

self.addEventListener('install', (event) => {
    console.log('Service Worker installing...');
    
    event.waitUntil(
        caches.open(CACHE_NAME)
            .then((cache) => {
                console.log('Caching core assets');
                return cache.addAll(PRECACHE_ASSETS);
            })
            .then(() => self.skipWaiting())
    );
});

self.addEventListener('activate', (event) => {
    console.log('Service Worker activating...');
    
    event.waitUntil(
        caches.keys()
            .then((cacheNames) => {
                return Promise.all(
                    cacheNames
                        .filter((name) => {
                            return name !== CACHE_NAME && name !== RUNTIME_CACHE;
                        })
                        .map((name) => {
                            console.log('Deleting old cache:', name);
                            return caches.delete(name);
                        })
                );
            })
            .then(() => self.clients.claim())
    );
});

self.addEventListener('fetch', (event) => {
    if (!event.request.url.startsWith(self.location.origin)) {
        return;
    }
    
    if (event.request.method !== 'GET') {
        return;
    }
    
    event.respondWith(
        caches.match(event.request)
            .then((cachedResponse) => {
                if (cachedResponse) {
                    return cachedResponse;
                }
                
                return fetch(event.request)
                    .then((response) => {
                        if (!response || response.status !== 200 || response.type === 'error') {
                            return response;
                        }
                        
                        const responseToCache = response.clone();
                        
                        caches.open(RUNTIME_CACHE)
                            .then((cache) => {
                                cache.put(event.request, responseToCache);
                            });
                        
                        return response;
                    })
                    .catch(() => {
                        return caches.match('/index.html');
                    });
            })
    );
});

self.addEventListener('message', (event) => {
    if (event.data === 'skipWaiting') {
        self.skipWaiting();
    }
    
    if (event.data === 'clearCache') {
        event.waitUntil(
            caches.keys()
                .then((cacheNames) => {
                    return Promise.all(
                        cacheNames.map((name) => caches.delete(name))
                    );
                })
                .then(() => {
                    return self.clients.matchAll();
                })
                .then((clients) => {
                    clients.forEach((client) => {
                        client.postMessage({ type: 'cacheCleared' });
                    });
                })
        );
    }
});

if ('sync' in self.registration) {
    self.addEventListener('sync', (event) => {
        if (event.tag === 'verify-hashes') {
            event.waitUntil(
                fetch('/js/verification.js')
                    .then(() => console.log('Background verification completed'))
                    .catch(() => console.log('Background verification failed'))
            );
        }
    });
}

console.log('Service Worker loaded');
