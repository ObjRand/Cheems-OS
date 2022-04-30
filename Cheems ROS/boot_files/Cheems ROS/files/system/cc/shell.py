import os,time,colorama,sys,shutil

os.system('mode con cols=80 lines=20')
os.system('title Cheems Con.')

user_input = ''
fixed_cd = ''
cur_cd = ''
remove_path = ''
app_cd = ''
scriptlines = []

def init():
    global fixed_cd,cur_cd,remove_path,app_cd,scriptlines

    fixed_cd = os.getcwd()

    cur_cd = os.getcwd()

    os.chdir('..')
    os.chdir('..')

    remove_path = os.getcwd()

    #os.chdir('system')

    app_cd = os.getcwd().replace(remove_path,'C:\\',1)
    app_cd = app_cd[:3] + "" + app_cd[4:]

    #print(app_cd)

    scriptlines = []

def parse(file):
    global scriptlines
    with open(file,'r') as f: scriptlines = f.readlines(); f.close()
    for line in scriptlines:
        line = line.replace('\n','')
        if line == "!exit":
            quit()
        shell(True,parseline=line)
    scriptlines.clear()
    shell(False)

def shell(canParse,parseline=''):
    global app_cd,user_input,cur_cd

    if canParse == False:
        try:
            user_input = input(f"{app_cd}@~>")
        except:
            print("")
            print("Can\'t Copy Nothing. (Keyboard Interupt)")
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
                        os.chdir(user_input)
                        #print(os.getcwd())
                        app_cd = os.getcwd().replace(remove_path,'C:\\',1)
                        app_cd = app_cd[:3] + "" + app_cd[4:]
            except:
                print("Dir does not exist, or can\'t be found")
        elif "run " in user_input[0:4]:
            user_input = user_input.replace("run ","",1)

            try:
                if '\\' in user_input or '/' in user_input:
                    pass
                else:
                    parse(user_input)
            except:
                print("Script error.")
        elif "write" in user_input[0:5]:
            user_input = user_input[6:]
            print(user_input)
        elif "cmd " in user_input[0:4]:
            user_input = user_input[4:]
            if "cd" in user_input:
                pass
            else:
                os.system(user_input)
        elif user_input == "neofetch":
                print(f''' {colorama.Fore.CYAN}██████╗██╗  ██╗███████╗███████╗███╗   ███╗███████╗    ██████╗  ██████╗ ███████╗''')
                time.sleep(0.1)
                print('''██╔════╝██║  ██║██╔════╝██╔════╝████╗ ████║██╔════╝    ██╔══██╗██╔═══██╗██╔════╝
██║     ███████║█████╗  █████╗  ██╔████╔██║███████╗    ██████╔╝██║   ██║███████╗''')
                time.sleep(0.1)
                print('''██║     ██╔══██║██╔══╝  ██╔══╝  ██║╚██╔╝██║╚════██║    ██╔══██╗██║   ██║╚════██║
╚██████╗██║  ██║███████╗███████╗██║ ╚═╝ ██║███████║    ██║  ██║╚██████╔╝███████║''')
                print(f''' ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝    ╚═╝  ╚═╝ ╚═════╝ ╚══════╝{colorama.Style.RESET_ALL}''')
                print('')
                os.chdir('system')

                with open('os.ver') as f: os_ver = f.read(); f.close()

                print(f"    OS VERSION: {os_ver}")
                print('')

                os.chdir('users')

                if os.path.exists('cur_user.dat'):
                    with open('cur_user.dat') as f: cur_user = f.read(); f.close()
                else:
                    print('Not Logged In!')

                print(f"    CUR USER: {cur_user}")
                print('')

                os.chdir('..')
                os.chdir('..')
        elif user_input == "pause":
            os.system('pause')
        elif user_input == "pause-null":
            os.system('pause >nul')
        elif user_input == "reload":
            os.system('cls')
            os.chdir(fixed_cd)
            os.system(f'\"{fixed_cd}\\reboot.bat\"')
            os.chdir(cur_cd)
        elif user_input == "cwd":
            app_cd = os.getcwd().replace(remove_path,'C:\\',1)
            app_cd = app_cd[:3] + "" + app_cd[4:]
            print(os.getcwd())
            #print(app_cd)
        elif user_input == "dir":
            print(next(os.walk('.'))[1])
            #print(remove_path.upper())
        elif user_input == "update":
            os.chdir(fixed_cd)
            os.chdir('..')
            os.chdir('um')
            os.system('python update.py')
            os.chdir(cur_cd)
        elif user_input == "clear":
            os.system('cls')
        elif user_input == "help":
            print('''All Commands:

update - Updates To Newest Version Of Cheems ROS

cd - Change current dir.
pause - Pause Prompt (Waits for any key input to continue).
pause-null - Pause Prompt but its invisible (Waits for any key input to continue).
help - The command you are using right now.
clear - Clears screen.
dir - Show Folders In Cur Dir.
cwd - Shows the current dir.
reload - Reloads the console.
neofetch - Shows System Info.
run - Runs a ccs script.
write - Prints to screen.
cmd - Any Batch Command!
!exit - Exits back to cheems ROS. (Or Just Quits.)
''')
        elif user_input == "!exit":
            quit()
        else:
            if "#" in user_input[0:1]:
                pass
            else:
                print(f"\"{user_input}\" is not a working command!")

    if canParse == False:
        shell(False)

init()
shell(False)
