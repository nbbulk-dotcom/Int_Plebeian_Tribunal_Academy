# 📋 Deployment Checklist - International Plebeian Tribunal Academy

**Version:** 1.0.0  
**Date:** October 17, 2025  
**Deployment Target:** Afrihost (Production) + Devin AI (Mirror)

---

## PRE-DEPLOYMENT CHECKLIST

### Files Verification
- [ ] All HTML files present and valid
- [ ] All CSS files present and minified
- [ ] All JavaScript files present and functional
- [ ] All image files present and optimized
- [ ] All font files present
- [ ] Manifest.json configured correctly
- [ ] Service worker present
- [ ] .htaccess configured for Apache
- [ ] robots.txt present
- [ ] All historical site files preserved

### Content Verification
- [ ] Homepage loads correctly
- [ ] Navigation links functional
- [ ] All sections populated with content
- [ ] Historical site pages complete
- [ ] No placeholder text remaining
- [ ] No lorem ipsum content
- [ ] All external links tested
- [ ] Contact information correct

### Technical Verification
- [ ] HTML validates (W3C validator)
- [ ] CSS validates
- [ ] JavaScript console shows no errors
- [ ] All relative paths correct
- [ ] No broken internal links
- [ ] No 404 errors
- [ ] UTF-8 encoding throughout
- [ ] Responsive design works on mobile

---

## LOCAL TESTING CHECKLIST

### Functional Testing
- [ ] Homepage loads: **PASS / FAIL**
- [ ] CSS styles apply correctly: **PASS / FAIL**
- [ ] JavaScript functions execute: **PASS / FAIL**
- [ ] Logo displays: **PASS / FAIL**
- [ ] Navigation menu works: **PASS / FAIL**
- [ ] All anchor links scroll to sections: **PASS / FAIL**
- [ ] External links open in new tabs: **PASS / FAIL**
- [ ] Historical site loads: **PASS / FAIL**
- [ ] Historical navigation works: **PASS / FAIL**

### PWA Testing
- [ ] Manifest.json loads: **PASS / FAIL**
- [ ] Service worker registers: **PASS / FAIL**
- [ ] Install prompt appears: **PASS / FAIL**
- [ ] App installs successfully: **PASS / FAIL**
- [ ] Offline mode works: **PASS / FAIL**
- [ ] Offline indicator displays: **PASS / FAIL**
- [ ] Cached pages load offline: **PASS / FAIL**

### Verification System Testing
- [ ] Hash table displays: **PASS / FAIL**
- [ ] "Run Verification" button works: **PASS / FAIL**
- [ ] Verification completes successfully: **PASS / FAIL**
- [ ] "Export Registry" button works: **PASS / FAIL**
- [ ] JSON export downloads: **PASS / FAIL**

### Cross-Browser Testing
- [ ] Chrome/Chromium: **PASS / FAIL**
- [ ] Firefox: **PASS / FAIL**
- [ ] Safari: **PASS / FAIL**
- [ ] Edge: **PASS / FAIL**
- [ ] Mobile Chrome: **PASS / FAIL**
- [ ] Mobile Safari: **PASS / FAIL**

### Responsive Design Testing
- [ ] Desktop (1920x1080): **PASS / FAIL**
- [ ] Laptop (1366x768): **PASS / FAIL**
- [ ] Tablet (768x1024): **PASS / FAIL**
- [ ] Mobile (375x667): **PASS / FAIL**
- [ ] Mobile landscape: **PASS / FAIL**

---

## AFRIHOST DEPLOYMENT CHECKLIST

### Backup
- [ ] Old website backed up completely
- [ ] Backup ZIP downloaded to safe location
- [ ] Backup verified (can extract successfully)
- [ ] Backup file size confirmed (not 0 KB)

### Upload
- [ ] Logged into Afrihost control panel
- [ ] Navigated to /public_html/
- [ ] Old files deleted
- [ ] New files uploaded
- [ ] All files transferred successfully
- [ ] No upload errors

### Permissions
- [ ] All folders set to 755
- [ ] All files set to 644
- [ ] .htaccess set to 644
- [ ] index.html set to 644
- [ ] Permissions applied recursively

### Post-Upload Verification
- [ ] Site URL loads: https://www.plebeiantribunalsa.co.za
- [ ] Homepage displays correctly
- [ ] No 403 Forbidden errors
- [ ] No 404 Not Found errors
- [ ] HTTPS working (SSL certificate active)
- [ ] WWW redirect working (or non-WWW as configured)

---

## POST-DEPLOYMENT TESTING CHECKLIST

### Main Site Testing
- [ ] Homepage loads in under 3 seconds: **PASS / FAIL**
- [ ] All navigation links work: **PASS / FAIL**
- [ ] All sections visible and formatted: **PASS / FAIL**
- [ ] Logo displays correctly: **PASS / FAIL**
- [ ] Footer displays correctly: **PASS / FAIL**
- [ ] Contact email links work: **PASS / FAIL**
- [ ] External GitHub link works: **PASS / FAIL**

### Historical Site Testing
- [ ] /historical/ZARindex.html loads: **PASS / FAIL**
- [ ] Archive notice displays: **PASS / FAIL**
- [ ] Return to Academy link works: **PASS / FAIL**
- [ ] about.html loads: **PASS / FAIL**
- [ ] history.html loads: **PASS / FAIL**
- [ ] basel.html loads: **PASS / FAIL**
- [ ] database.html loads: **PASS / FAIL**
- [ ] research.html loads: **PASS / FAIL**
- [ ] ASSETS/presentation.html loads: **PASS / FAIL**
- [ ] All internal historical links work: **PASS / FAIL**

