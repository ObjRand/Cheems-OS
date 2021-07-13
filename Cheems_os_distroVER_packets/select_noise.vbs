Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "modules\select_noise.bat" & Chr(34), 0
Set WshShell = Nothing