"""Module that defines basic parts of game like:
    - Player Stats
    - Player Score
    - Pause
    - Death Screen
    - intro
    - main()
"""

import pygame
import platformer.constants as constants
import platformer.levels as levels
import platformer.messages as messages
from random import randint
from platformer.player import Player

#initialize pygame
pygame.init()

#initialize the font
pygame.font.init()

# Set the height and width of the screen
size = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
#screen = pygame.display.set_mode(size)

pygame.display.set_caption("Rocky Raccoon - 2D Platform Game")
clock = pygame.time.Clock()


def sleeping(screen, sleep, player):
    """displays sleeping cloud"""
    
    a = pygame.image.load('stuff/backgrounds/dream_cloud.png')
    a = pygame.transform.scale(a, (70, 65))

    font = pygame.font.Font(None, 17)
    font2 = pygame.font.Font(None, 100)
    
    message = font.render('ZZzzz', 1, (255, 255, 255))
    
    end_message = font2.render('Level Complete', 1, (randint(0,255), \
                                                         randint(0,255), \
                                                         randint(0,255)))
    
    if sleep == True:
        screen.blit(a, (player.rect.x + 150, player.rect.y - 70))
        screen.blit(message, (player.rect.x + 168, player.rect.y - 55))
        screen.blit(end_message, (constants.SCREEN_WIDTH/2 - 250, \
                                  constants.SCREEN_HEIGHT/2))
    else:
        a.set_alpha(255,0)
    
    button("Play Again!",200,450,100,50,constants.GREEN2,\
               constants.GREEN, game_Intro)
    button("Quit",400,450,100,50,constants.RED2,constants.RED, quitGame)
    

def texts2(score, coins):
    """Displays Game Over Text."""
    a = pygame.image.load('stuff/sprites/death_racccoon.png')
    largeText = pygame.font.SysFont("comicsansms",115)
    smallText = pygame.font.SysFont('comicsansms', 25)
    TextSurf, TextRect = text_objects("You Died", largeText)
    TextSurf2, TextRect2 = text_objects("Score: " + str(score), smallText)
    TextSurf3, TextRect3 = text_objects("Coins Collected: " + str(coins),\
                                         smallText)
    TextRect.center = ((constants.SCREEN_WIDTH/2), (constants.SCREEN_HEIGHT/2)\
                        - 230)
    TextRect2.center = ((constants.SCREEN_WIDTH/2), (constants.SCREEN_HEIGHT/2)\
                         + 185)
    TextRect3.center = ((constants.SCREEN_WIDTH/2), (constants.SCREEN_HEIGHT/2)\
                         + 220)

    while True:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        screen.fill(constants.WHITE)
        screen.blit(a, ((constants.SCREEN_WIDTH/2) - 185, \
                        (constants.SCREEN_HEIGHT/2 - 175)) )
        screen.blit(TextSurf, TextRect)
        screen.blit(TextSurf2, TextRect2)
        screen.blit(TextSurf3, TextRect3)
        

        button("Play Again!",150,450,100,50,constants.GREEN2,\
               constants.GREEN, main)
        button("Quit",550,450,100,50,constants.RED2,constants.RED, quitGame)

        pygame.display.update()
        clock.tick(15) 

def unpause():
    global pause
    pause = False

def paused(player):
    largeText = pygame.font.SysFont("comicsansms",115)
    TextSurf, TextRect = text_objects("Paused", largeText)
    TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/2))
    messages.texts(screen, player.score, player.coins)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        #screen.fill(constants.WHITE)
        screen.blit(TextSurf, TextRect)

        button("Continue",150,500,100,50,constants.GREEN2,constants.GREEN,\
                unpause)
        button("Quit",550,500,100,50,constants.RED2,constants.RED, quitGame)

        pygame.display.update()
        clock.tick(15)  

def button(msg, x, y, w, h, ic, ac, action=None):
    """function for buttons"""
    pygame.font.init()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def text_objects(text, font):
    textSurface = font.render(text, True, constants.BLACK)
    return textSurface, textSurface.get_rect()

def text_objects2(text, font):
    textSurface = font.render(text, True, constants.WHITE)
    return textSurface, textSurface.get_rect()

def game_Intro():
    intro = True
    #pygame.mixer.music.load('stuff/sounds/RockyRaccoon.wav')
    #pygame.mixer.music.play(-1)
    
    python_logo = pygame.image.load('stuff/backgrounds/python-powered.png')
    python_logo = pygame.transform.scale(python_logo, (100, 110))
    
    pygame_logo = pygame.image.load('stuff/backgrounds/pygame_logo.png')
    pygame_logo = pygame.transform.scale(pygame_logo, (170, 70))
    
    
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quitGame()
        
        screen.fill(constants.BLACK)
        largeText = pygame.font.SysFont('comicsansms', 115)
        TextSurf, TextRect = text_objects2("Rocky Raccoon", largeText)
        TextRect.center = ((constants.SCREEN_WIDTH/2),(constants.SCREEN_HEIGHT/\
                                                       2) - 100)
        screen.blit(TextSurf, TextRect) 
        
        
        button("GO!",250,340,100,50,constants.GREEN2,constants.GREEN, main)
        button("Quit",450,340,100,50,constants.RED2,constants.RED, quitGame)
        
        screen.blit(python_logo, (15, 470))
        screen.blit(pygame_logo, (constants.SCREEN_WIDTH - 180, 500))
        
        pygame.display.update()
        clock.tick(15)

