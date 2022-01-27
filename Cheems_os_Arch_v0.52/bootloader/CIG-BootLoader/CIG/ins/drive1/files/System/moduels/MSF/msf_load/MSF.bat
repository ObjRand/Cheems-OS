@echo off
title CheemsOSArch/MakeSoundFile
:load
set /p finished=<finish.txt
set /p buffers=<buffers.txt
set /p taskkill=<taskkill.txt
cls
echo Sound Buffer Check 1
ping 127.0.0.1 -n 2 > nul
if %buffers% == 1 goto check1
cls
echo Sound Buffer Check 2
ping 127.0.0.1 -n 2 > nul
if %buffers% == 2 goto check1
cls
echo Sound Buffer Check 3
ping 127.0.0.1 -n 2 > nul
if %buffers% == 3 goto check1
echo exit Code Over 3 >exitcode.txt
if %taskkill% == true goto taskkill /f /im wscripts.exe && exit
exit

:check1
if %finished% == true goto load
cd .. && cd MP
del cur_sound.wav
del sound.vbs
cd .. && cd msf_load
echo buffers done>exitcode.txt
ping 127.0.0.1 -n 1 > nul
exit