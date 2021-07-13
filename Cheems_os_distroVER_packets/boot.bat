@echo off
set "file=buffer.MP3"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
if exist started.vbs goto CDS
echo BIOS (version rel-1.14.0-0-g153433a1330b-prebuilt.qemu.org)
echo.
echo iPXE %DATE% PCI2.10 PnP PMMx088823+34243211 CA00
echo.
echo Booting from Hard Disk
ping localhost -n 2 >nul
cscript.exe //nologo sound.vbs
cls
echo BIOS (version rel-1.14.0-0-g153433a1330b-prebuilt.qemu.org)
echo.
echo iPXE %DATE% PCI2.10 PnP PMMx088823+34243211 CA00
echo.
echo Booting from Hard Disk.
ping localhost -n 2 >nul
cls
echo BIOS (version rel-1.14.0-0-g153433a1330b-prebuilt.qemu.org)
echo.
echo iPXE %DATE% PCI2.10 PnP PMMx088823+34243211 CA00
echo.
echo Booting from Hard Disk..
ping localhost -n 2 >nul
cls
echo BIOS (version rel-1.14.0-0-g153433a1330b-prebuilt.qemu.org)
echo.
echo iPXE %DATE% PCI2.10 PnP PMMx088823+34243211 CA00
echo.
echo Booting from Hard Disk...
ping localhost -n 2 >nul
cls
if exist distro.exe goto startOS
start %CD%\modules\errors\error_distroNull.vbs
start recovery.bat
exit
:startOS
start os.bat
exit

:CDS
cscript.exe //nologo sound.vbs
cls
echo starting from CD
ping localhost -n 2 >nul
cls
echo starting from CD.
ping localhost -n 2 >nul
cls
echo starting from CD..
ping localhost -n 2 >nul
cls
echo starting from CD...
ping localhost -n 2 >nul
cls
echo starting from CD....
ping localhost -n 2 >nul
cls
start os.bat
exit

pause