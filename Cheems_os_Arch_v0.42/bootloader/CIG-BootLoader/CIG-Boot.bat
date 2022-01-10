@echo off
title CIG Boot
echo %CD%>cd.txt && set /p oldcd=<cd.txt
cd CIG && set /p ins=<BOOT && cd ..
goto q1

:q1
echo.
set /p qo="Do you want to use an existing drive to install the OS on? ( Y / N ) "
if %qo% == Y goto UseExistingDrive
if %qo% == N goto MkDrive
if %qo% == y goto UseExistingDrive
if %qo% == n goto MkDrive
goto q1

:MkDrive
cls
echo Making Drive...
cd %oldcd% && echo d | xcopy /E /C /I /Q /G /H /R /K /Y /Z /J CIG\ins\drive1 drive1
cd .. && cd .. && move bootloader\CIG-BootLoader\drive1 drive1
cd drive1 && ins.bat
pause >nul
exit

:UseExistingDrive
cls
SetLocal EnableDelayedExpansion
set /p osname=<osname.cig
Set "i=0"&For /F "Delims==" %%# In ('Set # 2^>NUL')Do @Set "%%#="
For /F %%# In ('MountVol^|Find ":\"')Do (Set /A i+=1
    Set "#!i!=%%~d#"&Echo Drive !i!: %%~d#)
:Ask
Echo(&Set /P "Drive=Choose a drive to install %osname% on "
Set #|Findstr "^#%Drive%=">Nul||GoTo :Ask
Set "Drive=!#%Drive%!"
echo.
cd %Drive%
cd %oldcd% && echo d | xcopy /E /C /I /Q /G /H /R /K /Y /Z /J  CIG\ins\drive1 %Drive%\%osname%
cd /D %Drive%\ && cd %osname%
echo Finished downloading boot file
echo.
ins.bat
echo.
EndLocal
pause >nul
exit