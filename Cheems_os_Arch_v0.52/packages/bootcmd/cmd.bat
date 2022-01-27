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

:MSFB
REM This took way to much to figure out how to code :(
PUSHD %CD%
setlocal EnableDelayedExpansion

set /p y="Buffers (1-3): "
if !y! == 1 goto MSFB2
if !y! == 2 goto MSFB2
if !y! == 3 goto MSFB2
echo Buffers range is 1 to 3
goto new

:MSFB2
cd .. && cd ..
cd moduels && cd MSF && cd msf_load
echo !y! >buffers.txt
POPD

goto new

:MSFD
REM This took way to much to figure out how to code :(
PUSHD %CD%
setlocal EnableDelayedExpansion

set /p d="Delay (1-500): "
goto MSFD2
echo Delay range is 1 to 500
goto new

:MSFD2
cd .. && cd ..
cd moduels && cd MSF && cd MP
echo !d! >delay.txt
POPD

goto new

:MSFS
PUSHD %CD%

cd .. && cd ..
cd moduels && cd MSF && cd msf_load
set /p tas=<taskill.txt
set /p buf=<buffers.txt
set /p clu=<cleanup.txt
cd .. &&  cd MP
set /p del=<delay.txt
echo TasKill: %tas%
echo Buffers: %buf%
echo Delay: %del%
echo EndCleanUp: %clu%
POPD

goto new





:MSFT
PUSHD %CD%
setlocal EnableDelayedExpansion

set /a wr = None
set /p y="Taskill (T/F) "
if !y! == T set "wr=True"
if !y! == F set "wr=False"
if !y! == t set "wr=True"
if !y! == f set "wr=False"
cd .. && cd ..
cd moduels && cd MSF && cd msf_load
echo !wr! >taskill.txt
POPD

endlocal
goto new

:MSFC
PUSHD %CD%

cd .. && cd ..
cd moduels && cd MSF
if exist sound.wav del sound.wav
if exist error_1.wav del error_1.wav
if exist error_2.wav del error_2.wav
if exist os.wav del os.wav
if exist os_hum.wav del os_hum.wav
if exist cur_sound.wav del cur_sound.wav
if exist oldcd.txt del oldcd.txt
cd MP && if exist sound.vbs del sound.vbs
if exist cur_sound.wav del cur_sound.wav
echo Clean Up Done !!!

POPD

goto new

:MSFE

PUSHD %CD%
setlocal EnableDelayedExpansion

set /a mc = None
set /p s="MSF ENDADD (CLEANUP/NONE) "
if !s! == CLEANUP set "mc=True"
if !s! == NONE set "mc=False"
cd .. && cd ..
cd moduels && cd MSF && cd msf_load
echo !mc! >cleanup.txt
POPD

goto new

:MSFCM

PUSHD %CD%
setlocal EnableDelayedExpansion

set /a r = None
set /p s="MSF COMPRESSED AUDIO (T/F) "
if !s! == T set "r=True"
if !s! == F set "r=False"
if !s! == t set "r=True"
if !s! == f set "r=False"
cd .. && cd ..
cd moduels && cd MSF && cd sounds
echo !r! >compressed.txt
POPD

goto new


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
if %curcmd% == FASTBOOTTRUE goto FBT
if %curcmd% == FASTBOOTFALSE goto FBF
if %curcmd% == FULLRESET goto FR
if %curcmd% == MSFBUFF goto MSFB
if %curcmd% == MSFBUFFER goto MSFB
if %curcmd% == MSFTAS goto MSFT
if %curcmd% == MSFTASKILL goto MSFT
if %curcmd% == MSFTEST start /min err.bat
if %curcmd% == MSFDELAY goto MSFD
if %curcmd% == MSFCLEANUP goto MSFC
if %curcmd% == MSFENDADD goto MSFE
if %curcmd% == MSFS goto MSFS
if %curcmd% == MSFCOMPRESSED goto MSFCM
goto new

:setESC
for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do (
  set ESC=%%b
  exit /B 0
)
exit /B 0