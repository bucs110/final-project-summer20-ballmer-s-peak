import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,imagefile,cords):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.left,self.rect.top = cords
