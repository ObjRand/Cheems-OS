Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "select_sine.bat" & Chr(34), 0
Set WshShell = Nothing