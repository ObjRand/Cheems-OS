@echo off
title CheemsOSArch/MakeSoundFile
:load
set /p finished=<finish.txt
set /p buffers=<buffers.txt
set /p taskkill=<taskkill.txt
set /p cleanup=<cleanup.txt
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

:CleanUp
cd ..
if exist sound.wav del sound.wav
if exist error_1.wav del error_1.wav
if exist error_2.wav del error_2.wav
if exist os.wav del os.wav
if exist os_hum.wav del os_hum.wav
if exist cur_sound.wav del cur_sound.wav
if exist oldcd.txt del oldcd.txt
cd MP && if exist sound.vbs del sound.vbs
if exist cur_sound.wav del cur_sound.wav
ping 127.0.0.1 -n 1 > nul
exit


:check1
if %finished% == true goto load
cd .. && cd MP
del cur_sound.wav
del sound.vbs
cd .. && cd msf_load
echo buffers done>exitcode.txt
if %cleanup% == True goto CleanUp
ping 127.0.0.1 -n 1 > nul
exit