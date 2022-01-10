@echo off
title Cheems_os_Arch_v0.1 Installer
echo -====== Installing Dependancies ======-
echo.
pip install pynput
pip install pwinput
echo true>installed.txt
cd ..
start boot.bat
exit