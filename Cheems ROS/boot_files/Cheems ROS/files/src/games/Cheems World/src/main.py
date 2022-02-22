import pygame, sys, os
from settings import *
from level import Level

pygame.init()

GameScreen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
GameClock = pygame.time.Clock()

os.chdir('..')

level = Level()
BG = pygame.image.load(BG_PATH)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    GameScreen.blit(BG,(0,0))
    level.run()

    pygame.display.update()
    GameClock.tick(60)