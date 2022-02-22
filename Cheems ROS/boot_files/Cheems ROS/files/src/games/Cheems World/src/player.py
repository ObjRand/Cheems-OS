import pygame
from tile import * 
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,groups,collision_sprites):
        super().__init__(groups)
        self.player_pos = pos

        print(self.player_pos)

        self.flip = 'right'
        #self.image = pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.image = pygame.image.load('assets\images\CHEEMS_right.png')
        #self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect(topleft = pos)

        # player movement
        self.direction = pygame.math.Vector2()
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = 16
        self.low_gravity = False
        self.collision_sprites = collision_sprites
        self.on_floor = False

    def flip_player(self,dir):
        self.image = pygame.image.load('assets\images\CHEEMS_' + dir + '.png')

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.flip = 'right'
            self.flip_player(self.flip)
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.flip = 'left'
            self.flip_player(self.flip)
            self.direction.x = -1
        else:
            self.flip_player(self.flip)
            self.direction.x = 0

        if keys[pygame.K_r]:
            # RESET RECTS POSITION TO ORIGNAL SPAWN #
            self.rect = self.image.get_rect(topleft = self.player_pos)

        if keys[pygame.K_l]:
            self.low_gravity = True
            self.gravity = 0.4

        if keys[pygame.K_k]:
            self.speed = 12
            
        if keys[pygame.K_SPACE] and self.on_floor:
            # MAKES YOUR Y INCREASES BY JUMP SPEED + X * 2 #
            if self.low_gravity == True:
                self.direction.y = -(self.jump_speed * (self.gravity * 2))
            else:
                self.direction.y = -(self.jump_speed + 2)

    def horizontal_collisions(self):
        for sprite in self.collision_sprites.sprites():
            if sprite.rect.colliderect(self.rect):
                if sprite == DeathTile:
                    self.rect = self.image.get_rect(topleft = self.player_pos)
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def vertical_collisions(self):
        for sprite in self.collision_sprites.sprites():
            #print(type(sprite))
            if sprite.rect.colliderect(self.rect):
                if sprite == pygame.DeathTile:
                    self.rect = self.image.get_rect(topleft = self.player_pos)
                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

        if self.on_floor and self.direction.y != 0:
            self.on_floor = False

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.input()
        self.rect.x += self.direction.x * self.speed
        self.horizontal_collisions()
        self.apply_gravity()
        self.vertical_collisions()