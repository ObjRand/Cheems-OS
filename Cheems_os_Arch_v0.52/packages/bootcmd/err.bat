@echo off
cd .. && cd ..
cd moduels && cd MSF
PUSHD sounds && start /min copyerror_1.bat
POPD && start /min MSF_min.bat
exit