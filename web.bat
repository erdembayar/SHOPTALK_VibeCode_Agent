@echo off
REM Windows Batch Script to launch the Web UI
REM Usage: web.bat

set PYTHON_EXE=C:/Users/eryondon/AppData/Local/Programs/Python/Python311/python.exe
set WEB_SCRIPT=c:\Users\eryondon\source\repos\SHOPTALK\web_app.py

echo Starting Agentic Framework Web UI...
echo Access the interface at: http://localhost:5000
%PYTHON_EXE% "%WEB_SCRIPT%"
