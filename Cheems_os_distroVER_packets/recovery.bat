@echo off
color 04
:crc
echo.
echo CheemsOS-Recovery-Console
echo.
echo.
set /p input="C:>"
if %input% == reset goto reset
if %input% == installdistro goto insd
if %input% == help goto help
if %input% == boot goto boot
if %input% == loadbackup goto backupcheck

:insd
cls
pushd "%CD% xcins distro.exe"
xcopy %CD%\xcins\distro.exe %CD%\distro.exe /s /y
goto new

:help
echo.
echo installdistro
echo loadbackup
echo boot
echo reset
echo.
goto new

:backupcheck
IF exist Cheems_os_distroVER_packets goto backupfound
goto backupNull


:backupNull
echo No available backup
start %CD%\modules\errors\error_backupNull.vbs
goto new

:backupfound
echo Backup Found!
echo.
echo [1] Backup
echo.
set /p backupinput="Backup:>"
if %backupinput% == 1 start %CD%\Cheems_os_distroVER_packets\backup1\Cheems_os_distroVER_packets\boot.bat
goto new

:boot
start boot.bat
exit

:reset
start reset.bat
goto new

:new
set /p input="C:>"
if %input% == reset goto reset
if %input% == installdistro goto insd
if %input% == help goto help
if %input% == boot goto boot
if %input% == loadbackup goto backupcheck
pause