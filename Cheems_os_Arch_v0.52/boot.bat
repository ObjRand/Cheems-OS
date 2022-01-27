@echo off
cd installer
set /p installed=<installed.txt
if %installed% == true goto boot
goto install

:install
start installer.bat
exit


:boot
cd ..
title CHEEMS_OS/ARCH_v01
setlocal
call :setESC
cls
echo.
echo.
echo.
echo.
echo              %ESC%[36m Cheems OS Arch %ESC%[0m
echo.           
echo.
echo.
cd moduels && cd MSF && cd sounds
start /min copyos.bat
cd ..
ping 127.0.0.1 -n 2 > nul
start /min MSF_min.bat
cd ..
ping 127.0.0.1 -n 4 > nul
cd KeyDec
start /min run.bat
goto petc

:petc
cls
echo.
echo.
echo.
echo.
echo              %ESC%[36m Cheems OS Arch %ESC%[0m
echo.           
echo        %ESC%[34m  Press Enter To Continue ... %ESC%[0m
echo.
set /p cur_key=<cur_key.txt
if %cur_key% == Key.enter goto bootloader
ping 127.0.0.1 -n 2 > nul
goto petc

:bootloader
echo none >cur_key.txt
cd .. && cd ..
cd bootloader
start st.py
exit
pause >nul

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0