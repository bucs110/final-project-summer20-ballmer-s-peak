import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, file):

        # initialize the sprite's functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 20

    def move(self):
        '''
        moves the projectible up the screen
        args: none
        return: none
        '''
        self.rect.y -= self.speed
