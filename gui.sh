#!/bin/bash
# Unix/Linux Shell Script to launch the GUI
# Usage: ./gui.sh

PYTHON_EXE="python3"
GUI_SCRIPT="$(dirname "$0")/gui.py"

echo "Starting Agentic Framework GUI..."
$PYTHON_EXE "$GUI_SCRIPT"
