@echo off
REM International Plebeian Tribunal Academy - Local Test Script (Windows)
REM This script starts a local web server to test the site before deployment

echo ========================================
echo International Plebeian Tribunal Academy
echo Local Test Server - Windows
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed or not in PATH
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation
    echo.
    pause
    exit /b 1
)

echo Python detected successfully
echo.

REM Get the directory where this script is located
set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

echo Starting local web server...
echo.
echo The site will be available at:
echo   http://localhost:8000
echo   http://127.0.0.1:8000
echo.
echo Press Ctrl+C to stop the server
echo.
echo Opening browser in 3 seconds...
timeout /t 3 /nobreak >nul

REM Open default browser
start http://localhost:8000

REM Start Python HTTP server
python -m http.server 8000

pause
