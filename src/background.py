import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,imagefile,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
