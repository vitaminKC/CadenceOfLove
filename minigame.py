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


def collision_sprite(score, mc, dust, dust_class):
    if pygame.sprite.spritecollide(mc.sprite, dust, True):
        score += 1
        dust.add(dust_class())
    return score

def display_score(score, font, BLUE, screen):
    score_surf = font.render(f'Score: '+str(score),False,BLUE)
    score_rect = score_surf.get_rect(center = (560,95))
    screen.blit(score_surf,score_rect)


def display_time(counter, font, BLUE, screen):
    time_surf = font.render(f'Time: {counter}',False,BLUE)
    time_rect = time_surf.get_rect(center = (560,60))
    screen.blit(time_surf,time_rect)