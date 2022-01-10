@echo off
cd ..
echo f | xcopy /K /D /H /Y %CD%\sounds\audio.wav audio.wav
del cur_sound.wav
rename "audio.wav" "cur_sound.wav"
exit