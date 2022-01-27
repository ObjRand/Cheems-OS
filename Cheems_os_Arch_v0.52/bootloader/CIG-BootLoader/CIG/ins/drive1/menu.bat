@echo off
cd files && cd System && set /p col=<mn_col.$ && cd ..
cd System\moduels\KeyDec && start /min run.bat
cd .. && cd MSF\sounds && start copyos_hum.bat && cd ..
start MSF_min.bat && cd .. && cd KeyDec
goto main

:main
cls
setlocal
call :setESC
echo.
echo %ESC%[%col%m Cheems OS Arch v0.3 %ESC%[0m
echo.
echo  [1] Files
echo  [2] Settings
echo  [3] ShutDown
echo.
set /p cur_key=<cur_key.txt
if %cur_key% == '1' goto file_system
if %cur_key% == '2' goto settings
if %cur_key% == '3' goto shutdownc
if %cur_key% == '6' goto deb
ping 127.0.0.1 -n 2 > nul
goto main

:file_system
cls
echo.
echo %ESC%[%col%m FILE MANAGER %ESC%[0m
echo  -------------------------
echo.
echo  FILES/FOLDERS:
echo.
@DIR
echo.
echo  COMMANDS:
echo.
echo  CMD [c]
echo  EXIT [e]
echo.
set /p cur_key=<cur_key.txt
if %cur_key% == 'e' goto main
if %cur_key% == 'c' goto open
ping 127.0.0.1 -n 2 > nul
goto file_system

:open
set /p input="CMD-> "
if %input% == cd goto cdc
if %input% == run goto runf
if %input% == dir @DIR && pause >nul
if %input% == exit goro main

goto file_system

:cdc
set /p cdc="CD-> "
cd %cdc%
goto file_system

:runf
set /p runf="RUN-> "
start %runf%
goto file_system

:settings
cls
echo.
echo %ESC%[%col%m SETTINGS %ESC%[0m
echo  ---------------------
echo.
echo  Main Color [1]
echo.
echo  EXIT [e]
echo.
set /p cur_key=<cur_key.txt
if %cur_key% == 'e' goto main
if %cur_key% == '1' goto cmn_col
ping 127.0.0.1 -n 2 > nul
goto settings

:cmn_col
set /p mn_col="Main-OS-Color-> "
cd .. && cd .. && echo %mn_col%>mn_col.$ && cd moduels\REPLA && start REPLA.py && cd .. && cd .. && set /p col=<mn_col.$ && cd .. && cd Programs && start str_a_shutdown.exe && goto shutdownc
cd System\moduels\KeyDec && start /min run.bat
goto settings

:shutdownc
cls
ping 127.0.0.1 -n 2 > nul
echo none>cur_key.txt
taskkill /f /im pythonw.exe && taskkill /f /im python.exe
taskkill /f /im cmd.exe
exit

:: debug mode
:deb
cls
:debn
set /p cmd="Debug CMD: "
%cmd%
goto debn

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0