import pygame, random


pygame.init()

#Window Size
WINDOW_WIDTH = 1270
WINDOW_HEIGHT = 750
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Cadence of Love')

clock = pygame.time.Clock()

#starting stats
PLAYER_VELOCITY = 40
score = 0
BUFFER_DISTANCE = 100
counter = 30

pygame.time.set_timer(pygame.USEREVENT, 1000)

#colors
BLACK = (0,0,0)
# PURPLE = (222, 205, 247)
# BLUE = (48, 162, 236)
# BROWN = (80, 30, 30)

font = pygame.font.Font('./start_screen/Domotika-Pro-Light-trial.ttf', 32)

score_surface = font.render('score: ' + str(score), True, BLACK)
time_surface = font.render('time: ' + str(counter), True, BLACK)
end_surface = font.render('END!', True, BLACK)


# #I added the images used for the title screen and placed them on the screen
room_surface = pygame.image.load('./minigame_images/classroom1.png')

mc_image = pygame.image.load('./minigame_images/mc.svg.png')
mc_rect = mc_image.get_rect()
mc_rect.midleft = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

dust_image = pygame.image.load('./minigame_images/dust.png')
dust_rect = dust_image.get_rect()
dust_rect.x = random.randint(260, 1010)
dust_rect.y = random.randint(64, WINDOW_HEIGHT-30)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
        if event.type == pygame.QUIT: 
            running = False
            
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP]) and mc_rect.top > 130:
        mc_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_DOWN]) and mc_rect.bottom < WINDOW_HEIGHT:
        mc_rect.y += PLAYER_VELOCITY
    if (keys[pygame.K_LEFT]) and mc_rect.left < 260:
        mc_rect.x -= PLAYER_VELOCITY
    if (keys[pygame.K_RIGHT]) and mc_rect.right < WINDOW_WIDTH-260:
        mc_rect.x += PLAYER_VELOCITY


    #When mc collides with dust, a point is gained
    if mc_rect.colliderect(dust_rect):
        score += 1
        dust_rect.x = random.randint(100, WINDOW_WIDTH-BUFFER_DISTANCE)
        dust_rect.y = random.randint(60, WINDOW_HEIGHT-BUFFER_DISTANCE)
    
    score_surface = font.render('score: ' + str(score), True, BLACK)
    time_surface = font.render('time: ' + str(counter), True, BLACK)

    #When the player has no more lives, the end screen appears
    if counter == 0:
        screen.blit(end_surface, (380, 300))
        pygame.display.update()

        #The music stops when they lose, but when they press a key to play again, the stats are reset and the music starts again
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #exit minigame
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #This puts the writing and design on the screen.
    screen.blit(room_surface, (260,0))
    screen.blit(score_surface, (560, 70))
    screen.blit(time_surface, (560, 40))

    #This puts the images on the screen.
    screen.blit(mc_image, mc_rect)
    screen.blit(dust_image, dust_rect)

    #These update the game and sets the frames per second.
    pygame.display.update()
    clock.tick(60)

pygame.quit()