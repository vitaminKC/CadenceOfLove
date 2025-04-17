import pygame
import minigame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1270, 750))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)



font = pygame.font.Font('./fonts/Sana.ttf', 32)
BLACK = (0, 0, 0)
PINK = (255, 243, 253)
BLUE = (72, 84, 233)



#minigame starting stats
mini_active = False
mini_end = False
counter = 30
score = 0
#background for minigame
mini_background = pygame.image.load('./minigame_images/classroom1.png')


#surfaces for the start screen
start1_surface = font.render('Click Anywhere To Start', True, PINK)
start_surface = pygame.image.load('./start_screen/start_image.png')
title_surface = pygame.image.load('./start_screen/title.jpg')



end_surface = font.render('END!', True, BLUE)

mc = pygame.sprite.GroupSingle()
mc.add(minigame.mc())

dust = pygame.sprite.Group()
dust.add(minigame.dust())

running = True
start_screen = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False    

    screen.fill(PINK)
    while start_screen:
        screen.blit(start_surface, (320, 160))
        screen.blit(title_surface, (380, 300))
        screen.blit(start1_surface, (465, 430))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                start_screen = False



    keys = pygame.key.get_pressed()
    if (keys[pygame.K_p]):
        mini_active = True
        while mini_active:
            for event in pygame.event.get():
                if event.type == pygame.USEREVENT: 
                    counter -= 1
                if event.type == pygame.QUIT: 
                    running = False 

            #This puts the writing and design on the screen.
            screen.blit(mini_background, (260,0))
            # score = collision_sprite(score)
            score = minigame.collision_sprite(score, mc, dust, minigame.dust)
            minigame.display_score(score, font, BLUE, screen)    
            counter = 30 - int(pygame.time.get_ticks() / 1000)
            minigame.display_time(counter, font, BLUE, screen)

            #This puts the images on the screen.
            mc.draw(screen)
            mc.update()
            dust.draw(screen)
            dust.update()
            pygame.display.update()

            if counter == 0:
                counter = 0
                mini_end = True
                mini_active = False

        while mini_end == True:
            screen.fill(PINK)
            screen.blit(end_surface, (450, 300))
            screen.blit(start1_surface, (465, 430))
            minigame.display_score(score, font, BLUE, screen)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                   running = False 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mini_end = False

    screen.fill(BLACK)
    pygame.display.update()        

    #These update the game and sets the frames per second.
    pygame.display.update()
    clock.tick(60)

pygame.quit()