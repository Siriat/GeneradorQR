@echo off
setlocal
cd /d "%~dp0"

echo Instalando dependencias de build...
python -m pip install --user -r requirements.txt
if errorlevel 1 (
    echo Error instalando dependencias.
    pause
    exit /b 1
)

echo Generando ejecutable...
python -m PyInstaller --noconfirm --clean --onefile --windowed --name "GeneradorQR" --icon "assets\icon.ico" --version-file "version_info.txt" --add-data "assets\icon.png;assets" --add-data "assets\icon.ico;assets" app.py
if errorlevel 1 (
    echo Error generando el ejecutable.
    pause
    exit /b 1
)

echo.
echo Listo. El .exe esta en:
echo %~dp0dist\GeneradorQR.exe
pause
