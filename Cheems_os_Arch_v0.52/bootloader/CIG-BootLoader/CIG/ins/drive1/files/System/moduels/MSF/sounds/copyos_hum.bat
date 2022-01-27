@echo off
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\os_hum.wav os_hum.wav
del cur_sound.wav
rename "os_hum.wav" "cur_sound.wav"
exit