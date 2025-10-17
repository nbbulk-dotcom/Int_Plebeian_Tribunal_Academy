#!/bin/bash

echo "========================================"
echo "International Plebeian Tribunal Academy"
echo "Local Test Server - Unix/Mac/Linux"
echo "========================================"
echo ""

if ! command -v python3 &> /dev/null && ! command -v python &> /dev/null; then
    echo "ERROR: Python is not installed"
    echo ""
    echo "Please install Python:"
    echo "  Mac: brew install python3"
    echo "  Ubuntu/Debian: sudo apt-get install python3"
    echo "  Fedora: sudo dnf install python3"
    echo ""
    exit 1
fi

echo "Python detected successfully"
echo ""

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd "$SCRIPT_DIR"

echo "Starting local web server..."
echo ""
echo "The site will be available at:"
echo "  http://localhost:8000"
echo "  http://127.0.0.1:8000"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""
echo "Opening browser in 3 seconds..."
sleep 3

if command -v xdg-open &> /dev/null; then
    xdg-open http://localhost:8000 &> /dev/null &
elif command -v open &> /dev/null; then
    open http://localhost:8000 &> /dev/null &
fi

if command -v python3 &> /dev/null; then
    python3 -m http.server 8000
else
    python -m http.server 8000
fi
