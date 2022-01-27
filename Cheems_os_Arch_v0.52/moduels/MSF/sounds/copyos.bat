@echo off
set /p comp=<compressed.txt
if %comp% == True goto CompressedWAVS
goto NonCompresssedWAVS

:CompressedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\compressed\os.wav os.wav
del cur_sound.wav
rename "os.wav" "cur_sound.wav"
exit

:NonCompresssedWAVS
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\not_compressed\os.wav os.wav
del cur_sound.wav
rename "os.wav" "cur_sound.wav"
exit