import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,type):
        super().__init__(groups)

        self.display_surface = pygame.display.get_surface()

        if type == 'grass':
            self.image = pygame.image.load(TILE_GRASS)
        if type == 'dirt':
            self.image = pygame.image.load(TILE_DIRT)

        self.rect = self.image.get_rect(topleft = pos)

class InteractableTile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,type):
        super().__init__(groups)

        self.display_surface = pygame.display.get_surface()

        if type == 'Fast':
            self.image = pygame.image.load('assets/images/fast.png')

        self.rect = self.image.get_rect(center = pos)

class BorderTile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,size):
        super().__init__(groups)

        if size == 'normal':
            TILE_WIDTH = TILE_SIZE
        if size == 'small':
            TILE_WIDTH = TILE_SIZE // 2
        if size == 'smaller':
            TILE_WIDTH = TILE_SIZE // 4
        if size == 'very small':
            TILE_WIDTH = TILE_SIZE // 8

        self.image = pygame.Surface((TILE_WIDTH,TILE_SIZE))

        self.rect = self.image.get_rect(topleft = pos)

class DeathTile(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)

        self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))

        self.rect = self.image.get_rect(topleft = pos)