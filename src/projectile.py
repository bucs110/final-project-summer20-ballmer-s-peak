import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self,type, x, y, file):
        '''
        initializes the projectile class
        args: (int) x, (int) y, (string) file
        return: none
        '''
        # initialize the sprite's functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()
        self.type = type
        self.rect.x = x
        self.rect.y = y

    def getType(self):
        '''
        gets the type of projectile
        args: none
        return: string
        '''
        return self.type

    def move(self, speed):
        '''
        moves the projectible up the screen
        args: none
        return: none
        '''
        self.rect.y += speed
