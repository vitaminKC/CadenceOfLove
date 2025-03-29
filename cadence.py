import pygame

spriteDimensions = 700
spriteX = 300
spriteY = 70

class Cadence():
    def __init__(self, img):
        # pygame.sprite.Sprite.__init__(self)
        self.image = img
        self.image = pygame.transform.scale(self.image, (spriteDimensions, spriteDimensions))
        # self.rect = self.image.get_rect(midbottom = c)

    def getImage(self):
        return self.image