import os,time,colorama,sys

os.system('mode con cols=80 lines=20')
os.system('title ')

user_input = ''
fixed_cd = ''
cur_cd = ''
remove_path = ''
app_cd = ''
scriptlines = []
title_done = False
intigerlimit = 25000
num = -1

def init():
    global fixed_cd,cur_cd,remove_path,app_cd,scriptlines

    fixed_cd = os.getcwd()

    cur_cd = os.getcwd()

    os.chdir('..')
    os.chdir('..')

    remove_path = os.getcwd()

    #os.chdir('system')

    app_cd = os.getcwd().replace(remove_path,'C:\ ',1)
    app_cd = app_cd[:3] + "" + app_cd[4:]

    #print(app_cd)

    scriptlines = []

def parse(file, headers):
    global scriptlines, cur_cd, num, title_done

    commands = ''
    
    for line in file.splitlines():
        line = line.replace('\n','')
        if line == "!exit":
            quit()
        if cur_cd == '':
            cur_cd = 'C:/ '
            if title_done == False:
                commands += '\n' + 'title ' + cur_cd + ' - ' + headers
                title_done = True
        commands += '\n' + shell(True,parseline=line)
        print(commands)
    scriptlines.clear()

    return commands

def shell(canParse,parseline='',title='None'):
    global app_cd,user_input,cur_cd,num,intigerlimit,title_done

    commands = []
    
    if title == 'None':
        title = 'title ' + cur_cd
    else:
        title = 'title ' + title

    if canParse == False:
        try:
            pass
        except:
            pass
            pass
            pass
    else:
        user_input = parseline

    if user_input == "":
        pass
    else:
        if "cd " in user_input[0:3]:
            try:
                user_input = user_input.replace("cd ","",1)
                if app_cd == 'C:\\' and user_input == '..':
                    pass
                else:
                    if '\\' in user_input or '/' in user_input:
                        pass
                    else:
                        pass
                        #print(os.getcwd())
                        pass
                        pass
                
                commands.append("cd " + user_input)
            except:
                pass
        elif "run " in user_input[0:4]:
            pass

            try:
                if '\\' in user_input or '/' in user_input:
                    pass
                else:
                    pass
            except:
                pass
        elif "write" in user_input[0:5]:
            pass
            pass
            commands.append('echo ' + user_input[6:intigerlimit])
        elif "cmd " in user_input[0:4]:
            pass
            commands.append(user_input[4:])
            if "cd" in user_input:
                pass
            else:
                pass
        elif user_input == "neofetch":
                pass
                pass
                pass

                pass
                pass
                pass

                pass

                if os.path.exists('cur_user.dat'):
                    pass
                else:
                    pass

                pass
                pass

                pass
                pass
                commands.append('echo EXC ERROR: Neo Fetch (no batch aquivelent)' + '\n')
        elif user_input == "pause":
            pass
            commands.append('pause' + '\n')
        elif user_input == "pause-null":
            pass
            commands.append('pause >nul' + '\n')
        elif user_input == "reload":
            pass
            pass
            pass
            pass

            commands.append('reboot.bat')
        elif user_input == "cwd":
            pass
            pass
            pass
            #print(app_cd)
            commands.append('echo %CD%' + '\n')
        elif user_input == "dir":
            pass
            #print(remove_path.upper())
            commands.append('echo %CD%' + '\n')
        elif user_input == "clear":
            commands.append('cls')
        elif user_input == "help":
            pass
            commands.append('''echo All Commands:
echo.
echo cd - Change current dir.
echo pause - Pause Prompt (Waits for any key input to continue).
echo pause-null - Pause Prompt but its invisible (Waits for any key input to continue).
echo help - The command you are using right now.
echo clear - Clears screen.
echo dir - Show Folders In Cur Dir.
echo cwd - Shows the current dir.
echo reload - Reloads the console.
echo neofetch - Shows System Info.
echo run - Runs a ccs script.
echo write - Prints to screen.
echo cmd - Any Batch Command!
echo !exit - Exits back to cheems ROS. (Or Just Quits.)
''')
        elif user_input == "!exit":
            pass
        else:
            if "#" in user_input[0:1]:
                pass
            else:
                pass

    if canParse == False:
        shell(False)

    if title_done == True:
        try:
            return commands[num]
        except:
            return '\n'
    else:
        return commands[0]

