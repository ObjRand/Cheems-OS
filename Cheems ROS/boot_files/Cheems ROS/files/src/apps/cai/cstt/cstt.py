import curses as crs
from curses import wrapper
import time,random,os

os.system('mode con cols=70 lines=11')

wpm = 0

def rand_line():
    with open('lines.txt', 'r') as f:
        lines = f.readlines()
        f.close()
        return lines[random.randint(0, len(lines) - 1)].strip()

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr('Welcome To Cheems Speed Type Test! (AKA C.S.T.T)')
    stdscr.addstr('\nPress A Key To Begin!')
    stdscr.refresh()
    key = stdscr.getkey()
    if ord(key) == 27:
        quit()

def display_text(stdscr,target,current,wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1,0,f'WPM: {wpm}')

    for i, char in enumerate(current):
        correct_char = target[i]
        if char != correct_char:
            color = crs.color_pair(2)
        else:
            color = crs.color_pair(1)

        stdscr.addstr(0,i,char,color)

def wpm_test(stdscr):
    target_text = rand_line()
    current_text = []
    start_time = time.time()

    stdscr.nodelay(True)

    while True:
        time_elapsed = max(time.time() - start_time,1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)

        stdscr.clear()

        display_text(stdscr,target_text,current_text,wpm)

        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break

        try: 
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break

        # IF KEY PRESSED IS BACKSPACE, REMOVE CUR CHAR FROM LIST IF YOU CAN #
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(current_text) > 0:
                current_text.pop()
        elif len(current_text) < len(target_text):
            current_text.append(key)
    win(stdscr)

def win(stdscr):
    stdscr.clear()
    stdscr.addstr(1, 0, "YOU COMPLETED THE TEXT!!!")
    stdscr.addstr(3, 0, "Wanna Play Again? (Y/N)\n")

    key = stdscr.getkey()

    stdscr.clear()
    stdscr.addstr(0, 0, "[Press A Key To Start!]")

    if key == 'Y' or key == 'y':
        stdscr.getch()
        wpm_test(stdscr)
    elif key == 'N' or key == 'n' or ord(key) == 27:
        quit()
    else:
        stdscr.clear()
        stdscr.addstr(1, 0, "NOT AN OPTION!",crs.color_pair(2))
        stdscr.getch()
        win(stdscr)

def main(stdscr):
    crs.init_pair(1, crs.COLOR_GREEN, crs.COLOR_BLACK)
    crs.init_pair(2, crs.COLOR_RED, crs.COLOR_BLACK)
    crs.init_pair(3, crs.COLOR_WHITE, crs.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)
    win(stdscr)

wrapper(main)