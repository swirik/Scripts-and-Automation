@echo off
cd /d "%~dp0"
powershell -Command "Start-Process python -ArgumentList 'install_font_script.py' -Verb RunAs"
