import pygame
from sys import exit

pygame.init()

#Window Size
WINDOW_WIDTH = 1270
WINDOW_HEIGHT = 750
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Cadence of Love')

clock = pygame.time.Clock()


#Here are the colors I use
WHITE = (255, 243, 253)
BLACK = (0,0,0)

#This is the font imported for the "click to start".
font = pygame.font.Font('./start_screen/Domotika-Pro-Light-trial.ttf', 32)

#Here the "click to start" is made a surface
start1_surface = font.render('Click Anywhere To Start', True, BLACK)

#I added the images used for the title screen and placed them on the screen
start_surface = pygame.image.load('./start_screen/start_image.png')
title_surface = pygame.image.load('./start_screen/title.jpg')


screen.fill(WHITE)
test_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
test_surface.fill(BLACK)


running = True
start_screen = True

while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #The start screen is loaded first, but when the mouse is pressed, it moves to the next display
        if event.type == pygame.MOUSEBUTTONDOWN:
            start_screen = False

    if start_screen:
        screen.blit(screen,(0,0))
        screen.blit(start_surface, (320, 160))
        screen.blit(title_surface, (380, 300))
        screen.blit(start1_surface, (465, 430))
                     
    else:
        screen.blit(test_surface, (0,0))
    
    clock.tick(60)
    pygame.display.update()

pygame.quit()
