@echo off
set /p comp=<compressed.txt
if %comp% == True goto CompressedWAVS
goto NonCompresssedWAVS

:CompressedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\compressed\audio.wav audio.wav
del cur_sound.wav
rename "audio.wav" "cur_sound.wav"
exit

:NonCompresssedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\not_compressed\audio.wav audio.wav
del cur_sound.wav
rename "audio.wav" "cur_sound.wav"
exit