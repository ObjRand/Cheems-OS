@echo off
cd ..
cd msf_load
echo true>finish.txt
start /min MSF.bat
cd ..
set /p millieseconds=<delay.txt
for /L %%i in (1,1,%millieseconds%) do ( echo %time% )>nul
echo f | xcopy /K /D /H /Y cur_sound.wav %CD%\MP\cur_sound.wav
cd MP
set "file=cur_sound.wav"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
cscript.exe //nologo sound.vbs
cd ..
cd msf_load
echo false>finish.txt
exit