import pygame
import cadence
from sys import exit

pygame.init()

spriteX = 300
spriteY = 10

screen = pygame.display.set_mode((1270, 750))
clock = pygame.time.Clock()

#background/foreground surfaces
background = pygame.image.load('./background/classroom.png')
scaled_bg = pygame.transform.scale(background, (1270, 750))
textbox = pygame.image.load('./misc/textbox.png')
scaled_box = pygame.transform.scale(textbox, (1150, 320))
textFont = pygame.font.Font

#Cadence emotions
sprite0 = pygame.image.load('./uniform_sprites/normal_c.png').convert_alpha()
sprite1 = pygame.image.load('./uniform_sprites/normal_o.png').convert_alpha()
sprite2 = pygame.image.load('./uniform_sprites/excited_c.png').convert_alpha()
sprite3 = pygame.image.load('./uniform_sprites/excited_o.png').convert_alpha()
sprite4 = pygame.image.load('./uniform_sprites/angry_c.png').convert_alpha()
sprite5 = pygame.image.load('./uniform_sprites/angry_o.png').convert_alpha()
sprite6 = pygame.image.load('./uniform_sprites/upset_c.png').convert_alpha()
sprite7 = pygame.image.load('./uniform_sprites/upset_o.png').convert_alpha()
sprite8 = pygame.image.load('./uniform_sprites/shy_c.png').convert_alpha()
sprite9 = pygame.image.load('./uniform_sprites/shy_o.png').convert_alpha()
sprite10 = pygame.image.load('./uniform_sprites/flustered_c.png').convert_alpha()
sprite11 = pygame.image.load('./uniform_sprites/flustered_o.png').convert_alpha()

#Cadence sprites
normalC = cadence.Cadence(sprite0)
normalO = cadence.Cadence(sprite1)
exictedC = cadence.Cadence(sprite2)
excitedO = cadence.Cadence(sprite3)
angryC = cadence.Cadence(sprite4)
angryO = cadence.Cadence(sprite5)
upsetC = cadence.Cadence(sprite6)
upsetO = cadence.Cadence(sprite7)
shyC = cadence.Cadence(sprite8)
shyO = cadence.Cadence(sprite9)
flusteredC = cadence.Cadence(sprite10)
flusteredO = cadence.Cadence(sprite11)

emotions = [normalC, normalO, exictedC, excitedO, angryC, angryO, upsetC, upsetO, shyC, shyO, flusteredC, flusteredO]

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(scaled_bg, (0, 0))
    sprite = emotions[0]
    screen.blit(sprite.getImage(), (spriteX, spriteY))
    screen.blit(scaled_box, (60, 455))


        
    
    pygame.display.update()
    

    clock.tick(60)