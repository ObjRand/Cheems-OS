Set WshShell = CreateObject("WScript.Shell") 
WshShell.Run chr(34) & "select_saw.bat" & Chr(34), 0
Set WshShell = Nothing