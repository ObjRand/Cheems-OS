@echo off
start reset_cmd_settings.bat
cd .. && cd .. && cd installer
start reset_install.bat
cd .. && cd moduels\MSF\MP
del sound.vbs
del cur_sound.mp3
exit