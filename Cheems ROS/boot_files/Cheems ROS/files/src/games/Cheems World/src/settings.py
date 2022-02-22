import threading, playsound

def SET_GET_MAP(LEVEL_FILE):
    LEVEL_MAP = []

    with open(LEVEL_FILE, 'r') as map:
        for line in map:
            LEVEL_MAP.append(line.rstrip("\n"))

    return LEVEL_MAP

def setsound(sound):
    playsound('assets/sounds/' + sound)

def play_sound(sound):
    sound_thread = threading.Thread(target = setsound,args = [sound])
    sound_thread.start()

TILE_SIZE = 64
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# COLORS #
BG_PATH = 'bg_grass.png'

# TILE COLORS #
TILE_GRASS = 'assets\images\cheems_grass.png'
TILE_DIRT = 'assets\images\cheems_dirt.png'

# CAMERA #
CAMERA_BORDERS = {
    'left': 100,
    'right':200,
    'top':100,
    'bottom':150
}