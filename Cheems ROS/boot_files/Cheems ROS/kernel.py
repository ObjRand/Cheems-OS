from os_funcs import *
import os,random,time,playsound
import pyperclip, sys
from colorama import Fore, Back, Style

os.chdir('files')
os.chdir('system')
os.chdir('exc')

sys.path.insert(1, os.getcwd())

from decompiler import *

os.system('title Cheems ROS')

os.chdir('..')
os.chdir('..')

logged_in = False
startedup = False
username_globalvar = ''
username = ''
password = ''
apps_path = os.getcwd() + '\\apps'
start_at = apps_path

def purple_man():
    os.system('mode con cols=100 lines=65')
    os.system('title THE MAN BEHIND THE SLAUGTER.')
    print(f'''
{Fore.BLACK}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Style.RESET_ALL}{Fore.MAGENTA}████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNm{Fore.MAGENTA}█████████████████{Style.RESET_ALL}{Fore.BLACK}mmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}█████████████████████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}█████████████████████{Style.RESET_ALL}{Fore.BLACK}mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}█████████████████████{Style.RESET_ALL}{Fore.BLACK}mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}█████████████████████{Style.RESET_ALL}{Fore.BLACK}mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMm{Fore.MAGENTA}███{Fore.WHITE}██{Style.RESET_ALL}{Fore.MAGENTA}   ████{Fore.WHITE}██{Style.RESET_ALL}{Fore.MAGENTA}   ████{Style.RESET_ALL}{Fore.BLACK}mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}███{Fore.WHITE}██{Style.RESET_ALL}{Fore.MAGENTA}  █████{Fore.WHITE}██{Style.RESET_ALL}{Fore.MAGENTA}  █████{Style.RESET_ALL}{Fore.BLACK}mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}█████████████████████{Style.RESET_ALL}{Fore.BLACK}mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██               ██████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████            ████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████            ████████{Style.RESET_ALL}{Fore.BLACK}mmmNMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}███            ██████████{Style.RESET_ALL}{Fore.BLACK}+mMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████████{Style.RESET_ALL}{Fore.BLACK}m{Fore.MAGENTA}█████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}██████████████{Style.RESET_ALL}{Fore.BLACK}NNN{Fore.MAGENTA}███████████████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNo{Fore.MAGENTA}███████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}██████████████████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}███████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}███{Fore.YELLOW}██████{Style.RESET_ALL}{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNm{Fore.MAGENTA}████{Fore.YELLOW}████{Style.RESET_ALL}{Fore.MAGENTA}███████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh{Fore.MAGENTA}██████████{Fore.YELLOW}████{Style.RESET_ALL}{Fore.MAGENTA}███████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh{Fore.MAGENTA}█████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMh{Fore.MAGENTA}█████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNN{Fore.MAGENTA}█████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMMMMMMMh{Fore.MAGENTA}█████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMNNNNNhhhhhs{Fore.MAGENTA}█████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNN{Fore.MAGENTA}████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMM{Fore.MAGENTA}█████████████████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMMNNNNNNNNMMMNNNNN{Fore.MAGENTA}███████████{Style.RESET_ALL}{Fore.BLACK}NNNNNNNN{Fore.MAGENTA}█████████████████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMM{Fore.MAGENTA}████████████████████████████████████████████████████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMM{Fore.MAGENTA}██████████████████████████████████████████████████{Style.RESET_ALL}{Fore.BLACK}MMN{Fore.MAGENTA}███████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMM
MMMMMMMMMMMMMM{Fore.MAGENTA}██████████████████{Style.RESET_ALL}{Fore.BLACK}NN{Fore.MAGENTA}█████████████████████████████{Style.RESET_ALL}{Fore.BLACK}NMMN{Fore.MAGENTA}██████████████████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}███████{Style.RESET_ALL}{Fore.BLACK}MMMMMMNN{Fore.MAGENTA}███████████████████████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMN{Fore.MAGENTA}████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN{Fore.MAGENTA}███████████████{Style.RESET_ALL}{Fore.BLACK}NMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNNNNNNNM{Fore.MAGENTA}██████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Fore.MAGENTA}████████████████████{Style.RESET_ALL}{Fore.BLACK}MMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM{Style.RESET_ALL}''')
    with open('media\\fedy.txt') as pf: fedy = pf.read();pf.close;pyperclip.copy(fedy)
    playsound.playsound('media/sounds/tmbts.mp3')
    startup_page()

