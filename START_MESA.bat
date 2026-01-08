@echo off
title MESA Launcher
color 0B

echo.
echo  ███╗   ███╗███████╗███████╗ █████╗ 
echo  ████╗ ████║██╔════╝██╔════╝██╔══██╗
echo  ██╔████╔██║█████╗  ███████╗███████║
echo  ██║╚██╔╝██║██╔══╝  ╚════██║██╔══██║
echo  ██║ ╚═╝ ██║███████╗███████║██║  ██║
echo  ╚═╝     ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝
echo.
echo  Multi-Agent Exchange Simulation Architecture
echo  ---------------------------------------------
echo.

REM Get the directory where this batch file is located
set "PROJECT_DIR=%~dp0"

echo Cleaning up any previous sessions...
taskkill /F /IM node.exe >nul 2>&1
taskkill /F /IM python.exe >nul 2>&1
rmdir /s /q "%PROJECT_DIR%frontend\.next" >nul 2>&1
timeout /t 2 /nobreak > nul

echo [1/2] Starting Backend Engine (Port 8000)...
cd /d "%PROJECT_DIR%backend"
start "MESA Backend" cmd /k "venv\Scripts\python.exe main.py"

timeout /t 3 /nobreak > nul

echo [2/2] Starting Frontend Dashboard (Port 3000)...
cd /d "%PROJECT_DIR%frontend"
start "MESA Frontend" cmd /k "npm run dev"

timeout /t 8 /nobreak > nul

echo.
echo  Opening Dashboard in browser...
start "" http://localhost:3000

echo.
echo  ---------------------------------------------
echo  MESA is running!
echo.
echo  Backend:  http://localhost:8000
echo  Frontend: http://localhost:3000
echo.
echo  Keep the terminal windows open.
echo  To stop: Close the Backend and Frontend windows.
echo  ---------------------------------------------
echo.
pause
