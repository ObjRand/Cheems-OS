@echo off
set /p comp=<compressed.txt
if %comp% == True goto CompressedWAVS
goto NonCompresssedWAVS

:CompressedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\compressed\error_1.wav error_1.wav
del cur_sound.wav
rename "error_1.wav" "cur_sound.wav"
exit

:NonCompresssedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\not_compressed\error_1.wav error_1.wav
del cur_sound.wav
rename "error_1.wav" "cur_sound.wav"
exit