def check_cur_user():
    global username_globalvar
    if os.path.exists('system/users/cur_user.dat'):
        logged_in = True
    else:
        logged_in = False

    if logged_in == True:
        with open('system/users/cur_user.dat','r') as cur_user:
            username_globalvar = cur_user.read()
            cur_user.close()
        play_sound('os_enter_menu.mp3')
        os_page()
    else:
        pass

def os_input(tag = 'user'):
    theinput = input(f"{Fore.RED}{tag}{Style.RESET_ALL}@~>")
    return theinput

def signup():
    global username_globalvar

    os.system('cls')
    print('-------------------------------------------------')
    print("|                    Sign Up.                   |")
    print('-------------------------------------------------\n')
    username = input('username: ')

    exit_command(username,startup_page)

    print('\n!WARNING THE PASSWORD IS SAVED WITH NO SPACES!\n')
    password = input('password: ').replace(" ", "")

    exit_command(password,startup_page)

    if os.path.exists(f'system/users/{username}'):
        os.system('cls')
        print('This User Already Exists! (LOGIN!)')
        os.system('pause')
        signup()
    else:
        os.mkdir(f'system/users/{username}')

    with open(f'system/users/{username}/username.txt','w') as user:
        user.write(username)
        user.close()

    with open('system/users/cur_user.dat','w') as cur_user:
        cur_user.write(username)
        cur_user.close()

    with open(f'system/users/{username}/password.txt','w') as passw:
        passw.write(password)
        passw.close()

    username_globalvar = username

    play_sound('os_sign_up.mp3')

    os_page()

def login():
    global username_globalvar
    os.system('cls')

    print('-------------------------------------------------')
    print("|                     Login.                    |")
    print('-------------------------------------------------\n')

    if os.listdir('system/users') == []:
        os.system('cls')
        print('NO USERS ARE LOGGED IN!')
        os.system('pause')
        startup_page()
    else:
        for x in os.listdir('system/users'):
            print('- ' + x)
            print('')

    username = input('Login as: ')

    exit_command(username,startup_page)

    print('\n!WARNING THE PASSWORD IS SAVED WITH NO SPACES!\n')
    password_checkvar = input('Your password: ').replace(" ", "")

    exit_command(password_checkvar,startup_page)

    with open(f'system/users/{username}/username.txt','r') as logincheckuser:
        logincheck_user = logincheckuser.read()
        logincheckuser.close()

    if os.path.exists(f'system/users/{username}') and logincheck_user == username:
        username_globalvar = username
    else:
        os.system('cls')
        print(f'User "{username}" Is Non-Existant!')
        os.system('pause')
        login()

    with open(f'system/users/{username}/password.txt','r') as passw:
        password = passw.read()
        passw.close()

    if password_checkvar == password:
        with open('system/users/cur_user.dat','w') as cur_user:
            cur_user.write(username)
            cur_user.close()

        play_sound('os_login.mp3')

        os_page()
    else:
        os.system('cls')
        print('Wrong Password!')
        os.system('pause')
        login()
        
def startup_page():
    os.system('mode con cols=50 lines=20')
    os.system('title Cheems ROS')
    os.system('cls')
    check_cur_user()
    print('-------------------------------------------------')
    print("|                  Start Page.                  |")
    print('-------------------------------------------------\n')
    print("Welcome To The Start Page!\n")
    print("What Would you Like To Do?\n")
    print("1) Sign up.")
    print("2) Login.")
    print("3) Exit.\n")
    startup_option = os_input()
    if startup_option == '1':
        signup()
    if startup_option == '2':
        login()
    if startup_option == '3':
        quit()
    if startup_option == '1987':
        purple_man()
    else:
        os.system('cls')
        print(f'\'{startup_option}\' is Not An Option!')
        os.system('pause')
        startup_page()

