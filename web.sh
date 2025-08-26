#!/bin/bash
# Unix/Linux Shell Script to launch the Web UI
# Usage: ./web.sh

PYTHON_EXE="python3"
WEB_SCRIPT="$(dirname "$0")/web_app.py"

echo "Starting Agentic Framework Web UI..."
echo "Access the interface at: http://localhost:5000"
$PYTHON_EXE "$WEB_SCRIPT"
