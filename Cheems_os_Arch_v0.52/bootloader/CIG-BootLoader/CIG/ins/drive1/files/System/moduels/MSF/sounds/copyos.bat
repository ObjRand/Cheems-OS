@echo off
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\os.wav os.wav
del cur_sound.wav
rename "os.wav" "cur_sound.wav"
exit