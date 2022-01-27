@echo off
set /p comp=<compressed.txt
if %comp% == True goto CompressedWAVS
goto NonCompresssedWAVS

:CompressedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\compressed\os_hum.wav os_hum.wav
del cur_sound.wav
rename "os_hum.wav" "cur_sound.wav"
exit

:NonCompresssedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\not_compressed\os_hum.wav os_hum.wav
del cur_sound.wav
rename "os_hum.wav" "cur_sound.wav"
exit