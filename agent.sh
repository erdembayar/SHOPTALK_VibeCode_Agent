#!/bin/bash
# Unix/Linux Shell Script for Agentic Framework CLI
# Usage: ./agent.sh "your query here"

PYTHON_EXE="python3"
CLI_SCRIPT="$(dirname "$0")/cli.py"

$PYTHON_EXE "$CLI_SCRIPT" "$@"
