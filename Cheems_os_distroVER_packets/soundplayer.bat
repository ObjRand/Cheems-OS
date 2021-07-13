@echo off
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "select_sqw.mp3"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >selectsound.vbs
cls