### Performance Testing
- [ ] PageSpeed Insights score > 80: **PASS / FAIL**
- [ ] Time to First Byte < 1s: **PASS / FAIL**
- [ ] First Contentful Paint < 2s: **PASS / FAIL**
- [ ] Largest Contentful Paint < 3s: **PASS / FAIL**
- [ ] No render-blocking resources: **PASS / FAIL**

### Security Testing
- [ ] HTTPS enforced (.htaccess redirect): **PASS / FAIL**
- [ ] Security headers present: **PASS / FAIL**
- [ ] X-Frame-Options set: **PASS / FAIL**
- [ ] Content-Security-Policy set: **PASS / FAIL**
- [ ] No mixed content warnings: **PASS / FAIL**
- [ ] .htaccess prevents directory listing: **PASS / FAIL**

### SEO Testing
- [ ] robots.txt accessible: **PASS / FAIL**
- [ ] Meta descriptions present: **PASS / FAIL**
- [ ] Page title correct: **PASS / FAIL**
- [ ] Alt text on images: **PASS / FAIL**
- [ ] Semantic HTML structure: **PASS / FAIL**
- [ ] Schema.org markup (optional): **PASS / FAIL**

### PWA Testing (Production)
- [ ] Manifest.json loads via HTTPS: **PASS / FAIL**
- [ ] Service worker registers: **PASS / FAIL**
- [ ] Install prompt appears: **PASS / FAIL**
- [ ] App installs on mobile: **PASS / FAIL**
- [ ] Offline mode functional: **PASS / FAIL**
- [ ] Add to Home Screen works (mobile): **PASS / FAIL**

---

## DEVIN MIRROR DEPLOYMENT CHECKLIST

### Mirror Setup
- [ ] Devin AI static hosting configured
- [ ] All files uploaded to Devin platform
- [ ] Mirror URL generated and accessible
- [ ] Mirror URL documented in audit report

### Mirror Verification
- [ ] Mirror loads independently: **PASS / FAIL**
- [ ] All pages accessible via mirror: **PASS / FAIL**
- [ ] Styles and scripts load: **PASS / FAIL**
- [ ] PWA installs from mirror: **PASS / FAIL**
- [ ] Hash verification works on mirror: **PASS / FAIL**

### Sync Verification
- [ ] Hashes match between Afrihost and Devin: **PASS / FAIL**
- [ ] Content identical between deployments: **PASS / FAIL**
- [ ] Verification endpoint accessible: **PASS / FAIL**

---

## 24-HOUR MONITORING CHECKLIST

### Stability Monitoring
- [ ] Site accessible after 1 hour: **PASS / FAIL**
- [ ] Site accessible after 6 hours: **PASS / FAIL**
- [ ] Site accessible after 12 hours: **PASS / FAIL**
- [ ] Site accessible after 24 hours: **PASS / FAIL**
- [ ] No downtime reported: **PASS / FAIL**

### Error Monitoring
- [ ] Server logs checked: **No errors / Errors found**
- [ ] Browser console checked: **No errors / Errors found**
- [ ] No 404 errors in logs: **PASS / FAIL**
- [ ] No 500 errors in logs: **PASS / FAIL**

### Analytics (if configured)
- [ ] Analytics tracking code works: **PASS / FAIL**
- [ ] Page views recording: **PASS / FAIL**
- [ ] User interactions tracking: **PASS / FAIL**

---

## FINAL SIGN-OFF

### Deployment Summary
**Deployment Date:** ___________________  
**Deployed By:** ___________________  
**Afrihost URL:** https://www.plebeiantribunalsa.co.za  
**Devin Mirror URL:** ___________________  

### Overall Status
- [ ] All tests passed
- [ ] All issues resolved
- [ ] Documentation complete
- [ ] Backup verified
- [ ] Monitoring in place
- [ ] Ready for production

### Critical Items Status
- [ ] Homepage functional
- [ ] Historical site preserved
- [ ] PWA installable
- [ ] Verification system operational
- [ ] No broken links
- [ ] Mobile responsive
- [ ] HTTPS working
- [ ] Devin mirror synced

### Known Issues
Document any unresolved issues:

1. ________________________________________________________________

2. ________________________________________________________________

3. ________________________________________________________________

### Next Steps
- [ ] Announce new site to community
- [ ] Update social media links
- [ ] Submit sitemap to search engines
- [ ] Monitor for first 7 days
- [ ] Gather user feedback
- [ ] Plan future updates

---

## ROLLBACK PLAN

If critical issues arise:

1. [ ] Access Afrihost File Manager
2. [ ] Delete /public_html/ contents
3. [ ] Upload old-site-backup-2025-10-17.zip
4. [ ] Extract backup ZIP
5. [ ] Verify old site restored
6. [ ] Investigate new site issues
7. [ ] Fix issues locally
8. [ ] Re-deploy when ready

---

## APPROVAL SIGNATURES

**Technical Reviewer:** ___________________  
**Date:** ___________________

**Content Reviewer:** ___________________  
**Date:** ___________________  

**Final Approval:** ___________________  
**Date:** ___________________  

---

**Checklist Version:** 1.0.0  
**Last Updated:** October 17, 2025  
**Prepared By:** DEVIN AI for International Plebeian Tribunal Academy  

**NOTES:**  
Use this checklist systematically. Check each item as completed. Document any failures and their resolutions. Keep this checklist with deployment records for future reference.
