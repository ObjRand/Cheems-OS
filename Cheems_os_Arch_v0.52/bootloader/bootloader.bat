@echo off
taskkill /f /im pythonw.exe
taskkill /f /im python.exe
cd ..
cd moduels && cd MSF && cd MP
del cur_sound.wav
del sound.vbs
cd .. && cd sounds
start copyaudio.bat
cd ..
start MSF_min.bat
PUSHD %CD%
cd .. && cd .. && cd packages\bootcmd
set /p fastboot=<fastboot.txt
POPD
cls
ping 127.0.0.1 -n 4 > nul
goto check_machiene
echo error could not check machiene (skipped 'goto check_machiene' command)


:check_machiene
setlocal
call :setESC


REM CHECK 1
:check1
if exist sounds\audio.wav goto check1-1
goto sounds_are_not_ok
:check1-1
if exist not_compressed goto sounds_are_ok
goto sounds_are_not_ok
:sounds_are_ok
echo [ %ESC%[32m OK %ESC%[0m ] Sound Files
goto check2
:sounds_are_not_ok
echo [ %ESC%[31m NOT OK %ESC%[0m ] Sound Files
goto check2


REM CHECK 2
:check2
if %fastboot% == False ping 127.0.0.1 -n 2 > nul
if exist sounds\copyaudio.bat goto check2-1
goto soundcfiles_are_not_ok
:check2-1
if exist sounds\copyos.bat goto soundcfiles_are_ok
goto soundcfiles_are_not_ok
:soundcfiles_are_ok
echo [ %ESC%[32m OK %ESC%[0m ] Sound Files Copier
goto check3
:soundcfiles_are_not_ok
echo [ %ESC%[31m NOT OK %ESC%[0m ] Sound Files Copier
goto check3

REM CHECK 3
:check3
if %fastboot% == False ping 127.0.0.1 -n 2 > nul && cd ..
if exist MSF goto MSF_are_ok
goto MSF_are_not_ok
:MSF_are_ok
echo [ %ESC%[32m OK %ESC%[0m ] Sound Module
goto check4
:MSF_are_not_ok
echo [ %ESC%[31m NOT OK %ESC%[0m ] Sound Module
goto check4

REM CHECK 4
:check4
if %fastboot% == False ping 127.0.0.1 -n 3 > nul
if exist KeyDec goto KeyDetecton_is_ok
goto KeyDetecton_is_not_ok
:KeyDetecton_is_ok
echo [ %ESC%[32m OK %ESC%[0m ] Key Detection Module
goto check5
:KeyDetecton_is_not_ok
echo [ %ESC%[31m NOT OK %ESC%[0m ] Key Detection Module
goto check5

:check5
if %fastboot% == False ping 127.0.0.1 -n 3 > nul
cd .. && cd bootloader
if exist CIG-Bootloader goto CIG_Bootloader_is_ok
goto CIG_Bootloader_is_not_ok
:CIG_Bootloader_is_ok
echo [ %ESC%[32m OK %ESC%[0m ] CIG Bootloader
goto check6
:CIG_Bootloader_is_not_ok
echo [ %ESC%[31m NOT OK %ESC%[0m ] CIG Bootloader
goto check6

:check6
if %fastboot% == False ping 127.0.0.1 -n 2 > nul
if %fastboot% == True ping 127.0.0.1 -n 2 > nul
cd .. && cd packages && cd bootcmd
start cmd.bat
exit

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0