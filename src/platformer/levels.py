"""Module that defines levels; objects, items, etc"""

import pygame
import platformer.constants as constants
import platformer.platforms as platforms
import platformer.enemies as enemies
import platformer.objects as objects
import platformer.level_list as lv

class Level():
    """ This is a generic super-class used to define a level.
        Create a child class for each level with level-specific
        info. """

    # Lists of sprites used in all levels. Add or remove
    # lists as needed for your game. """
    platform_list = None
    enemy_list = None
    coin_list = None
    enemy_list2 = None
    single_heart_list = None
    health = None
    sign_1 = None
    sign_2 = None
    igloo = None
    gem = None
    wizard = None
    doors = None
    gate = None
    bed = None
    
    
    # Background image
    background = None

    # How far this world has been scrolled left/right
    world_shift = 0
    level_limit = 0
    
    def __init__(self, player):
        """ Constructor. Pass in a handle to player. Needed for when 
        moving platforms collide with the p
        layer. """
        
        self.platform_list = pygame.sprite.Group()
        self.enemy_list = pygame.sprite.Group()
        self.enemy_list2 = pygame.sprite.Group()
        self.coin_list = pygame.sprite.Group()
        self.health = pygame.sprite.Group()
        self.single_heart_list = pygame.sprite.Group()
        self.sign_1 = pygame.sprite.Group()
        self.sign_2 = pygame.sprite.Group()
        self.wizard = pygame.sprite.Group()
        self.igloo = pygame.sprite.Group()
        self.gem = pygame.sprite.Group()
        self.doors = pygame.sprite.Group()
        self.gate = pygame.sprite.Group()
        self.bed = pygame.sprite.Group()
        
        self.player = player
        
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
        self.enemy_list2.update()
        self.coin_list.update()
        self.health.update()
        self.single_heart_list.update()
        self.wizard.update()
        self.igloo.update()
        self.gem.update()
        self.doors.update()
        self.gate.update()
        self.bed.update()
        

    def draw(self, screen):
        """ Draw everything on this level. """
        
        # Draw the background
        screen.fill(constants.WHITE)
        screen.blit(self.background, (self.world_shift // 3, 0))
        
        # Draw all the sprite lists that we have
        self.gate.draw(screen)
        self.platform_list.draw(screen)
        self.enemy_list.draw(screen)
        self.enemy_list2.draw(screen)
        self.coin_list.draw(screen)
        self.health.draw(screen)
        self.single_heart_list.draw(screen)
        self.sign_1.draw(screen)
        self.sign_2.draw(screen)
        self.wizard.draw(screen)
        self.igloo.draw(screen)
        self.gem.draw(screen)
        self.doors.draw(screen)
        self.gate.draw(screen)
        self.bed.draw(screen)


    def shift_world(self, shift_x):
        """ When the user moves left/right and we need to scroll everything"""

        # Keep track of the shift amount
        self.world_shift += shift_x

        # Go through all the sprite lists and shift
        
        for platform in self.platform_list:
            platform.rect.x += shift_x

        for enemy in self.enemy_list:
            enemy.rect.x += shift_x
            
        for enemy2 in self.enemy_list2:
            enemy2.rect.x += shift_x    
            
        for coin in self.coin_list:
            coin.rect.x += shift_x
        
        for heart in self.single_heart_list:
            heart.rect.x += shift_x

        for sign in self.sign_1:
            sign.rect.x += shift_x
        
        for sign in self.sign_2:
            sign.rect.x += shift_x
            
        for igloo in self.igloo:
            igloo.rect.x += shift_x
            
        for wiz in self.wizard:
            wiz.rect.x += shift_x

        for gem in self.gem:
            gem.rect.x += shift_x
            
        for door in self.doors:
            door.rect.x += shift_x
        
        for gate in self.gate:
            gate.rect.x += shift_x
            
        for bed in self.bed:
            bed.rect.x += shift_x
   
# Create platforms for the level
class Level_01(Level):
    """ Definition for level 1. """
    
    def __init__(self, player):
        """ Create level 1. """
        # Call the parent constructor
        Level.__init__(self, player)
        
        """pygame.mixer.music.load('stuff/sounds/SonicMusic.wav')"""
       # pygame.mixer.music.play(-1)
        self.background = pygame.image.load("stuff/backgrounds/BG.png"\
                                            ).convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = -2500

        # Array with type of platform, and x, y location of the platform.
        level = lv.level
        
        #######################################################################
        # Chicken Legs
        ####################################################################### 
        single_heart = [objects.hearts(116, 230), 
                        objects.hearts(1750, 520)]
        
        
        #######################################################################
        # Signs
        ####################################################################### 

        hint_sign1 = objects.sign(120, 465) 
        hint_sign2 = objects.sign(3400, 468)
        
        
        #######################################################################
        # Igloo
        ####################################################################### 
        
        igloo = objects.igloo(player, 3500, 460)
        
        #######################################################################
        # Gem
        ####################################################################### 
        
        gem = [objects.gem(1920, 500)]
        
        #######################################################################
        # Coins
        ####################################################################### 
        coins = [objects.coins(116,82),
                 objects.coins(230,82), 
                 
                 objects.coins(760,500),
                 objects.coins(820,500),
                 objects.coins(880,500),
                 objects.coins(940,500),
                 objects.coins(1000,500),
                 
                 objects.coins(1948,430),
                 objects.coins(1948,340),
                 objects.coins(1948,270),
                 
                 objects.coins(1320,60),
                 objects.coins(1380,60),
                 objects.coins(1440,60),
                 objects.coins(1500,60),
                 objects.coins(1560,60),
                 objects.coins(1620,60),
                 objects.coins(1680,60),
                 
                 objects.coins(1320,500),
                 objects.coins(1380,500),
                 objects.coins(1440,500),
                 objects.coins(1500,500),
                 objects.coins(1560,500),
                 objects.coins(1620,500),
                 objects.coins(1680,500),
                 
                 objects.coins(1060,200),
                 objects.coins(1120,200),
                 objects.coins(1180,200),
                 
                 objects.coins(810,60),
                 objects.coins(870,60),
                 objects.coins(930,60),
                 objects.coins(990,60),
                 
                 objects.coins(2800,380),
                 objects.coins(2860,380),
                 objects.coins(2920,380),
                 objects.coins(2980,380),
                 
                 objects.coins(3000,500),
                 objects.coins(3060,500),
                 objects.coins(3120,500),
                 objects.coins(3180,500),
                 objects.coins(3240,500),
                 objects.coins(3300,500),
                 ]
        
        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
               
        #add sprites to corresponding lists
        self.coin_list.add(coins)
        self.single_heart_list.add(single_heart)
        self.sign_1.add(hint_sign1)
        self.sign_2.add(hint_sign2)
        self.igloo.add(igloo)
        self.gem.add(gem)
        
        #######################################################################
        # Unlockable Door
        #######################################################################  
        door1 = objects.door(player, 2435, 405 )
        door1.level = self
        door1.player = self.player
        self.doors.add(door1)
        
        #######################################################################
        # Gate
        #######################################################################
        gate = objects.still_door(2435, 200)
        self.gate.add(gate)


        #######################################################################
        # Wizard
        #######################################################################  
        wizard = objects.wizard(player)
        wizard.rect.x = 2700
        wizard.rect.y = 57
        wizard.boundary_left = 2600
        wizard.boundary_right = 2950
        if wizard.talking == True:
            wizard.change_x = 0
        elif wizard.talking == False:
            wizard.change_x = 1
        wizard.level = self
        self.wizard.add(wizard)
        
        #######################################################################
        # Skeleton Enemies
        #######################################################################        
        w = enemies.Enemies(200, 192, 65, 280, 2)
        w.level = self
        self.enemy_list2.add(w)
        
        w2 = enemies.Enemies(1500, 496, 1345, 1555, 2)
        w2.level = self
        self.enemy_list2.add(w2)
        
        w3 = enemies.Enemies(379, 485, 379, 415, 2)
        w3.level = self
        self.enemy_list2.add(w3)
        
        w4 = enemies.Enemies(3000, 496, 2700, 3200, 2)
        w4.level = self
        self.enemy_list2.add(w4)
        
        w5 = enemies.Enemies(2800, 350, 2799, 3000, 2)
        w5.level = self
        self.enemy_list2.add(w5)
        
        #######################################################################
        # Moving Platforms
        #######################################################################        
        # Platform 1
        block = platforms.MovingPlatform(platforms.ICE_TOP_MIDDLE)
        block.rect.x = 520
        block.rect.y = 374
        block.boundary_bottom = 575
        block.boundary_top = 300
        block.change_y = 2
        block.player = self.player
        block.level = self
        self.platform_list.add(block)
        
        # Platform 2 (left)
        block2 = platforms.MovingPlatform(platforms.TOP_RIGHT_CORNER_SNOW)
        block2.rect.x = 1863
        block2.rect.y = 316
        block2.boundary_bottom = 575
        block2.boundary_top = 316
        block2.change_y = 2
        block2.player = self.player
        block2.level = self
        self.platform_list.add(block2)
        
        # Platform 4 - ENEMY
        block = enemies.MovingEnemy(platforms.ENEMY)
        block.rect.x = 800
        block.rect.y = 523
        block.boundary_left = 710
        block.boundary_right = 900
        block.change_x = 2
        block.player = self.player
        block.level = self
        self.enemy_list.add(block)
        
        # Platform 5
        block5 = platforms.MovingPlatform(platforms.ICE_TOP_MIDDLE)
        block5.rect.x = 2150
        block5.rect.y = 250
        block5.boundary_bottom = 545
        block5.boundary_top = 250
        block5.change_y = 3
        block5.player = self.player
        block5.level = self
        self.platform_list.add((block5))

class Level_02(Level):
    """ Definition for level 2. """

    def __init__(self, player):
        """ Create level 2. """

        # Call the parent constructor
        Level.__init__(self, player)

        self.background = pygame.image.load("stuff/backgrounds/blueback.png"\
                                            ).convert()
        self.background.set_colorkey(constants.WHITE)
        self.level_limit = 0
        
        #######################################################################
        # Bed
        ####################################################################### 
        
        bed = objects.bed(1100, 470, player)
        self.bed.add(bed)
        
        #######################################################################
        # Coins
        ####################################################################### 
        
        coins = [objects.coins(520,500),
                 objects.coins(580,500),
                 objects.coins(640,500),
                 objects.coins(700,500),
                 objects.coins(760,500),
                 objects.coins(820,500),
                 objects.coins(880,500),
                 objects.coins(940,500),
                 objects.coins(1000,500),
                 objects.coins(1060,500),
                 ]
        self.coin_list.add(coins)
        


        # Array with type of platform, and x, y location of the platform.
        level = [ 
                  [platforms.SPIKES, -12, 589],
                  [platforms.SPIKES, 52, 589],
                  [platforms.SPIKES, 116, 589],
                  [platforms.SPIKES, 180, 589],
                  [platforms.SPIKES, 244, 589],
                  [platforms.SPIKES, 308, 589],
                  [platforms.SPIKES, 372, 589],
                  [platforms.SPIKES, 436, 589],
                  [platforms.ICE_TOP_MIDDLE, 500, 560],
                  [platforms.ICE_TOP_MIDDLE, 564, 560],
                  [platforms.ICE_TOP_MIDDLE, 628, 560],
                  [platforms.ICE_TOP_MIDDLE, 692, 560],
                  [platforms.ICE_TOP_MIDDLE, 756, 560],
                  [platforms.ICE_TOP_MIDDLE, 820, 560],
                  [platforms.ICE_TOP_MIDDLE, 884, 560],
                  [platforms.ICE_TOP_MIDDLE, 948, 560],
                  [platforms.ICE_TOP_MIDDLE, 1012, 560],
                  [platforms.ICE_TOP_MIDDLE, 1076, 560],
                  [platforms.ICE_TOP_MIDDLE, 1140, 560],
                  [platforms.ICE_TOP_MIDDLE, 1204, 560],
                  [platforms.SPIKES, 1268, 589],
                  [platforms.SPIKES, 1332, 589],
                  [platforms.SPIKES, 1396, 589],
                  [platforms.SPIKES, 1460, 589],
                  [platforms.SPIKES, 1524, 589],
                  [platforms.SPIKES, 1588, 589],
                  [platforms.SPIKES, 1652, 589],
                  ]


        # Go through the array above and add platforms
        for platform in level:
            block = platforms.Platform(platform[0])
            block.rect.x = platform[1]
            block.rect.y = platform[2]
            block.player = self.player
            self.platform_list.add(block)
