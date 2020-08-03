import pygame
import sys
from src import player
from src import enemy
from src import projectile
from src import background

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
        self.background = background.Background("assets/galaxy.png",(0,0))
        self.clock = pygame.time.Clock()
        self.FPS = 30  # this final variable dictates the framerate at which the game should run
        self.player = player.Player("Player 1", 50, 80, "assets/player.png")
        self.enemies = pygame.sprite.Group()
        self.enemies.add(enemy.Enemy("Enemy", 200, 50, "assets/asteroid.png"))
        self.projectiles = pygame.sprite.Group()
        self.projectiles.add(projectile.Projectile(500, 400, "assets/projectile_minigun.png"))
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
            for item in self.projectiles:
                item.move()  # Tells the bullets to move forward
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            keys = pygame.key.get_pressed()
            print(keys)
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.player.move("y", "-1")
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player.move("y", "+1")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move("x", "-1", "assets/player_left.png")
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move("x", "+1", "assets/player_right.png")
            if keys[pygame.K_SPACE]:
                print(self.player.rect.x)
                self.projectiles.add(projectile.Projectile(self.player.rect.x + 60, self.player.rect.y + 16, "assets/projectile_minigun.png"))
            if not keys[pygame.K_UP] and not keys[pygame.K_w] and not keys[pygame.K_DOWN] and not keys[pygame.K_s] and not keys[pygame.K_LEFT] and not keys[pygame.K_a] and not keys[pygame.K_RIGHT] and not keys[pygame.K_d]:
                self.player.changeImage("assets/player.png")

            self.screen.fill((250, 250, 250))
            self.screen.blit(self.background.image, self.background.rect)
            self.enemies.draw(self.screen)
            self.projectiles.draw(self.screen)
            print(self.player.image)
            self.screen.blit(self.player.image, self.player.rect.center)
            pygame.display.flip()
            self.clock.tick(self.FPS)



    def gameOver(self):
        '''
        Logic that decides what to do at the end of the game
        args: none
        return: none
        '''
        pass