def displayitem(screen, haveGem, haveKey):
    """Displays item player is currently holding
        Displays text on top right corner of screen.
    """
    if haveGem == True:
        a = pygame.image.load('stuff/objects/gem.png')
        a = pygame.transform.scale(a, (50, 50))
        screen.blit(a, (110, 27))
        
    elif haveKey == True:
        a = pygame.image.load('stuff/objects/key.png')
        screen.blit(a, (120, 27))
    
def quitGame():
    pygame.quit()
    quit()

def HealthBar(screen, health):
    """Displays Hearts (player health).
    
    It loads 4 distinct images of heart levels and displays
        according to the number of health points remaining.
    
    Args:
        screen: The initialized screen used to display content. 
        health: The current number of health; ranges from 3-0.
    
    Returns:
        Displays hearts image on top right corner of screen, below score.
    """
    hearts = []
    d = pygame.image.load("stuff/hearts/heart0.png")
    hearts.append(d)
    c = pygame.image.load("stuff/hearts/heart1.png")
    hearts.append(c)
    b = pygame.image.load("stuff/hearts/heart2.png")
    hearts.append(b)
    a = pygame.image.load("stuff/hearts/heart3.png")
    hearts.append(a)
        
    if health < 0:
        health = 0
    image = hearts[health]
    screen.blit(image, (15, 45))

def main():
    """This is the main program. It initializes pygame and sets the
    screen attributes. The player and the levels are created. The Main
    program loop checks user events and performs appropriate action. 
     """
    global pause
    
    # Create the player
    player = Player()

    # Create all the levels
    level_list = []
    level_list.append(levels.Level_01(player))
    level_list.append(levels.Level_02(player))

    # Set the current level
    current_level_no = 0
    current_level = level_list[current_level_no]

    active_sprite_list = pygame.sprite.Group()
    player.level = current_level

    player.rect.x = 65
    player.rect.y = 510
    active_sprite_list.add(player)
    
    #list of bullets
    bullet_list = pygame.sprite.Group()

    #Loop until the user clicks the close button.
    done = False
    
    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()
    
   # hurt_sound = pygame.mixer.Sound('stuff/sounds/hurt.wav')
   # jump_sound = pygame.mixer.Sound('stuff/sounds/jump2.wav')
    
    # -------- Main Program Loop -----------
    while not done:        
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done = True # Flag that we are done so we exit this loop

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    player.go_left()
                if event.key == pygame.K_d:
                    player.go_right()
                if event.key == pygame.K_w:
                   # pygame.mixer.Sound.play(jump_sound)
                    player.jump()
                if event.key == pygame.K_SPACE:
                    bullet = player.shoot()
                    active_sprite_list.add(bullet)
                    bullet_list.add(bullet)
                if event.key == pygame.K_p:
                    pause = True
                    paused(player)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a and player.change_x < 0:
                    player.stop()
                elif event.key == pygame.K_d and player.change_x > 0:
                    player.stop()
                elif event.key == pygame.K_w:
                    if event.key == pygame.KEYDOWN:
                        if event.key == pygame.K_d and player.change_x < 0:
                            player.go_right
                            player.jump()
                        if event.key == pygame.K_a and player.change_x > 0:
                            player.go_LEFT
                            player.jump()

        # Update the player.
        active_sprite_list.update()

        # Update items in the level
        current_level.update()


        # Checks if player is hurt
        #if player.hurt_sound == True:
           # pygame.mixer.Sound.play(hurt_sound)
          #  player.hurt_sound = False

        
        # If the player gets near the right side, shift the world left (-x)
        if player.rect.x >= 500:
            diff = player.rect.x - 500
            player.rect.x = 500
            current_level.shift_world(-diff)

        # If the player gets near the left side, shift the world right (+x)
        if player.rect.x <= 120:
            diff = 120 - player.rect.x
            player.rect.x = 120
            current_level.shift_world(diff)
            
       
            
        # If the player gets to the end of the level, go to the next level
        #current_position = player.rect.x + current_level.world_shift
        if player.igloo == True:
            if current_level_no < len(level_list)-1:
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
        
        
        
        # controls the display of all distinct messages in game
        if player.sign1 == True:
            messages.sign(screen, True)
        elif player.sign2 == True:
            messages.sign2(screen, True)
        else:
            messages.sign(screen, False)
            messages.sign2(screen, False)
            
            
        if player.wizard_message == True:
            messages.message(screen, True)
        else:
            messages.message(screen, False)
            
            
        if player.wizard_message2 == True:
            messages.message2(screen, True)
        else:
            messages.message2(screen, False)
            
            
        if player.door_message == True and player.door_locked == True:
            messages.door_mess(screen, True)
        elif player.door_message == False:
            messages.door_mess(screen, False)

        #a = time(screen, t, player)
        #if a == True:
            #player.kill()
        messages.texts(screen, player.score, player.coins)
        
        if player.alive() != True and player.complete != True:
            texts2(player.score, player.coins)
            
        if player.complete == True:
            sleeping(screen, True, player)
        pygame.display.flip()

        
        # ALL CODE TO DRAW SHOULD GO BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
        messages.back(screen)
        HealthBar(screen, player.health)
        displayitem(screen, player.haveGem, player.haveKey)
        
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT

        clock.tick(30)
        
    pygame.quit()

if __name__ == "__main__":
    game_Intro()
    
