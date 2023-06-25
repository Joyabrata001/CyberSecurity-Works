@echo off

:start
echo Starting honeypot...
python HoneypotVariation5.py

:stop
echo Stopping honeypot...
taskkill /F /IM python.exe

:menu
echo Honeypot control menu:
echo 1. Start honeypot
echo 2. Stop honeypot
echo 3. Exit
set /p choice=Enter your choice:

if %choice% == 1 goto start
if %choice% == 2 goto stop
if %choice% == 3 exit
goto menu