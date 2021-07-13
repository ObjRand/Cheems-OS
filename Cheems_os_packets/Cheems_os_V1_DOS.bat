@echo off
color 0a
title CHEEMS_OS/MS_DOS_V1
goto cheemos
:cheemos
echo.
echo.
echo.
echo.
echo              CHEEMS OS
echo.           
echo.
echo.
set "file=os.MP3"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
cscript.exe //nologo sound.vbs
set "file=audio.MP3"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
cscript.exe //nologo sound.vbs
cls
echo.
echo.
echo.
echo.
echo              CHEEMS OS
echo.           
echo.
echo.
ping localhost -n 3 >nul
del sound.vbs
ping localhost -n 3 >nul
cls
echo.
cls
echo %DATE%
echo.      
echo.     
echo Press 1 to start
set /p st=
if %st% == 1 goto start
if %st% == 40987 goto secret
if %st% == 1987 goto man
if not "%st%" EQU "1" (if NOT %st% == 40987 (if not %st% == 1977 (goto startOfBatchFile)))
:man
start purple.txt
set "file=the-man-behind-the-slaughter.mp3"
( echo Set Sound = CreateObject("WMPlayer.OCX.7"^)
  echo Sound.URL = "%file%"
  echo Sound.Controls.play
  echo do while Sound.currentmedia.duration = 0
  echo wscript.sleep 100
  echo loop
  echo wscript.sleep (int(Sound.currentmedia.duration^)+1^)*1000) >sound.vbs
cscript.exe //nologo sound.vbs
ping localhost -n 5 >nul
del sound.vbs
ping localhost -n 3 >nul
goto cheemos
:start
echo Program loading.....
goto load
:secret
echo secret
ping localhost -n 3 >nul
cls
echo Loading
ping localhost -n 2 >nul
cls
echo Loading.
ping localhost -n 2 >nul
cls
echo Loading..
ping localhost -n 2 >nul
cls
echo Loading...
ping localhost -n 2 >nul
cls
echo COMPLETE
ping localhost -n 5 >nul
exit
:load
cls
echo Hello the program loaded
echo Starting the Cheems_OS launcher program...
ping localhost -n 3 >nul
cls
echo Loading
ping localhost -n 2 >nul
cls
echo Loading.
ping localhost -n 2 >nul
cls
echo Loading..
ping localhost -n 2 >nul
cls
echo Loading...
ping localhost -n 2 >nul
cls
echo COMPLETE
ping localhost -n 3 >nul
cls
echo set speech = Wscript.CreateObject("SAPI.spVoice") >> "temp.vbs"
set text=This is Cheems OS.DOS.
echo speech.speak "%text%" >> "temp.vbs"
start temp.vbs
echo This is Cheems OS.DOS.
ping localhost -n 3 >nul
del temp.vbs
cls
color f5
title Cheems_OS_V2
echo.
ping localhost -n 3 >nul
echo Hi, This file has Updated !
ping localhost -n 5 >nul
cls
goto home
:home
cls
echo %DATE%
echo This is the Home page
echo of the CHEEMS_OS
echo.
echo.
echo Press 1 to see the apps
echo Press 2 to see the games
echo Press 3 to go to settings
set /p hm=
if %hm% == 1 goto apps
if %hm% == 2 goto game
if %hm% == 3 goto setting
if not "%hm%" EQU "1" (if NOT %hm% == 2 (if not %hm% == 3 (goto home)))
:apps
title Cheems_OS_V2
color f5
cls
echo These are the apps that are installed.
ping localhost -n 3 >nul
echo.
echo.
echo press 1 for chat room
echo press 2 for update install
echo press 3 for media player
echo press 4 for site selector
echo press 5 to go back
set /p app=
if %app% == 1 goto chatroom 
if %app% == 2 goto installer
if %app% == 3 goto media
if %app% == 4 goto site
if %app% == 5 goto home
if not "%hm%" EQU "1" (if NOT %hm% == 2 (if not %hm% == 3 (goto home)))
:game
echo hi.. 
pause
exit
:setting
echo hi... 
pause
exit
:chatroom
cls
title the_chat_room.exe
echo THE_CHAT_ROOM.EXE
timeout /t 2 /nobreak >nul
echo LOADING...
timeout /t 3 /nobreak >nul
cls
echo CONNECTED! YOU ARE IN READ ONLY MODE, YOU CAN'T CHAT
timeout /t 2 /nobreak >nul
echo Alex: How is everyone doing?
timeout /t 2 /nobreak >nul

echo DS_ADMIN://LOCK_CHAT_FOR_ROLE_GUEST.
timeout /t 2 /nobreak >nul
echo Chat End
pause
cls
goto apps
:installer
:media
:exit
cls
echo Exit?
echo press 1 to Exit.
echo press 2 to go back
set /p ex=
if %ex% == 1 goto apps
if %ex% == 2 goto calc
:site
@echo off
color 0d
title Site Selector
:top
cls
echo ***************************************************************
echo.
echo Site Selector
echo.
echo ***************************************************************
echo.
echo Key: [1] Google - Search Engine
echo [2] Hotmail - Mail Server
echo [3] Yahoo - Search Engine/Mail Server
echo [4] Facebook - Social Networking
echo [5] Myspace - Social Networking
echo [6] CNN - News
echo [7] Weather - Weather
echo [8] WikiHow - A How-To Website
echo [9] Instructables - A How-To Website
echo [10] YouTube - Online Videos
echo [11] Answers - Online Encyclopedia
echo [12] Wikipedia - Online Encyclopedia
echo.
echo [e] Exit
echo.
echo ***************************************************************
echo Enter the number of the website which you would like to go to:
echo.
set /p udefine=
echo.
echo ***************************************************************
if %udefine%==1 start www.google.com
if %udefine%==2 start www.hotmail.com
if %udefine%==3 start www.yahoo.com
if %udefine%==4 start www.facebook.com
if %udefine%==5 start www.myspace.com
if %udefine%==6 start www.cnn.com
if %udefine%==7 start www.weather.com
if %udefine%==7 start www.wikihow.com
if %udefine%==9 start www.instructables.com
if %udefine%==10 start www.youtube.com
if %udefine%==11 start www.answers.com
if %udefine%==12 start www.wikipedia.com
if %udefine%==e goto exit
if not "%udefine%" EQU "1" (if NOT %udefine% == 2 (if not %udefine% == 3 (if not "%udefine%" EQU "4" (if NOT %udefine% == 5 (if not %udefine% == 6 (if not "%udefine%" EQU "7" (if NOT %udefine% == 8 (if not %udefine% == 9 (if not "%udefine%" EQU "10" (if NOT %udefine% == 11 (if not %udefine% == 12 (goto top))))))))))))
:albertIsJustGonnaTypeRandomNumbersFromNowOn
cls
echo ***************************************************************
echo.
echo Thank You for using Site Selector
echo.
echo ***************************************************************
echo Type [e] to exit or [b] to go back and select another site.
echo.
set /p udefine=
echo.
echo ***************************************************************
if %udefine% == b goto top
if %udefine% == e goto exitw
if not %udefine% == b then (if not %udefine% == e then (goto albertIsJustGonnaTypeRandomNumbersFromNowOn))
:exitw
cls
echo ***************************************************************
echo.
echo Thank You for using Site Selector
echo.
echo ***************************************************************
pause
goto exit1
:exit1
cls
color 0a
echo Exit?
echo press 1 to Exit.
echo press 2 to go back to Site.exe
set /p ex1=
if %ex1% == 1 goto apps
if %ex1% == 2 goto site
if not %ex% == 1 then (if not %ex% == 2 then (goto exit1))