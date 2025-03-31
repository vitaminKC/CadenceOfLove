import pygame, random

pygame.init()

#Window Size
WINDOW_WIDTH = 1270
WINDOW_HEIGHT = 750
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Cadence of Love')

clock = pygame.time.Clock()

#starting stats
PLAYER_VELOCITY = 15
score = 0
counter = 30

pygame.time.set_timer(pygame.USEREVENT, 1000)

#colors
BLACK = (0, 0, 0)


font = pygame.font.Font('./start_screen/Sana Sans Alt W00 Regular.ttf', 32)

score_surface = font.render('Score: ' + str(score), True, BLACK)
time_surface = font.render('Time: ' + str(counter), True, BLACK)
end_surface = font.render('END!', True, BLACK)


# #I added the images used for the title screen and placed them on the screen
room_surface = pygame.image.load('./minigame_images/classroom1.png')

mc_image = pygame.image.load('./minigame_images/mc.svg.png')
mc_rect = mc_image.get_rect()
mc_rect.midleft = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

dust_image = pygame.image.load('./minigame_images/dust.png')
dust_rect = dust_image.get_rect()
dust_rect.x = random.randint(280, WINDOW_WIDTH-280)
dust_rect.y = random.randint(260, WINDOW_HEIGHT-30)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT: 
            counter -= 1
        if event.type == pygame.QUIT: 
            running = False
            
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_UP]) and mc_rect.top > 160:
        mc_rect.y -= PLAYER_VELOCITY
    if (keys[pygame.K_DOWN]) and mc_rect.bottom < WINDOW_HEIGHT:
        mc_rect.y += PLAYER_VELOCITY
    if (keys[pygame.K_LEFT]) and mc_rect.left > 280:
        mc_rect.x -= PLAYER_VELOCITY
    if (keys[pygame.K_RIGHT]) and mc_rect.right < WINDOW_WIDTH-275:
        mc_rect.x += PLAYER_VELOCITY


    #When mc collides with dust, a point is gained
    if mc_rect.colliderect(dust_rect):
        score += 1
        dust_rect.x = random.randint(280, WINDOW_WIDTH-290)
        dust_rect.y = random.randint(250, WINDOW_HEIGHT-100)
    
    score_surface = font.render('Score: ' + str(score), True, BLACK)
    time_surface = font.render('Time: ' + str(counter), True, BLACK)

    #When the player has no more lives, the end screen appears
    if counter == 0:
        counter = 0
        screen.blit(end_surface, (380, 300))
        pygame.display.update()

        #The music stops when they lose, but when they press a key to play again, the stats are reset and the music starts again
        is_paused = True
        while is_paused:
            PLAYER_VELOCITY = 0
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    #exit minigame
                    is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    running = False

    #This puts the writing and design on the screen.
    screen.blit(room_surface, (260,0))
    screen.blit(score_surface, (520, 75))
    screen.blit(time_surface, (520, 40))

    #This puts the images on the screen.
    screen.blit(mc_image, mc_rect)
    screen.blit(dust_image, dust_rect)

    #These update the game and sets the frames per second.
    pygame.display.update()
    clock.tick(60)

pygame.quit()