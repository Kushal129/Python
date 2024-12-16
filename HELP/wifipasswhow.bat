@echo off
echo Enter Wi-Fi name:
set /p wifiname=
netsh wlan show profiles "%wifiname%" key=clear
pause
