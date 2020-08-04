import pygame
from src import projectile

class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y, file):
        '''
        initializes the enemy sprite
        args: (string) name, (int) x, (int) y, (string) file
        return: none
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name

    def shoot(self, projectilesGroup):
        pass
    def move(self):
        self.rect.y += 1

    def getProjectiles(self):
        pass
