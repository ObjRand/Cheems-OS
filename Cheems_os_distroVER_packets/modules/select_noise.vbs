Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "select_noise.bat" & Chr(34), 0
Set WshShell = Nothing