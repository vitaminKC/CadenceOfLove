import pygame
from sys import exit
pygame.init()
screen = pygame.display.set_mode((1270, 750))
clock = pygame.time.Clock()
test_sprite = pygame.image.load('./uniform_sprites/excited_c.png')
scaled = pygame.transform.scale(test_sprite, (700, 700))
background = pygame.image.load('./background/classroom.png')
scaled_bg = pygame.transform.scale(background, (1270, 750))

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(scaled_bg, (0, 0))
    screen.blit(scaled, (300, 100))
    
    pygame.display.update()
    clock.tick(60)