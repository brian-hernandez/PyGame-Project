"""Module for 2 differnt types of enemies"""

import pygame
from platformer.spritesheet_functions import SpriteSheet
import platformer.platforms as platforms

class Enemies(pygame.sprite.Sprite):
    """class for the enemy (skeleton) sprites"""
    # Sprite Images
    enemy_moving_frames_r = []
    enemy_moving_frames_l = []
    
    change_x = 0
    change_y = 0
    
    # Boundaries
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    
    facing = "R"
    
    level = None
    player = None
    
    rect = None    

    def __init__(self, x, y, bound_L, bound_R, change):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet("stuff/sprites/skeleton_7.png")
        
        image = sprite_sheet.get_image(37, 7, 33, 64)
        self.enemy_moving_frames_r.append(image)
        image = sprite_sheet.get_image(70, 7, 33, 64)
        self.enemy_moving_frames_r.append(image)
        image = sprite_sheet.get_image(107, 7, 33, 64)
        self.enemy_moving_frames_r.append(image)
        image = sprite_sheet.get_image(142, 7, 33, 64)
        self.enemy_moving_frames_r.append(image)
        
        image = sprite_sheet.get_image(37, 7, 33, 64)
        image = pygame.transform.flip(image, True, False)
        self.enemy_moving_frames_l.append(image)
        image = sprite_sheet.get_image(70, 7, 33, 64)
        image = pygame.transform.flip(image, True, False)
        self.enemy_moving_frames_l.append(image)
        image = sprite_sheet.get_image(107, 7, 33, 64)
        image = pygame.transform.flip(image, True, False)
        self.enemy_moving_frames_l.append(image)
        image = sprite_sheet.get_image(142, 7, 33, 64)
        image = pygame.transform.flip(image, True, False)
        self.enemy_moving_frames_l.append(image)
        
        self.image = self.enemy_moving_frames_r[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.boundary_left = bound_L
        self.boundary_right = bound_R
        self.change_x = change
        

    def update(self):
        # Move left/right

        self.rect.x += self.change_x
           
        cur_pos = self.rect.x - self.level.world_shift
        
        if cur_pos < self.boundary_left:
            self.change_x *= -1

        elif cur_pos > self.boundary_right:
            self.change_x *= -1

        if self.change_x > 0:
            frame = (self.rect.x // 30) % len(self.enemy_moving_frames_l)
            self.image = self.enemy_moving_frames_l[frame]
            self.facing = "L"
        elif self.change_x < 0:
            frame = (self.rect.x // 30) % len(self.enemy_moving_frames_r)
            self.image = self.enemy_moving_frames_r[frame]
            self.facing = "R"
        
class MovingEnemy(platforms.Platform):
    """class for the moving spikes enemy"""
    change_x = 0
    change_y = 0

    # Boundaries
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None

    def update(self):

        # Move left/right
        self.rect.x += self.change_x
        
        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < \
        self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
    
