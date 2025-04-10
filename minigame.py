import pygame, random

class mc(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./minigame_images/mc.svg.png')
        self.rect = self.image.get_rect(midbottom = (360,500))
    def player_input(self):
        keys = pygame.key.get_pressed()
        if (keys[pygame.K_UP]) and self.rect.top > 160:
            self.rect.y -= 5
        if (keys[pygame.K_DOWN]) and self.rect.bottom < 750:
            self.rect.y += 5
        if (keys[pygame.K_LEFT]) and self.rect.left > 280:
            self.rect.x -= 5
        if (keys[pygame.K_RIGHT]) and self.rect.right < 995:
            self.rect.x += 5
    def update(self):
        self.player_input()


class dust(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('./minigame_images/dust.png')
        self.rect = self.image.get_rect(midbottom = (random.randint(280,995), random.randint(160,750)))