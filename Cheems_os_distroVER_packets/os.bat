@echo off
if exist distro.exe goto CHEEMSOSDISTROVER
start error.vbs
start recovery.bat
exit

:CHEEMSOSDISTROVER
echo started.vbs>started.vbs
color 0a
title CHEEMS_OS/MS_DOS_distroVER
goto cheemos
:cheemos
echo.
echo.
echo.
echo              CHEEMS OS
echo.             
echo.           
echo.
echo.
set "file=distroOS.MP3"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
cscript.exe //nologo sound.vbs
cls
echo.
echo.
echo.
echo.
echo              CHEEMS OS
echo.           
echo.
echo.
ping localhost -n 1 >nul
del sound.vbs
ping localhost -n 1 >nul
cls
echo.
goto HomePage

:HomePage
if exist %CD%/modules/sound/select_noise.cfg start select_noise.vbs
if exist %CD%/modules/sound/select_sine.cfg start select_sine.vbs
if exist %CD%/modules/sound/select_saw.cfg start select_saw.vbs
if exist %CD%/modules/sound/select_sqw.cfg start select_sqw.vbs
cls
echo This is the Home page
echo CheemsOS_DitroVER
echo.
echo.
echo [1] apps
echo [2] games
echo [3] settings
echo [4] credits
set /p hm=
if %hm% == 1 goto apps
if %hm% == 2 goto game
if %hm% == 3 goto setting
if %hm% == 4 start %CD%/xcins/credits.txt
goto HomePage

:setting
if exist %CD%/modules/sound/select_noise.cfg start select_noise.vbs
if exist %CD%/modules/sound/select_sine.cfg start select_sine.vbs
if exist %CD%/modules/sound/select_saw.cfg start select_saw.vbs
if exist %CD%/modules/sound/select_sqw.cfg start select_sqw.vbs
cls
echo Settings:
echo.
echo [1] Sound
echo.
echo [3] Back
echo.
set /p sm=
if %sm% == 1 goto Soundsettings
if %sm% == 3 goto HomePage
goto setting

:Soundsettings
if exist %CD%/modules/sound/select_noise.cfg start select_noise.vbs
if exist %CD%/modules/sound/select_sine.cfg start select_sine.vbs
if exist %CD%/modules/sound/select_saw.cfg start select_saw.vbs
if exist %CD%/modules/sound/select_sqw.cfg start select_sqw.vbs
cls
echo.
echo selectSFX:
echo.
echo To change the sounds for selecting rename the
echo file: Cheems_os_distroVER_packets\modules\sound\select_sine.cfg
echo to either select_noise.cfg, select_sine.cfg, select_saw.cfg or select_sqw.cfg
echo.
echo [1] Back
echo.
set /p ssm=
if %ssm% == 1 goto setting
goto Soundsettings


goto Soundsettings

:apps
if exist %CD%/modules/sound/select_noise.cfg start select_noise.vbs
if exist %CD%/modules/sound/select_sine.cfg start select_sine.vbs
if exist %CD%/modules/sound/select_saw.cfg start select_saw.vbs
if exist %CD%/modules/sound/select_sqw.cfg start select_sqw.vbs
cls
echo Apps:
echo.
echo [1] Console
echo.
echo [3] Back 
echo.
set /p am=
if %am% == 1 goto crc
if %am% == 3 goto HomePage
    
:crc
cls
echo.
echo CheemsOS-Console
echo.
echo.
set /p input="C:>"
if %input% == reset goto reset
if %input% == classicVER goto classicVER
if %input% == backup goto backup
if %input% == help goto help
if %input% == back goto apps
if %input% == oldkillscreen start %CD%\xcins\Cheems_os_packets\stuffforgame\CheemsOSKillscreen.html

:insd
cls
xcopy /Y %CD%\xcins\distro.exe %CD%\distro.exe

:help
echo.
echo backup
echo reset
echo classicVER 
echo back
echo oldkillscreen 
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
if %input% == back goto apps
if %input% == oldkillscreen start %CD%\xcins\Cheems_os_packets\stuffforgame\CheemsOSKillscreen.html
goto crc

pause