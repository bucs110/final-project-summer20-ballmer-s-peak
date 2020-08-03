import pygame
import sys
from src import player
from src import enemy

class Controller:
    def __init__(self, width=640, height=480):
        '''
        Initializes the sprites and creates the initial screen
        args: optional (int) width, optinal (int) height
        return: none
        '''
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.background = pygame.Surface(self.screen.get_size()).convert()
        self.clock = pygame.time.Clock()
        self.FPS = 30  # this final variable dictates the framerate at which the game should run
        self.player = player.Player("Player 1", 50, 80, "assets/player.png")
        self.enemies = pygame.sprite.Group()
        self.enemies. add(enemy.Enemy("Enemy", 200, 50, "assets/asteroid.png"))
        self.state = "GAME"
        print(self.state)

    def mainLoop(self):
        '''
        Runs the game
        args: none
        return: none
        '''
        while True:
            if (self.state == "GAME"):
                self.gameLoop()
            elif self.state == "GAME OVER":
                self.gameOver()

    def gameLoop(self):
        '''
        The logic that decides what to draw after each frame
        args: none
        return: none
        '''
        pygame.key.set_repeat(1, 50)
        while self.state == "GAME":
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.player.move("y", "-1")
                    elif event.key == pygame.K_DOWN:
                        self.player.move("y", "+1")
                    elif event.key == pygame.K_LEFT:
                        self.player.move("x", "-1")
                    elif event.key == pygame.K_RIGHT:
                        self.player.move("x", "+1")

            self.background.fill((250, 250, 250))
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.player.image, self.player.rect.center)
            self.enemies.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(self.FPS)



    def gameOver(self):
        '''
        Logic that decides what to do at the end of the game
        args: none
        return: none
        '''
        pass
