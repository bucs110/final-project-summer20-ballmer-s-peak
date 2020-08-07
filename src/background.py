import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self,imagefile,x,y):
        '''
        initializes the background sprite
        args: (string) imagefile, (int) x, (int) y
        return: none
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagefile)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
