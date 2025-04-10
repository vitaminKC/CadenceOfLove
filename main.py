import pygame
import minigame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((1270, 750))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)

font = pygame.font.Font('./start_screen/Sana Sans Alt W00 Regular.ttf', 32)
BLACK = (0, 0, 0)

mini_active = False
counter = 30
score = 0

#background surface
mini_background = pygame.image.load('./minigame_images/classroom1.png')

def collision_sprite(score):
    if pygame.sprite.spritecollide(mc.sprite,dust,True):
        score += 1
        dust.add(minigame.dust())
    return score

def display_score(score):
    score_surf = font.render(f'Score: '+str(score),False,BLACK)
    score_rect = score_surf.get_rect(center = (560,95))
    screen.blit(score_surf,score_rect)

def display_time(counter):
    time_surf = font.render(f'Time: {counter}',False,BLACK)
    time_rect = time_surf.get_rect(center = (560,60))
    screen.blit(time_surf,time_rect)


end_surface = font.render('END!', True, BLACK)

mc = pygame.sprite.GroupSingle()
mc.add(minigame.mc())

dust = pygame.sprite.Group()
dust.add(minigame.dust())

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False    

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
            score = collision_sprite(score)
            display_score(score)    
            counter = 30 - int(pygame.time.get_ticks() / 1000)
            display_time(counter)

            #This puts the images on the screen.
            mc.draw(screen)
            mc.update()
            dust.draw(screen)
            dust.update()
            pygame.display.update()

            if counter == 0:
                counter = 0
                mini_active = False

    screen.blit(end_surface, (380, 300))
    pygame.display.update()        

    #These update the game and sets the frames per second.
    pygame.display.update()
    clock.tick(60)

pygame.quit()