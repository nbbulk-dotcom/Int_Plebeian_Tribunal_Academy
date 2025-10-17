# 📦 Afrihost Upload Guide - Foolproof "Monkey See, Monkey Do" Instructions

**International Plebeian Tribunal Academy Website Deployment**

This guide provides ultra-simple, step-by-step instructions for uploading the new Academy website to Afrihost hosting. Follow each step exactly as written. Each step includes checkboxes for verification.

---

## 🎯 Quick Overview

- **Total Time:** Approximately 40 minutes
- **Difficulty:** Easy (no technical knowledge required)
- **Requirements:** Computer with internet, Afrihost account credentials
- **Result:** New Academy website live at https://www.plebeiantribunalsa.co.za

---

## 📋 Pre-Flight Checklist

Before starting, ensure you have:

- [ ] Downloaded `academy-website-full.zip` to your computer
- [ ] Afrihost login credentials (username and password)
- [ ] Stable internet connection
- [ ] 30-40 minutes of uninterrupted time

---

## STEP 1: Download and Extract Files (5 minutes)

### 1.1 Download the ZIP File
- [ ] Open your email or message containing the download link
- [ ] Click the download link for `academy-website-full.zip`
- [ ] Save file to your **Desktop** folder
- [ ] Wait for download to complete (file size approximately 5-10 MB)

### 1.2 Extract the ZIP File

**FOR WINDOWS:**
- [ ] Right-click on `academy-website-full.zip` on your Desktop
- [ ] Click "Extract All..."
- [ ] Click "Extract" button
- [ ] A new folder called `academy-website-full` will appear

**FOR MAC:**
- [ ] Double-click `academy-website-full.zip` on your Desktop
- [ ] A folder called `academy-website-full` will appear automatically

### 1.3 Verify Files
- [ ] Open the `academy-website-full` folder
- [ ] You should see files including:
  - [ ] `index.html`
  - [ ] `manifest.json`
  - [ ] `robots.txt`
  - [ ] Folders: `css`, `js`, `images`, `historical`, etc.

**⚠️ STOP HERE if you don't see these files. Contact support.**

---

## STEP 2: Login to Afrihost (2 minutes)

### 2.1 Access Afrihost Control Panel
- [ ] Open your web browser (Chrome, Firefox, Safari, etc.)
- [ ] Go to: https://www.afrihost.com
- [ ] Click "MyAfrihost" or "Login" button (top right corner)
- [ ] Enter your username
- [ ] Enter your password
- [ ] Click "Login" or "Sign In"

### 2.2 Navigate to File Manager
- [ ] Look for "Control Panel" or "cPanel" button
- [ ] Click on "File Manager" icon or link
- [ ] Wait for File Manager to load

**Visual Check:** You should now see a file browser interface showing folders.

---

## STEP 3: Backup Old Website (10 minutes)

**⚠️ CRITICAL: Do not skip this step! This preserves your old website.**

### 3.1 Select All Current Files
- [ ] In File Manager, navigate to `/public_html/` folder
- [ ] Click to open `/public_html/`
- [ ] Click "Select All" button (or Ctrl+A on Windows, Cmd+A on Mac)
- [ ] All files should now be highlighted

### 3.2 Download Backup
- [ ] Click "Compress" or "Zip" button at the top
- [ ] Name the file: `old-site-backup-2025-10-17.zip`
- [ ] Click "Compress" or "OK"
- [ ] Wait for compression to complete (progress bar will show)
- [ ] Click "Download" button
- [ ] Save to your Desktop
- [ ] Wait for download to complete

### 3.3 Verify Backup Downloaded
- [ ] Check your Desktop for `old-site-backup-2025-10-17.zip`
- [ ] File should be several MB in size (not 0 KB)

**✅ CHECKPOINT: You have successfully backed up your old website!**

---

## STEP 4: Delete Old Files (5 minutes)

### 4.1 Clear Public HTML Folder
- [ ] In File Manager, make sure you're in `/public_html/`
- [ ] Click "Select All" again
- [ ] Look for "Delete" or trash can icon button
- [ ] Click "Delete"
- [ ] Confirm deletion when prompted
- [ ] Wait for deletion to complete

### 4.2 Verify Folder is Empty
- [ ] The `/public_html/` folder should now be empty
- [ ] You should see: "This folder is empty" or no files listed

**⚠️ If you see an error, try refreshing the page and repeat.**

---

## STEP 5: Upload New Website Files (15 minutes)

### 5.1 Upload Method A: ZIP Upload (Recommended)

**Step 5.1.1: Upload ZIP File**
- [ ] In File Manager, click "Upload" button
- [ ] Click "Select File" or drag-and-drop zone
- [ ] Navigate to Desktop → `academy-website-full` folder
- [ ] Select ALL files inside the folder (index.html, css folder, js folder, etc.)
- [ ] Click "Open" or "Upload"
- [ ] Wait for upload progress bar to reach 100%
- [ ] Click "Close" or "Back to File Manager"

**Alternative: If your File Manager supports ZIP uploads:**
- [ ] Create a ZIP of the contents of `academy-website-full` folder
- [ ] Upload this ZIP to `/public_html/`
- [ ] Right-click the ZIP file → "Extract"
- [ ] Delete the ZIP file after extraction

### 5.2 Verify All Files Uploaded
In `/public_html/`, you should now see:
- [ ] `index.html`
- [ ] `manifest.json`
- [ ] `robots.txt`
- [ ] `.htaccess`
- [ ] `service-worker.js`
- [ ] Folders: `css`, `js`, `images`, `fonts`, `historical`, `build`

