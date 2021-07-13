@echo off
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
cls
echo CheemsOS_DitroVER
echo.      
echo.     
echo Press 1 to go to bootloader
set /p st=
if %st% == 1 start boot.bat