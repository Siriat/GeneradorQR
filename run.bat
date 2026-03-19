@echo off
cd /d "%~dp0"
python -m pip install --user -r requirements.txt
if errorlevel 1 (
    echo Error instalando dependencias.
    pause
    exit /b 1
)
start "" pythonw app.py