**⚠️ If any files are missing, re-upload them individually.**

---

## STEP 6: Set File Permissions (3 minutes)

### 6.1 Set Folder Permissions to 755
- [ ] Select ALL folders (css, js, images, fonts, historical, build)
- [ ] Right-click → "Permissions" or "Change Permissions"
- [ ] Enter: `755`
- [ ] Check "Apply to all subfolders"
- [ ] Click "OK" or "Apply"

### 6.2 Set File Permissions to 644
- [ ] Select ALL files (index.html, manifest.json, robots.txt, .htaccess, etc.)
- [ ] Right-click → "Permissions" or "Change Permissions"
- [ ] Enter: `644`
- [ ] Click "OK" or "Apply"

**Permissions Table for Reference:**
| Item Type | Permission | What It Means |
|-----------|------------|---------------|
| Folders | 755 | Owner: read/write/execute, Others: read/execute |
| Files | 644 | Owner: read/write, Others: read only |

---

## STEP 7: Test the Website (5 minutes)

### 7.1 Visit Your Website
- [ ] Open a NEW browser tab
- [ ] Go to: https://www.plebeiantribunalsa.co.za
- [ ] Press Ctrl+Shift+R (Windows) or Cmd+Shift+R (Mac) to hard refresh

### 7.2 Visual Verification Checklist
Does the homepage show:
- [ ] Blue header with "International Plebeian Tribunal Academy" title?
- [ ] Navigation menu with links (Home, About, Curriculum, etc.)?
- [ ] Hero section with "Immutable Genesis Node" heading?
- [ ] System Overview section with architecture cards?
- [ ] Footer at the bottom?

### 7.3 Test Navigation Links
Click each link and verify it loads:
- [ ] Home (should scroll to top)
- [ ] About (should scroll to section)
- [ ] Curriculum (should scroll to documents)
- [ ] Verification (should scroll to hash table)
- [ ] Blockchain (should scroll to blockchain section)
- [ ] South Africa Origins → Should load historical ZA site

### 7.4 Test Historical Site
- [ ] Click "South Africa Origins" link
- [ ] Should load `/historical/ZARindex.html`
- [ ] Yellow archive notice should be visible
- [ ] Historical navigation should work

### 7.5 Test PWA Installation (Optional)
- [ ] On Chrome/Edge: Look for install icon in address bar
- [ ] Click install icon
- [ ] Click "Install" button
- [ ] App should open in standalone window

---

## STEP 8: Advanced Testing (Optional - 5 minutes)

### 8.1 Mobile Test
- [ ] Open site on your phone
- [ ] Check that layout is responsive
- [ ] Menu should work on mobile

### 8.2 Offline Test
- [ ] Install PWA (Step 7.5)
- [ ] Disconnect from internet
- [ ] Reload page
- [ ] Yellow "Offline Mode" banner should appear
- [ ] Site should still load

### 8.3 Hash Verification Test
- [ ] Scroll to "Verification Hashes" section
- [ ] Click "Run Verification" button
- [ ] Should see "Verifying..." then "✓ Verified"
- [ ] Alert: "All hashes verified successfully"

---

## ✅ FINAL CHECKLIST

Before you finish, verify:
- [ ] Old website backed up to Desktop
- [ ] New website live at https://www.plebeiantribunalsa.co.za
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Historical site accessible at /historical/ZARindex.html
- [ ] No error messages visible
- [ ] Site works on desktop AND mobile

---

## 🎉 SUCCESS!

**Congratulations!** Your new International Plebeian Tribunal Academy website is now live!

**What's Next:**
1. Monitor the site for 24 hours to ensure stability
2. Share the new URL with your community
3. Test all features and report any issues
4. Explore the Devin AI mirror for redundancy

---

## ❓ TROUBLESHOOTING

### Problem: "This site can't be reached"
**Solution:** 
- Wait 5-10 minutes for DNS propagation
- Clear browser cache (Ctrl+Shift+Delete)
- Try accessing from a different device

### Problem: "403 Forbidden Error"
**Solution:**
- Check file permissions (Step 6)
- Ensure `.htaccess` file is present
- Verify `/public_html/` is the correct folder

### Problem: "Page not found" for historical site
**Solution:**
- Verify `/historical/` folder exists
- Check that `ZARindex.html` is inside `/historical/`
- Check file permissions on historical folder (should be 755)

### Problem: Styles not loading (plain HTML only)
**Solution:**
- Verify `/css/` folder uploaded correctly
- Check `/css/main.css` exists
- Clear browser cache and hard refresh

### Problem: Can't log in to Afrihost
**Solution:**
- Reset password at https://www.afrihost.com
- Contact Afrihost support: support@afrihost.com
- Have your account number ready

---

## 📞 SUPPORT CONTACTS

**Afrihost Technical Support:**
- Email: support@afrihost.com
- Phone: 087 943 7678
- Website: https://www.afrihost.com/support

**Academy Technical Contact:**
- Email: contact@plebeiantribunalsa.co.za

---

## 📝 NOTES

**Date Deployed:** ________________

**Deployed By:** ________________

**Any Issues Encountered:** 

_____________________________________________

_____________________________________________

_____________________________________________

**Resolution:**

_____________________________________________

_____________________________________________

_____________________________________________

---

**Document Version:** 1.0  
**Last Updated:** October 17, 2025  
**Prepared by:** DEVIN AI for International Plebeian Tribunal Academy
