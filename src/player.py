import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, file):
        '''
        initializes the player sprite
        args: (string) name, (int) x, (int) y, (string) file
        return: none
        '''
        # initialize the sprite's functionality
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.name = name
        self.speed = 5

    def move(self, axis, direction, file="assets/player.png"):
        '''
        moves to player based off its passed parameters
        args: (string) axis, (string) direction
        return: none
        '''
        print("moved player")
        if axis == "x" and direction == "+1" and self.rect.x <550:
            self.rect.x += self.speed
            self.changeImage(file)
        elif axis == "x" and direction == "-1" and self.rect.x > -35:
            self.rect.x -= self.speed
            self.changeImage(file)
        elif axis == "y" and direction == "+1" and self.rect.y < 390:
            self.changeImage(file)
            self.rect.y += self.speed
        elif axis == "y" and direction == "-1" and self.rect.y > -35:
            self.rect.y -= self.speed
            self.changeImage(file)

    def changeImage(self, file):
        '''
        changes the sprite of the player to help with animation
        args: (string) file
        return: none
        '''
        self.image = pygame.image.load(file).convert_alpha()
