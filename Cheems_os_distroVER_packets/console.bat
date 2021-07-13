@echo off
:crc
echo.
echo CheemsOS-Console
echo.
echo.
set /p input="C:>"
if %input% == reset goto reset
if %input% == classicVER goto classicVER
if %input% == backup goto backup
if %input% == help goto help

:insd
cls
xcopy /Y %CD%\xcins\distro.exe %CD%\distro.exe

:help
echo.
echo backup
echo reset
echo classicVER 
echo.
goto new

:backup
start backup.bat
goto new

:reset
start reset.bat
goto new

:classicVER
echo installing Cheems_os_V1_DOS.bat 
xcopy %CD%\xcins\Cheems_os_packets C:\Users\%USERNAME%\Desktop\Cheems_os_packets_calssic
ping localhost -n 2 >nul
start C:\Users\user\Desktop\Cheems_os_packets_calssic
exit

:new
set /p input="C:>"
if %input% == reset goto reset
if %input% == classicVER goto classicVER
if %input% == backup goto backup
if %input% == help goto help
pause