"""
Module for managing platforms.
"""
import pygame
from platformer.spritesheet_functions import SpriteSheet

# These constants define our platform types:
#   Name of file
#   X location of sprite
#   Y location of sprite
#   Width of sprite
#   Height of sprite

GRASS_LEFT            =    (0, 64, 63, 62)
ICE_TOP_MIDDLE        =   (64, 64, 64, 62)
ICE_MIDDLE            = (64, 128, 64, 128)
STONE_PLATFORM_LEFT   = (384, 256, 63, 63)
STONE_PLATFORM_MIDDLE = (448, 193, 63, 63)
STONE_PLATFORM_RIGHT  = (448, 256, 63, 63)
ICE_TOP_LEFT  = (0, 64, 127, 63)
SPIKES = (320, 420, 64, 27)
ENEMY = (256, 345, 64, 40)

#########    
TOP_LEFT_SNOW = (0, 405, 63, 63)
TOP_MIDDLE_SNOW = (74, 405, 63, 63)
TOP_RIGHT_SNOW = (148, 405, 63, 63)

DIRT_LEFT = (0, 483, 63, 63)
DIRT_MIDDLE = (74, 483, 63, 63)
DIRT_RIGHT =  (148, 483, 63, 63)

TOP_LEFT_CORNER_SNOW = (221, 405,87, 63)
TOP_MIDDLE_CORNER_SNOW = (19, 559, 87, 63) 
TOP_RIGHT_CORNER_SNOW = (221, 482, 87, 63)

TOP_RIGHT_DOUBLE_SNOW = (110, 559, 63, 63)
LEFT_SIDE_SNOW = (258, 559, 63, 63)
RIGHT_SIDE_SNOW = (186, 559, 63, 63) 

DIRT_SNOW_CORNER = (0, 336, 63, 63)

DIRT_SNOW_CORNER_BL=(93, 337, 63, 63)

BOTTOM_MIDDLE_SNOW = (172, 336, 63, 63)



class Platform(pygame.sprite.Sprite):
    """ Platform the user can jump on """

    def __init__(self, sprite_sheet_data):
        """ Platform constructor. Assumes constructed with user passing in
            an array of 5 numbers like what's defined at the top of this
            code. """
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("stuff/sprites/snowTiles2_3.png")
        # Grab the image for this platform
        self.image = sprite_sheet.get_image(sprite_sheet_data[0],
                                            sprite_sheet_data[1],
                                            sprite_sheet_data[2],
                                            sprite_sheet_data[3])

        self.rect = self.image.get_rect()
        
class MovingPlatform(Platform):
    """Class for moving platforms"""
    change_x = 0
    change_y = 0

    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0

    level = None
    player = None
    
    def update(self):
        # Move left/right
        self.rect.x += self.change_x

        # See if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # If we are moving right, set our right side
            # to the left side of the item we hit
            if self.change_x < 0:
                self.player.rect.right = self.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.player.rect.left = self.rect.right

        # Move up/down
        self.rect.y += self.change_y

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.bottom = self.rect.top
            else:
                self.player.rect.top = self.rect.bottom

        # Check the boundaries and see if we need to reverse
        # direction.
        if self.rect.bottom > self.boundary_bottom or self.rect.top < \
        self.boundary_top:
            self.change_y *= -1

        cur_pos = self.rect.x - self.level.world_shift
        if cur_pos < self.boundary_left or cur_pos > self.boundary_right:
            self.change_x *= -1
        