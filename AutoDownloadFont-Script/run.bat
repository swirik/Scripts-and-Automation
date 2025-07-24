@echo off
cd /d "%~dp0"

:: Run the Python script with admin privileges
:: Optional: Check if you want to elevate here using runas or a third-party tool

python install_font_script.py

