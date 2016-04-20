"""Module that defines player and how it interacts with environment(objects)"""

import pygame
import platformer.constants as constants
from platformer.platforms import MovingPlatform
from platformer.spritesheet_functions import SpriteSheet
        
class Player(pygame.sprite.Sprite):
    
    """ This class represents the player sprite. It keeps track of
        movement and which sprite frames to use. It controls the
        collisions and what to do depending on sprite group.
    """

    # -- Attributes
    # Set speed vector of player
    change_x = 0
    change_y = 0

    # This holds all the images for the animated walk left/right
    # of our player
    walking_frames_l = []
    walking_frames_r = []
    
    # This holds all the images for the animated jump left/right
    # of our player
    jumping_frames_l = []
    jumping_frames_r = []
    
    # This holds all the images for the animated idle 
    # of our player
    idle_frames_r = []
    
    # This holds all the images for the animated hurt 
    # of our player
    hurt_frames_r = []
    hurt_frames_l = []
    
    # This checks whether the messages of the wizard should appear
    wizard_message = False
    wizard_message2 = False

    # What direction is the player facing?
    direction = "S"
    facing = "R"

    # List of sprites we can bump against
    level = None
    
    # Variables keeping track of score, coins, health, and seconds(t)
    score = 0
    coins = 0
    health = 3
    t = 0
    
    # Boolean variables to check whether damage and hurt sound
    # should occur
    damage = False
    hurt_sound = False
    
    # Checks whether a sign message should be appearing
    sign1 = False
    sign2 = False
    
    # Checks whether the player has a gem/key
    haveGem = False
    haveKey = False
    
    sleeping = False
    
    # Checks the status of the gate (locked/unlocked) and shows message
    door_message = False
    door_locked = True
    
    # Checks if the level is over
    level_over = False
    
    #igloo hit (if collision occurs, goes to next level)
    igloo = False
    
    #check is level is complete
    complete = False
    
    # -- Methods
    def __init__(self):
        """ Constructor function. 
        
        It obtains distinct player sprite images and adds them to a list. 
        The images include idle, right/left facing, damage, and jumping states.
        """

        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        sprite_sheet = SpriteSheet("stuff/sprites/raz.png")
        
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(10, 122, 72, 69)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(100, 122, 72, 69)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(186, 122, 72, 69)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(275, 122, 72, 69)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(365, 122, 72, 70)
        self.walking_frames_r.append(image)

        #idle frames facing right
        image = sprite_sheet.get_image(10, 122, 72, 69)
        self.idle_frames_r.append(image)
        image = sprite_sheet.get_image(100, 122, 72, 69)
        self.idle_frames_r.append(image)


        # Load all the right facing images, then flip them
        # to face left.
        image = sprite_sheet.get_image(10, 122, 72, 69)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(100, 122, 72, 69)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(186, 122, 72, 69)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(275, 122, 72, 69)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        image = sprite_sheet.get_image(365, 122, 72, 70)
        image = pygame.transform.flip(image, True, False)
        self.walking_frames_l.append(image)
        
        # Load all the right facing jumping images into a list
        image = sprite_sheet.get_image(10, 13, 72, 69)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(85, 12, 70, 77)
        self.jumping_frames_r.append(image)
        image = sprite_sheet.get_image(165, 20, 70, 66)
        self.jumping_frames_r.append(image)

        # Load all the right facing jumping images, then flip them
        # to face left.
        image = sprite_sheet.get_image(10, 13, 72, 69)
        image = pygame.transform.flip(image, True, False)
        self.jumping_frames_l.append(image)
        image = sprite_sheet.get_image(85, 12, 70, 77)
        image = pygame.transform.flip(image, True, False)
        self.jumping_frames_l.append(image)
        image = sprite_sheet.get_image(165, 20, 72, 66)
        image = pygame.transform.flip(image, True, False)
        self.jumping_frames_l.append(image)
        
        # Hurt frames R
        image = sprite_sheet.get_image(269, 23, 71, 76)
        self.hurt_frames_r.append(image)
        
        # Hurt frames L
        image = sprite_sheet.get_image(269, 23, 71, 76)
        image = pygame.transform.flip(image, True, False)
        self.hurt_frames_l.append(image)
        
        # Set the image the player starts with
        self.image = self.walking_frames_r[0]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        
        # Sounds 
        '''self.coin_sound = pygame.mixer.Sound('stuff/sounds/coinSound-2.wav')
        self.grabbing_gem = pygame.mixer.Sound('stuff/sounds/grabbing_Gem.wav')
        self.getting_key = pygame.mixer.Sound('stuff/sounds/item_fanfare.wav')
        self.wizard_hello = pygame.mixer.Sound('stuff/sounds/wizard_hello.wav')
        self.heart_sound = pygame.mixer.Sound('stuff/sounds/burp.wav')'''
        
    def hurt(self):
        """Removes a health point and checks if player is dead"""
        self.health -= 1
        if self.health == 0:
            self.kill()
            
    def shoot(self):
        """Creates a bullet (snowball)"""
        bullet = Bullet(self, self.rect.x, self.rect.y, self.level, self.facing)
        return bullet
        
    
    def update(self):
        """ Move the player. """
        # Gravity
        self.calc_grav()
        
        # Move left/right
        self.rect.x += self.change_x
        pos = self.rect.x + self.level.world_shift
        
        if self.facing == "R":
            frame = (pos // 30) % len(self.walking_frames_r)
            self.image = self.walking_frames_r[frame]
            
        if self.facing == "L":
            frame = (pos // 30) % len(self.walking_frames_l)
            self.image = self.walking_frames_l[frame]
        
        if self.direction == "U" and self.facing == "R":
            frame = (pos // 90) % len(self.jumping_frames_r)
            self.image = self.jumping_frames_r[frame]
        if self.direction == "U" and self.facing == "L":
            frame = (pos // 90) % len(self.jumping_frames_l)
            self.image = self.jumping_frames_l[frame]
        
        
        # Calls hurt function once every second while enemy
        # and player collision is occuring.
        if self.damage == True:
            a = (int(pygame.time.get_ticks()))
            a = int(a/1000)
            b = 0
            if self.t != a:
                self.t = a
                b =+ 1
                if b == 1:
                    self.hurt()
                    self.hurt_sound = True
                    if self.facing == "R":
                        self.image = self.hurt_frames_r[0]
                    if self.facing == "L":
                        self.image = self.hurt_frames_l[0]
                    b = 0                     
        self.damage = False
            
        # See if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, \
                                                     self.level.platform_list,\
                                                      False)
        for block in block_hit_list:
            # If we are moving right,
            # set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            elif self.change_x < 0:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
    

        # Move up/down
        self.rect.y += self.change_y
        # Check and see if we hit anything
        
        ########################################################################
        # Getting a coin
        ########################################################################
        coin_hit_list = pygame.sprite.spritecollide(self, \
                                                    self.level.coin_list, \
                                                    True)
        if coin_hit_list:
            #pygame.mixer.Sound.play(self.coin_sound)
            self.coins += 1
         
         
        #sleeping
        bed_hit = pygame.sprite.spritecollide(self, self.level.bed, False)
        
        if bed_hit:
            self.sleeping = True
            self.complete = True
            self.kill()          
            
            
        ########################################################################
        # Reading signs
        ########################################################################
        # Sign 1
        sign_hit = pygame.sprite.spritecollide(self, self.level.sign_1, False)
        
        if sign_hit:
            self.sign1 = True
            self.sign1 = True
        else:
            self.wizard_message = False
            self.sign1 = False
            
        # Sign 2
        sign_hit2 = pygame.sprite.spritecollide(self, self.level.sign_2, False)
        
        if sign_hit2:
            self.sign2 = True
        else:
            self.sign2 = False
        
        ########################################################################
        # Igloo
        ########################################################################
        
        igloo_hit = pygame.sprite.spritecollide(self, self.level.igloo, False)
        
        if igloo_hit:
            self.igloo = True
        else:
            self.igloo = False

        ########################################################################
        # Wizard
        ########################################################################
        
        wiz_hit = pygame.sprite.spritecollide(self, self.level.wizard, False)
        
        if wiz_hit:
            if self.haveGem == False and self.haveKey == False:
                self.wizard_message = True
            elif self.haveGem == True and self.haveKey == False:
                self.haveGem = False
                self.haveKey = True
                self.wizard_message2 = True
                #pygame.mixer.Sound.play(self.getting_key)
            elif self.haveGem == False and self.haveKey == True:
                self.wizard_message2 = True
        else:
            self.wizard_message = False
            self.wizard_message2 = False
            
        ########################################################################
        # Collecting Gem
        ########################################################################

        gem_hit = pygame.sprite.spritecollide(self, self.level.gem, True)
        if gem_hit:
           # pygame.mixer.Sound.play(self.grabbing_gem)
            self.haveGem = True
            self.haveKey = False
            
        ########################################################################
        # Locked Door Message
        ########################################################################
        door_hit = pygame.sprite.spritecollide(self, self.level.doors, False)
        
        if door_hit:
            self.door_message = True
        else:
            self.door_message = False
        
        ########################################################################
        # Hearts
        ########################################################################
        single_heart_hit_list = pygame.sprite.spritecollide\
        (self,self.level.single_heart_list,True)
        if single_heart_hit_list:
            if self.health == 3:
                self.health = 3
               # pygame.mixer.Sound.play(self.heart_sound)
            else:
                self.health += 1
               # pygame.mixer.Sound.play(self.heart_sound)
        
        ########################################################################
        # Enemies
        ########################################################################
        
        # Moving Enemy
        enemy_hit_list = pygame.sprite.spritecollide(self, \
                                                     self.level.enemy_list, \
                                                     False)
        if enemy_hit_list:
            self.damage = True        
        
        # Skeleton Enemy
        enemy_hit_list2 = pygame.sprite.spritecollide(self, \
                                                      self.level.enemy_list2, \
                                                      False)
        if enemy_hit_list2:
            self.damage = True
        
        # Spikes
        if self.rect.y > 516:
            self.damage = True
        
        ########################################################################
        # Platforms
        ########################################################################
        
        block_hit_list = pygame.sprite.spritecollide(self, \
                                                     self.level.platform_list,\
                                                     False)
        for block in block_hit_list:

            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            if isinstance(block, MovingPlatform):
                self.rect.x += block.change_x
            if block_hit_list:
                if self.direction == "R" or self.direction == "L":
                    self.direction = "S"


    def calc_grav(self):
        """ Calculate effect of gravity. """
        if self.change_y == 0:
            self.change_y = 2
        else:
            self.change_y += 1.3

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and\
         self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        self.direction = "U"
        self.rect.y += 2
        platform_hit_list = \
        pygame.sprite.spritecollide(self, self.level.platform_list, False)
        self.rect.y -= 2

        # If it is ok to jump, set our speed upwards
        if len(platform_hit_list) > 0 or\
         self.rect.bottom >= constants.SCREEN_HEIGHT:
                self.change_y = -19.8
        

    # Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -7
        self.direction = "L"
        self.facing = "L"
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 7
        self.direction = "R"
        self.facing = "R"
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
        #self.facing = "R"
        
class Bullet(pygame.sprite.Sprite):
    """Class for the snowball"""
    
    explosion_frames = []
    t = 0
    
    def __init__(self, player, playerx, playery, level, facing):
        pygame.sprite.Sprite.__init__(self)
        
        #sounds
       # self.snow_sound1 = pygame.mixer.Sound('stuff/sounds/snow_on_object.wav')
        #self.enemy_death_sound1 = pygame.mixer.Sound('stuff/sounds/soft_explosion.wav')
        
        a = pygame.image.load("stuff/sprites/snowball.png")
        self.image = pygame.transform.scale(a, (20, 21))
        
        #explosion
        sprite_sheet = SpriteSheet("stuff/sprites/explosion.png")
        
        image = sprite_sheet.get_image(32, 36, 62, 53)
        self.explosion_frames.append(image)

        

        self.player = player

        self.rect = self.image.get_rect()
        if facing == "L":
            self.rect.x = playerx 
            self.rect.y = playery + 35
        elif facing == "R":
            self.rect.x = playerx + 50
            self.rect.y = playery + 35

        self.level = level
        self.facing = facing
        self.damage = False
        
    def update(self):
        if self.facing == "R" and self.damage != True:
            self.rect.x += 10
        elif self.facing == "L" and self.damage != True:
            self.rect.x += -10
        else:
            self.rect.x = self.rect.x
            self.rect.y = self.rect.y - 80
            self.kill()

        pos = self.rect.x - self.level.world_shift
        
        # Checks collision between snowaball and enemy (skeleton)
        enemy_hit_list = pygame.sprite.spritecollide(self, \
                                                     self.level.enemy_list2,\
                                                      True)
        if enemy_hit_list:
            self.player.score += 100
            #pygame.mixer.Sound.play(self.enemy_death_sound1)
            frame = (pos // 30) % len(self.explosion_frames)
            self.image = self.explosion_frames[frame]
            self.damage = True
        
        # Checks the collision between the snowball and walls/platforms
        wall_hit_list = pygame.sprite.spritecollide(self, \
                                                    self.level.platform_list,\
                                                     False)
        if wall_hit_list:
           # pygame.mixer.Sound.play(self.snow_sound1)
            #self.image = self.explosion_frames[3]
            self.damage = True