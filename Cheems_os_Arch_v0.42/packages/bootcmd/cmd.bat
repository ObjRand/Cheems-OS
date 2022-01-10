@echo off
set /p user=<user.txt
set /p root=<root.txt
goto boot

:boot
title CHEEMS_OS/ARCH_ v01/CMD
setlocal
call :setESC
cls
echo.
echo Cheems OS Arch v0.21-CMD-arch1 (ttyq)
echo.           
echo Sign up with the %ESC%[36m'SGU'%ESC%[0m Command (default user: 'rootUSER')
echo.
echo Sorry for the cmd being so slow, this is due to the checks
echo we perform whenever you send a command.
echo.
goto new

:new
set input="nul"
echo nul>command_sent.txt
echo nul>cur_cmd_sent.txt
set /p user=<user.txt
set /p root=<root.txt
set /p root_color=<root_color.txt
set /p input="%ESC%[%root_color%m%root%%ESC%[0m@%user% # "
goto checks

:reset_acc
if %root% == root goto reset_acc2
echo Account is not admin, so therfore this action
echo cannot be performed.
goto new

:reset_acc2
cd acc
echo user>username.txt
echo none>password.txt
cd .. && echo user>user.txt
goto new

:SN
echo.
set /p username="UserName: "
python SGU.py
echo.
cd acc
echo %username%>username.txt
cd ..
echo %username%>user.txt
goto new

:cmd_color
echo.
set /p cmdc_color="cmd-color: "
echo %cmdc_color%>root_color.txt
echo.
goto new

:cig_boot
cd .. && cd .. && cd bootloader\CIG-BootLoader
CIG-Boot.bat
cd .. && cd .. && cd packages && cd bootcmd
goto new

:FBT
set /p q="This is a unfinished feature, are you sure you whant to activate this feature?( Y / N )"
if %q% == Y goto FBTT
if %q% == y goto FBTT
if %q% == N goto new
if %q% == n goto new
goto FTB

:FBTT
echo True>fastboot.txt
goto new

:FBF
echo False>fastboot.txt
goto new

:FR
set /p x="Are you certain you whant to fully reset every setting of the OS? ( Y / N )"
if %x% == Y goto FRT
if %x% == y goto FRT
if %x% == N goto new
if %x% == n goto new
goto FR

:FRT
fullreset.bat
goto new


:checks
echo %input%>command_sent.txt
start command_parser.py
ping 127.0.0.1 -n 2 -w 10> nul
set /p curcmd=<cur_cmd_sent.txt
if %curcmd% == SGU goto SN
if %curcmd% == RESACC goto reset_acc
if %curcmd% == CMDCcolor goto cmd_color
if %curcmd% == CIGBoot goto cig_boot
if %curcmd% == CIGboot goto cig_boot
if %curcmd% == Boot goto cig_boot
if %curcmd% == boot goto cig_boot
if %curcmd% == FastBootTRUE goto FBT
if %curcmd% == FastBootFALSE goto FBF
if %curcmd% == FULLRESET goto FR
goto new

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0