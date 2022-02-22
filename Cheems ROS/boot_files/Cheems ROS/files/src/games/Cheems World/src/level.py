import pygame
from settings import *
from tile import *
from player import Player

class Level:

    def __init__(self):
        
        self.player_pos = ()

        # LEVEL SETUP #
        self.display_surface = pygame.display.get_surface()

        # sprite group setup
        self.visible_sprites = CameraGroup()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self):
        LEVEL_MAP = SET_GET_MAP('level.map')
        for row_index,row in enumerate(LEVEL_MAP):
            for col_index,col in enumerate(row):
                x = col_index * TILE_SIZE 
                y = row_index * TILE_SIZE

                pos = (x,y)

                if col == 'G':
                    Tile(pos, [self.visible_sprites,self.collision_sprites],'grass')
                if col == 'D':
                    Tile(pos, [self.visible_sprites,self.collision_sprites],'dirt')
                if col == 'B':
                    BorderTile(pos, [self.collision_sprites], 'very small')
                if col == 'F':
                    InteractableTile((x,y+48), [self.visible_sprites,self.collision_sprites], 'Fast')
                if col == 'K':
                    DeathTile((x,y), [self.collision_sprites])
                if col == 'P':
                    self.player_pos = (x,y)
                    self.player = Player(self.player_pos, [self.visible_sprites,self.active_sprites],self.collision_sprites)

    def run(self):
        # RUN THE LEVEL #
        self.active_sprites.update() 
            
        self.visible_sprites.custom_draw(self.player)

class CameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__() 
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        # Center Camera Setup #

        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

    def custom_draw(self,player):

        # get the player offset 
        self.offset.x = player.rect.centerx - self.half_w
        self.offset.y = player.rect.centery - self.half_h

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

