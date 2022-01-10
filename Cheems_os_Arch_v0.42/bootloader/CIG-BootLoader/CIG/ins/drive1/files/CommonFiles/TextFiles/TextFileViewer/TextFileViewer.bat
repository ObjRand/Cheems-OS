@echo off && cls
title TextFileViewer 1.0
cd CTX_Parser
echo -===== Text File Viewer =====-
echo.

:new
set /p tfv="TFCMD-> "
if %tfv% == Read goto ChooseFile
if %tfv% == read goto ChooseFile
if %tfv% == Com goto ReadComments
if %tfv% == com goto ReadComments
if %tfv% == dir @DIR
if %tfv% == cd goto changedir

goto new

:ChooseFile
set /p file_tprs="File-> "
cd TextFileViewer && cd CTX_Parser
echo %file_tprs%>file_prs.txt
echo False>show_com.txt
echo.
python ctx_parse.py
pause >nul
exit

:ReadComments
set /p file_trf="File-> "
cd TextFileViewer && cd CTX_Parser
echo %file_trf%>file_prs.txt
echo True>show_com.txt
echo.
python ctx_parse.py
pause >nul
exit

:changedir
set /p cd="ChangeDir-> "
cd %cd%
goto new