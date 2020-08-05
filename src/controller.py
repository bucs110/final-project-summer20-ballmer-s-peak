import pygame
import sys
import random
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
        self.background = pygame.image.load("assets/galaxy.png").convert()
        self.clock = pygame.time.Clock()
        self.FPS = 30  # this final variable dictates the framerate at which the game should run
        self.ENEMY_SPEED = 5
        self.player = player.Player("Player 1", 50, 80, "assets/player.png")
        self.enemies = pygame.sprite.Group()
        for i in range(0, 6):
            self.enemies.add(enemy.Enemy("Enemy", self.width / 5 * i, 20, "assets/enemy.png"))
        self.projectiles = pygame.sprite.Group()
        self.projectiles.add()
        self.enemyProjectiles = pygame.sprite.Group()
        self.state = "GAME"
        self.score = 0

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
            for item in self.enemies:
                randomInt = random.randrange(1800)
                if randomInt < 900:
                    item.move()
                if randomInt < 60:
                    self.projectiles.add(projectile.Projectile("enemy", item.rect.x + 60, item.rect.y + 16, "assets/projectile_laser.png"))
            for item in self.projectiles:  # Projectile movement
                if item.getType() == "player":
                    item.move(-20)
                elif item.getType() == "enemy":
                    item.move(20)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == "":
                    pass
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.player.move("y", "-1")
            if keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.player.move("y", "+1")
            if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.player.move("x", "-1", "assets/player_left.png")
            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.player.move("x", "+1", "assets/player_right.png")
            if keys[pygame.K_SPACE]:
                self.projectiles.add(projectile.Projectile("player", self.player.rect.x + 60, self.player.rect.y + 16, "assets/projectile_minigun.png"))
            if not keys[pygame.K_UP] and not keys[pygame.K_w] and not keys[pygame.K_DOWN] and not keys[pygame.K_s] and not keys[pygame.K_LEFT] and not keys[pygame.K_a] and not keys[pygame.K_RIGHT] and not keys[pygame.K_d]:
                self.player.changeImage("assets/player.png")

            for bullet in self.projectiles:
                if bullet.getType() == "player":
                    # kill the enemy if player's projectile hits it
                    enemyHit = pygame.sprite.spritecollide(bullet, self.enemies, True)
                    for i in enemyHit:
                        self.score += 1
                        print("The Score is:", self.score)
                elif bullet.getType() == "enemy":
                    isCollide = pygame.sprite.collide_rect(bullet, self.player)
                    if isCollide == True:
                        self.player.lowerHealth()
                        self.projectiles.remove(bullet)
                # if pygame.sprite.spritecollide(self.enemies, self.projectiles, True):
                #     self.projectiles.remove(bullet)
            # pygame.sprite.groupcollide(self.enemies, self.projectiles, False, True)   # Handles collisions between the projectile and enemies
            self.screen.fill((250, 250, 250))
            self.screen.blit(self.background , (0, 0))
            self.enemies.draw(self.screen)
            self.projectiles.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect.center)
            pygame.display.flip()
            self.clock.tick(self.FPS)
            self.gameOver()



    def gameOver(self):
        '''
        Logic that decides what to do at the end of the game
        args: none
        return: none
        '''
        if self.player.checkHealth() == True:
            print ("game over")
            self.state = "Game Over"
            pygame.quit()
            sys.exit()
        #pass