def apps():
    os.system('mode con cols=50 lines=20')
    global username_globalvar, start_at, apps_path
    os.system('cls')
    print('-------------------------------------------------')
    print("|                      Apps                     |")
    print('-------------------------------------------------\n')

    os.chdir(start_at)

    with open('tree.dat') as f: tree = f.readlines(); f.close()
    
    for x in range(int(tree[0].replace('$', ''))):

        l = tree[x + 1]

        pos = max(l.find('='), l.find('='), 0)
        pos = l[pos:].strip().replace('=', '')

        nm = str(l.replace(pos, '').replace('=', '').replace('\n', ''))


        if '_$FLDR' in nm:

            nm = nm.replace('_$FLDR', '')
            os.chdir(nm)

            with open('folder.id') as f: id = f.readlines(); f.close()

            print(pos + ' - ' + id[0])

            os.chdir('..')

        else:
            os.chdir(nm)

            with open('app.id') as f: id = f.readlines(); f.close()

            print(pos + ') ' + id[0])

            os.chdir('..')

    if start_at == apps_path:
        print('\n' + str(int(pos) + 1) + ') Exit')
    else:
        with open('tree.dat') as f: tree = f.readlines(); f.close()

        if tree[0] == '$0':
            print('\n' + '1' + ') Back')
        else:
            print('\n' + str(int(pos) + 1) + ') Back')
    print('')

    apps_page_input = os_input(username_globalvar)

    if start_at != apps_path:
        if tree[0] == '$0':
            if apps_page_input == '1':
                os.chdir('..')
                start_at = os.getcwd()
        else:
            if apps_page_input == str(int(pos) + 1):
                os.chdir('..')
                start_at = os.getcwd()
            else:
                if apps_page_input == str(int(pos) + 1):
                    os.chdir('..')
                    os_page()    
                if apps_page_input == "":
                    pass
                else:
                    if apps_page_input[0:5] == "desc ":
                        apps_page_input = apps_page_input.replace("desc ", "")
                        for line in tree:
                            if '=' + apps_page_input in line and '_$FLDR' not in line:
                                print('TreeData : ' + line.replace('\n', ''))

                                position = max(line.find('='), line.find('='), 0)
                                position = line[position:].strip().replace('=', '')

                                print('Position : ' + position)

                                fldr = str(line.replace(position, '').replace('=', '').replace('\n', ''))

                                print('Folder : ' + fldr)

                                os.chdir(fldr)
                                with open('app.id') as f: id = f.readlines(); f.close()

                                print('Identification : ' + id[0])
                            if '=' + apps_page_input in line and '_$FLDR' in line:
                                print('TreeData : ' + line.replace('\n', ''))

                                position = max(line.find('='), line.find('='), 0)
                                position = line[position:].strip().replace('=', '')

                                print('Position : ' + position)

                                fldr = str(line.replace(position, '').replace('=', '').replace('\n', '').replace('_$FLDR', ''))

                                print('Folder : ' + fldr)

                                os.chdir(fldr)
                                with open('folder.id') as f: id = f.readlines(); f.close()

                                print('Identification : ' + id[0])
                        os.system('pause >nul')
                    else:
                        for line in tree:
                            if '=' + apps_page_input in line and '_$FLDR' not in line:
                                position = max(line.find('='), line.find('='), 0)
                                position = line[position:].strip().replace('=', '')
                                fldr = str(line.replace(position, '').replace('=', '').replace('\n', ''))
                                os.chdir(fldr)
                                decompile('_index.exc') # now RUNNING .exc FILES :)
                                os.chdir('..')
                            if '=' + apps_page_input in line and '_$FLDR' in line:
                                position = max(line.find('='), line.find('='), 0)
                                position = line[position:].strip().replace('=', '')
                                fldr = str(line.replace(position, '').replace('=', '').replace('\n', '').replace('_$FLDR', ''))
                                start_at = os.getcwd() + '\\' + fldr
    else:
        if apps_page_input == str(int(pos) + 1):
            os.chdir('..')
            os_page()    
        if apps_page_input == "":
            pass
        else:
            if apps_page_input[0:5] == "desc ":
                apps_page_input = apps_page_input.replace("desc ", "")
                for line in tree:
                    if '=' + apps_page_input in line and '_$FLDR' not in line:
                        print('TreeData : ' + line.replace('\n', ''))

                        position = max(line.find('='), line.find('='), 0)
                        position = line[position:].strip().replace('=', '')

                        print('Position : ' + position)

                        fldr = str(line.replace(position, '').replace('=', '').replace('\n', ''))

                        print('Folder : ' + fldr)

                        os.chdir(fldr)
                        with open('app.id') as f: id = f.readlines(); f.close()

                        print('Identification : ' + id[0])
                    if '=' + apps_page_input in line and '_$FLDR' in line:
                        print('TreeData : ' + line.replace('\n', ''))

                        position = max(line.find('='), line.find('='), 0)
                        position = line[position:].strip().replace('=', '')

                        print('Position : ' + position)

                        fldr = str(line.replace(position, '').replace('=', '').replace('\n', '').replace('_$FLDR', ''))

                        print('Folder : ' + fldr)

                        os.chdir(fldr)
                        with open('folder.id') as f: id = f.readlines(); f.close()

                        print('Identification : ' + id[0])
                os.system('pause >nul')
            else:
                for line in tree:
                    if '=' + apps_page_input in line and '_$FLDR' not in line:
                        position = max(line.find('='), line.find('='), 0)
                        position = line[position:].strip().replace('=', '')
                        fldr = str(line.replace(position, '').replace('=', '').replace('\n', ''))
                        os.chdir(fldr)
                        decompile('_index.exc') # now RUNNING .exc FILES :)
                        os.chdir('..')
                    if '=' + apps_page_input in line and '_$FLDR' in line:
                        position = max(line.find('='), line.find('='), 0)
                        position = line[position:].strip().replace('=', '')
                        fldr = str(line.replace(position, '').replace('=', '').replace('\n', '').replace('_$FLDR', ''))
                        start_at = os.getcwd() + '\\' + fldr

    apps()

