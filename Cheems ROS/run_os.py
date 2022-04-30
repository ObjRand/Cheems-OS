import os,threading,time
import pkg_resources

for package in ['colorama', 'keyboard','playsound','pyperclip','windows-curses']:
    try:
        dist = pkg_resources.get_distribution(package)
    except pkg_resources.DistributionNotFound:
        os.chdir('assets')
        os.chdir('tools')
        os.system(f'python installer.py')
        os.chdir('..')
        os.chdir('..')

import keyboard
from colorama import Fore, Style
from playsound import playsound

cd = os.getcwd()

osdir = os.listdir('boot_files')

lines = 8

for x in range(len(osdir)):
    lines += 2

os.system(f'mode con cols=45 lines={lines}')

def no_kernel_error():
    os.system('cls')
    play_sound('exit_menu.mp3')
    print(f'{Fore.RED}THIS OS HAS NO KERNEL!{Style.RESET_ALL}')
    print('')
    print(cd)
    os.remove('boot_files/cur_os.dat')
    os.system('pause')
    BOOTLOADER()

def startup_kernel(cur_os_data):
    os.chdir('boot_files')
    os.chdir(cur_os_data)
    os.system('python kernel.py')


def boot_input():
    the_input = input(f'{Fore.RED}boot{Style.RESET_ALL}@~>{Fore.CYAN}')
    print(Style.RESET_ALL,end='')
    return the_input 

def setsound(sound):
    # IT TRIES TO PLAY THE SOUND AND IF IT MAKE AN ERROR, IT WONT PLAY ANYTHING! #
    try:
        playsound('assets/' + sound)
    except:
        pass

def play_sound(sound):
    sound_thread = threading.Thread(target = setsound,args = [sound])
    sound_thread.start()

def os_check():
    print('BOOTING INTO OS...')

    os_file_exists = os.path.exists('boot_files/cur_os.dat')

    if os_file_exists:
        with open('boot_files/cur_os.dat') as cur_os_file:
            cur_os_data = cur_os_file.read()
            cur_os_file.close()
        try:
            startup_kernel(cur_os_data)
        except:
            no_kernel_error()
        quit()
    else:
        os.system('title Cheems BOOTLOADER')
        BOOTLOADER()

def start_bootloader():
    os.system('cls')

    print('--------------------------------------------')

    print(Fore.CYAN + '          CHEEMS BOOTLOADER V1.0' + Style.RESET_ALL)

    print('--------------------------------------------')


    play_sound('boot.mp3')

    print('''
    
                PRESS ENTER''')

    while True:
        if keyboard.is_pressed('enter'):
            os.system(f'mode con cols=100 lines=30')
            os.system('cls')
            print("""If You Want To Add An OS To The List Of OSES You Can Boot From...
Visit:\"https://github.com/Yeeterboi4/THE-CHEEMS-OS-REPOS/blob/main/Cheems%20ROS/boot_files/How%20To%20Make%20An%20OS.txt\" To Find Out More!
            
            """)
            print('Press Any Key To Continue.')
            os.system('pause >nul')
            break
    os_scan()

def os_scan():
    os.system(f'mode con cols=45 lines={lines}')
    x = 0
    os.system('cls')

    print('Choose What OS You Want To Boot In!')
    print('')

    for OS in osdir:
        print('- ' + osdir[x])
        print('')
        x += 1

    os_select()

def os_select():
    global os_len,osdir

    os_len = len(osdir) - 1
    os_to_boot = boot_input()

    if os_to_boot == '$refresh':
        play_sound('refresh.mp3')
        osdir = os.listdir('boot_files')
        os.system('cls')
        print('Refreshed Path!')
        print('')
        os.system('pause')
        os_scan()

    # CHECK IF YOUR INPUT EXISTS AS AN OS IN THE LIST AND SETS IT AS THE OS TO CHOOSE!
    for OS in osdir:
        # CHECK IF YOUR INPUT IS IN THE LIST
        if os_to_boot == osdir[os_len]:
            # PLAY ENTER MENU SOUND #
            play_sound('enter_menu.mp3')

            SelectedOS = osdir[os_len]
            os_set(SelectedOS)
        else:
            # AFTER INCREASES THE VALUE IF ITS NOT IN THE PART OF THE LIST (computers count from 0)
            os_len -= 1

    # IF IT CANT FIND IT, IT WILL SAY THAT IT DOESNT EXIST (it looks in all of through list)
    cantfindos(os_to_boot)

def os_set(SelectedOS):
    global os_len

    os.system('cls')

    print(f'You Selected{Fore.CYAN} {osdir[os_len]}{Style.RESET_ALL}!')
    print('')
    print(f'{Fore.RED}This OS Will Always Be Booted From!{Style.RESET_ALL}')
    print('')
    print(f'Are You {Fore.RED}SURE{Style.RESET_ALL} You Want To Use This OS? (T/F)')
    print('')
    set_choice = boot_input()
    if set_choice == 'T' or set_choice == 't':
        os.system('cls')

        # PLAY ENTER MENU SOUND #
        play_sound('enter_menu.mp3')

        print('BOOTING INTO OS...')

        time.sleep(0.5)

        with open('boot_files/cur_os.dat', 'w') as cur_os_file:
            cur_os_file.write(SelectedOS)
            cur_os_file.close()
        
        # BOOOOOOT TOOOOOO THEEEEEE OSSSSSS #
        try:
            startup_kernel(SelectedOS)
        except:
            no_kernel_error()
        quit()
    elif set_choice == 'F' or set_choice == 'f':
        play_sound('exit_menu.mp3')
        BOOTLOADER(False)
    else:
        os.system('cls')
        print('NOT AN OPTION!')
        os.system('pause')
        os_set(SelectedOS)

def cantfindos(os_to_boot):
    play_sound('exit_menu.mp3')
    os.system('cls')
    print(f'{Fore.RED}Cant Find OS: "{Fore.WHITE}{os_to_boot}{Fore.RED}"!{Style.RESET_ALL}')
    print('')
    print(f'Please Select An {Fore.CYAN}Existing{Style.RESET_ALL} OS!')
    print('')
    os.system('pause')
    BOOTLOADER(False)

def BOOTLOADER(start = True):
    if start:
        start_bootloader()

    os_scan()

os_check()