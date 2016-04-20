"""Module for objects that interact with player throughout game"""


import pygame
import time
from platformer.spritesheet_functions import SpriteSheet


class coins (pygame.sprite.Sprite):
    """class for coins"""
    coin_spin_frames = []
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        sprite_sheet = SpriteSheet('stuff/sprites/coins_1.png')
        
        image = sprite_sheet.get_image(0, 0, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        self.coin_spin_frames.append(image)
        image = sprite_sheet.get_image(0, 42, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        self.coin_spin_frames.append(image)
        image = sprite_sheet.get_image(0, 87, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        self.coin_spin_frames.append(image)
        image = sprite_sheet.get_image(0, 130, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        self.coin_spin_frames.append(image)
        image = sprite_sheet.get_image(0, 87, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        image = pygame.transform.flip(image, True, False)
        self.coin_spin_frames.append(image)
        image = sprite_sheet.get_image(0, 42, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        image = pygame.transform.flip(image, True, False)
        self.coin_spin_frames.append(image)
        image = sprite_sheet.get_image(0, 0, 40, 43)
        image = pygame.transform.scale(image, (30, 30))
        image = pygame.transform.flip(image, True, False)
        self.coin_spin_frames.append(image)
        
        self.image = self.coin_spin_frames[0]
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
    def update(self):
        a = time.time()
        b = a % 8
        c = b / 8
        some = (int(len(self.coin_spin_frames) * c))
        self.image = self.coin_spin_frames[some]

class hearts(pygame.sprite.Sprite):
    """class for chicken leg that adds a heart to player health"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('stuff/objects/chicken_leg.png')
        self.image = pygame.transform.scale(self.image, (40,30))
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
class gem(pygame.sprite.Sprite):
    """class for gems"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('stuff/objects/gem.png')
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
class sign(pygame.sprite.Sprite):
    """class for signs that offer instructions/hints"""
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load('stuff/objects/sign.png')
        self.image = a
        
        self.rect = self.image.get_rect()
        
        self.rect.x = x
        self.rect.y = y
        
class igloo(pygame.sprite.Sprite):
    """class for the ending location of level 1"""
    def __init__(self, player, x, y):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load('stuff/objects/Igloo.png')
        self.image = pygame.transform.scale(a, (300, 100))
        
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.x = x
        self.rect.y = y

        
class key(pygame.sprite.Sprite):
    """class for key object"""
    def __init__(self, x, y, own):
        pygame.sprite.Sprite.__init__(self)
        a = pygame.image.load('stuff/objects/key.png')
        self.image = pygame.transform.scale(a, (300, 100))
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class still_door(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('stuff/objects/door2.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
class bed(pygame.sprite.Sprite):
    """class for bed"""
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.image.load('stuff/objects/bed2.png')
        self.image = pygame.transform.scale(self.image, (90, 90))   
        #self.image = pygame.transform.rotate(self.image, -19) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    
    def update(self):
        # Not Asleep
        if self.player.complete == False:
            self.image = pygame.image.load('stuff/objects/bed2.png')
        # Asleep
        else:
            self.image = pygame.image.load('stuff/objects/bed_sleeping2.png')
        self.image = pygame.transform.scale(self.image, (90, 90))
        #self.image = pygame.transform.rotate(self.image, -19)

class door(pygame.sprite.Sprite): 
    """class for door that requires key to open"""
    level = None
    player = None
    change_y = 0
    
    def __init__(self, player, x, y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load('stuff/objects/door.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.player = player
        
        #sounds
        #self.door_unlock = pygame.mixer.Sound('stuff/sounds/door_unlock.wav')

    def update(self):

        # Check and see if we hit the player
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            # We did hit the player. Shove the player around and
            # assume he/she won't hit anything else.

            # Reset our position based on the top/bottom of the object.
            if self.change_y < 0:
                self.player.rect.right = self.rect.left
                #pygame.mixer.Sound.play(self.denied_sound)
            elif self.player.haveKey == True:
                self.rect.y = 201
                #pygame.mixer.Sound.play(self.door_unlock)
                self.player.haveKey = False
                self.player.door_locked = False
            else:
                self.player.rect.right = self.rect.left
                #pygame.mixer.Sound.play(self.denied_sound)
    
class wizard(pygame.sprite.Sprite):
    """wizard class; controls movement and messages"""
    wizard_walk_l = []
    wizard_walk_r = []
    wizard_wait = []
    
    talking = False
    
    change_x = 0
    change_y = 0
    
    boundary_top = 0
    boundary_bottom = 0
    boundary_left = 0
    boundary_right = 0
    
    level = None
    player = None
    
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self)
        
        self.player = player
        
        sprite_sheet = SpriteSheet('stuff/sprites/wizard_1.png')
        
        image = sprite_sheet.get_image(3, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(62, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(123, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(183, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(243, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(303, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(363, 98, 52, 83)
        self.wizard_walk_l.append(image)
        image = sprite_sheet.get_image(423, 98, 52, 83)
        self.wizard_walk_l.append(image)
        
        image = sprite_sheet.get_image(3, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(62, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(123, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(183, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(243, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(303, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(363, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        image = sprite_sheet.get_image(423, 98, 52, 83)
        image = pygame.transform.flip(image, True, False)
        self.wizard_walk_r.append(image)
        
        image = sprite_sheet.get_image(3, 3, 60, 88)
        self.wizard_wait.append(image)
        
        
        self.image = self.wizard_walk_r[0]
        self.rect = self.image.get_rect()


    def update(self):
        # Move left/right
        self.rect.x += self.change_x
           
        cur_pos = self.rect.x - self.level.world_shift
        
        if cur_pos < self.boundary_left:
            self.change_x *= -1
        elif cur_pos > self.boundary_right:
            self.change_x *= -1
        
        hit = pygame.sprite.collide_rect(self, self.player)
        if hit:
            self.talking = True
            self.image = self.wizard_wait[0]
            if self.change_x > 0:
                self.rect.x = self.rect.x - 1
            elif self.change_x < 0:
                self.rect.x = self.rect.x + 1
        else:
            self.talking = False
            if self.change_x > 0:
                frame = (self.rect.x // 20) % len(self.wizard_walk_r)
                self.image = self.wizard_walk_r[frame]
            elif self.change_x < 0:
                frame = (self.rect.x // 20) % len(self.wizard_walk_l)
                self.image = self.wizard_walk_l[frame]
