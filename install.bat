@echo off
set "PATH=C:\Program Files\nodejs;%PATH%"
cd /d "D:\proramming project\Estidamah\Estidamah"
call npm install --no-audit --no-fund
echo EXIT_CODE=%ERRORLEVEL%
