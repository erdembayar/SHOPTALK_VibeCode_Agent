@echo off
REM Windows Batch Script for Agentic Framework CLI
REM Usage: agent.bat "your query here"

set PYTHON_EXE=C:/Users/eryondon/AppData/Local/Programs/Python/Python311/python.exe
set CLI_SCRIPT=c:\Users\eryondon\source\repos\SHOPTALK\cli.py

%PYTHON_EXE% "%CLI_SCRIPT%" %*
