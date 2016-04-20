"""Module for text messages throughout the level"""

import pygame
import platformer.constants as constants

def texts(screen, score, coins):
    """Displays collected coins and acquired score.
        Displays text on top right corner of screen.
    """
    font = pygame.font.Font(None, 35)
    a = pygame.image.load("stuff/sprites/coin.png")
    scoretext = font.render("      x "+ str(coins), 1, (255, 255, 255))
    screen.blit(scoretext, (10, 15))
    
    points = font.render("Score 0"+ str(score), 1, (255, 255, 255))
    screen.blit(points, (640, 15))
    
    a = pygame.transform.scale(a, (30, 30))
    screen.blit(a, (12,11))
      
def back(screen):
    """Creates 3 surfaces for use as background for user info display"""
    a = pygame.Surface((150, 62), pygame.SRCALPHA)
    a.fill((0, 0, 0, 100))
    screen.blit(a, (7, 7))

    #b = pygame.Surface((120, 38), pygame.SRCALPHA)
    #b.fill((0, 0, 0, 100))
    #screen.blit(b, ((constants.SCREEN_WIDTH/2) - 5, 7))
    
    c = pygame.Surface((150, 38), pygame.SRCALPHA)
    c.fill((0, 0, 0, 100))
    screen.blit(c, (630, 7))

def message(screen, sign):
        """Displays wizard's message"""

        a = pygame.image.load('stuff/backgrounds/Frame.png')
        b = pygame.transform.scale(a, (500, 100))
        
        font = pygame.font.Font(None, 24) 

        message = font.render("You Must Bring Me The Gem", 1, (255, 255, 255))
        message2 = font.render("Before I Can Give You The Key!", 1,\
                                (255, 255, 255))

        
        if sign == True:
            screen.blit(b, (constants.SCREEN_WIDTH/2 - 250, \
                            constants.SCREEN_HEIGHT/2))
            screen.blit(message, (275, 330))
            screen.blit(message2, (275, 355))
        else:
            a.set_alpha(255,0)
            
def message2(screen, sign):
        """Displays wizard's message"""
        
        a = pygame.image.load('stuff/backgrounds/Frame.png')
        b = pygame.transform.scale(a, (500, 100))
        
        font = pygame.font.Font(None, 24) 

        message = font.render("You look tired. Go get some sleep.", 1,\
                               (255, 255, 255))
        
        if sign == True:
            screen.blit(b, (constants.SCREEN_WIDTH/2 - 250, \
                            constants.SCREEN_HEIGHT/2))
            screen.blit(message, (275, 330))
        else:
            a.set_alpha(255,0)
            
def door_mess(screen, sign):
        """Displays locked door message"""
        
        a = pygame.image.load('stuff/backgrounds/Frame.png')
        b = pygame.transform.scale(a, (500, 100))
        
        font = pygame.font.Font(None, 24) 

        message = font.render("You Need A Key. Talk to the Wizard!", 1,\
                               (255, 255, 255))
        
        if sign == True:
            screen.blit(b, (constants.SCREEN_WIDTH/2 - 250,\
                             constants.SCREEN_HEIGHT/2))
            screen.blit(message, (275, 340))
        else:
            a.set_alpha(255,0)
    
def sign(screen, sign):
        """Displays hint 1"""
        
        a = pygame.image.load('stuff/backgrounds/Frame.png')
        b = pygame.transform.scale(a, (500, 100))
        
        font = pygame.font.Font(None, 35) 

        message = font.render("Control using the WASD keys", 1,\
                               (255, 255, 255))
        message2 = font.render("Use the space key to throw snowballs", 1,\
                                (255, 255, 255))

        
        if sign == True:
            screen.blit(b, (constants.SCREEN_WIDTH/2 - 250,\
                             constants.SCREEN_HEIGHT/2))
            screen.blit(message, (225, 325))
            screen.blit(message2, (180, 355))
        else:
            a.set_alpha(255,0)
            
def sign2(screen, sign):
        """Displays hint 2"""
        
        a = pygame.image.load('stuff/backgrounds/Frame.png')
        b = pygame.transform.scale(a, (500, 100))
        
        font = pygame.font.Font(None, 35) 

        message = font.render("Home Sweet Home", 1, (255, 255, 255))

        
        if sign == True:
            screen.blit(b, (constants.SCREEN_WIDTH/2 - 250,\
                             constants.SCREEN_HEIGHT/2))
            screen.blit(message, (300, 330))
        else:
            a.set_alpha(255,0)

            