import pygame
from sys import exit

pygame.init()

#Window Size
WINDOW_WIDTH = 1270
WINDOW_HEIGHT = 750
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Cadence of Love')

clock = pygame.time.Clock()


# #Here are the colors I use
WHITE = (255, 243, 253)
DARK_PINK = (185,88,152)
PURPLE = (222, 205, 247)
BLUE = (48, 162, 236)
BLACK = (0,0,0)

#Here are all the texts in the title screen and their positions on the screen.
font0 = pygame.font.Font('./start_screen/Domotika-Pro-Light-trial.ttf', 32)


# font = pygame.font.SysFont('arial', 60, bold=True)
start1_text = font0.render('Click Anywhere To Start', True, BLACK)
start1_text_rect = start1_text.get_rect()
start1_text_rect.midtop = (WINDOW_WIDTH // 2 - 6, 454)

# #I added spongebob and patty images for the game and placed them on the screen
start_image = pygame.image.load('./start_screen/start_image.png')
start_rect = start_image.get_rect()
start_rect.midleft = (320, WINDOW_HEIGHT // 2)

title_image = pygame.image.load('./start_screen/title.jpg')
title_rect = title_image.get_rect()
title_rect.midleft = (380, 355)


#I set up the background music
# pygame.mixer.music.play(-1, 0.0)
test_surface = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
screen.fill(WHITE)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    start_screen = True
    while start_screen:
        screen.blit(screen,(0,0))
        screen.blit(start_image, start_rect)
        screen.blit(title_image, title_rect)
        screen.blit(start1_text, start1_text_rect)
        pygame.display.update()

        for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                     start_screen = False
    while not start_screen:
        screen.blit(test_surface, (0,0))
        pygame.display.update()

    #This puts the writing and design on the screen.
    
    clock.tick(60)

pygame.quit()