def os_page():
    os.system('mode con cols=50 lines=20')
    global username_globalvar

    os.system('cls')
    print('-------------------------------------------------')
    print("|                    OS Page.                   |")
    print('-------------------------------------------------\n')
    print("Welcome To The OS Page!\n")
    print("What Would you Like To Do?\n")
    print("1) CheemCon.")
    print("2) Apps")
    print("3) Settings.\n")
    os_page_option = os_input(username_globalvar)
    if os_page_option == '1':
        os.chdir('system')
        os.chdir('cc')
        os.system('python shell.py')
        os.chdir('..')
        os.chdir('..')
        os_page()
    if os_page_option == '2':
        apps()
    if os_page_option == '3':
        settings()
    if os_page_option == '1987':
        purple_man()
    else:
        os.system('cls')
        print('Not An Option!')
        os.system('pause')
        os_page()
    

def settings():
    global username_globalvar

    os.system('cls')
    print('-------------------------------------------------')
    print("|                   Settings.                   |")
    print('-------------------------------------------------\n')
    print("Welcome To The Settings!\n")
    print("Where Would you Like To Go?\n")
    print("1) User.")
    print("2) Go Back.\n")
    settings_option = os_input(username_globalvar)
    if settings_option == '1':
        user_settings()
    if settings_option == '2':
        os_page()

def user_settings():
    global username_globalvar

    os.system('cls')
    print('-------------------------------------------------')
    print("|                User Settings.                 |")
    print('-------------------------------------------------\n')
    print("Welcome To The User Settings!\n")
    print("What Would you Like To Do?\n")
    print("1) Logout.")
    print("2) Go Back.\n")
    user_option = os_input(username_globalvar)
    if user_option == '1':
        os.system('cls')
        os.remove('system/users/cur_user.dat')
        print('Logged Out!')
        playsound.playsound('media/sounds/os_logout.mp3')
        main(True)
    if user_option == '2':
        settings()
        
def start_up():
    set_os_def()    
    os.system('cls')
    play_sound('os_startup.mp3')
    draw_cheems()
    time.sleep(3.4)
    startup_page()

def main(set_start_up):
    check_cur_user()
    if set_start_up == True:
        start_up()
    startup_page()

main(True)
