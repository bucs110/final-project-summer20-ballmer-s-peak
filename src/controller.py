import pygame
import sys
import random
import time
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
        self.background1 = background.Background("assets/background1.png",0,0)
        self.background1copy = background.Background("assets/background1copy.png",385,0)
        self.background2 = background.Background("assets/background2.png",0,-500)
        self.background2copy = background.Background("assets/background2copy.png",385,-500)
        self.clock = pygame.time.Clock()
        self.FPS = 30  # this final variable dictates the framerate at which the game should run
        self.difficulty = 5
        self.player = player.Player("Player 1", 250,375, "assets/player.png")
        self.enemies = pygame.sprite.Group()
        for i in range(1, 6):
            print(i)
            self.enemies.add(enemy.Enemy("Enemy", self.width / 6 * i, 20, "assets/enemy.png"))
        self.projectiles = pygame.sprite.Group()
        self.projectiles.add()
        self.state = "GAME"
        self.score = 0
        self.explosionSound = pygame.mixer.Sound("assets/game_explosion.ogg")
        self.gameOverSound = pygame.mixer.Sound("assets/game_gameover.ogg")
        pygame.mixer.music.load("assets/game_maintheme.ogg")
        pygame.mixer.music.set_volume(.2)
        pygame.mixer.music.play(-1)
        self.playagain = False
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
            elif self.state == "AGAIN":
                again = Controller()
                again.gameLoop()


    def gameLoop(self):
        '''
        The logic that decides what to draw after each frame
        args: none
        return: none
        '''
        pygame.key.set_repeat(1, 50)
        while self.state == "GAME":
            # print(len(self.enemies))
            if len(self.enemies) == 0:
                self.difficulty += 1
                for i in range(1, self.difficulty):
                    self.enemies.add(enemy.Enemy("Enemy", random.randrange(10, 600), random.randrange(20, 60), "assets/enemy.png"))
            for item in self.enemies:  # randomly makes the enemies shoot and move down towards the player
                randomInt = random.randrange(1800)
                if randomInt < 900:
                    item.move()
                if randomInt < 60:
                    self.projectiles.add(projectile.Projectile("enemy", item.rect.x + 60, item.rect.y + 16, "assets/projectile_laser.png"))

            for item in self.projectiles:  # projectile movement
                if item.getType() == "player":
                    item.move(-20)
                elif item.getType() == "enemy":
                    item.move(20)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

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
            playerhit = pygame.sprite.spritecollide(self.player,self.enemies,True)

            for i in playerhit:
                self.player.lowerHealth()
                self.score +=1

            for bullet in self.projectiles:
                if bullet.getType() == "player":
                    # kill the enemy if player's projectile hits it
                    enemyHit = pygame.sprite.spritecollide(bullet, self.enemies, True)
                    for i in enemyHit:
                        pygame.mixer.Sound.play(self.explosionSound)
                        self.score += 1
                        self.projectiles.remove(bullet)
                        print("The Score is:", self.score)
                elif bullet.getType() == "enemy":
                    isCollide = pygame.sprite.collide_rect(bullet, self.player)
                    if isCollide == True:
                        self.player.lowerHealth()
                        self.projectiles.remove(bullet)
            if(self.background1.rect.y >=500):
                self.background1.rect.y = -500
                self.background1copy.rect.y = -500
            if(self.background2.rect.y >=500):
                self.background2.rect.y = -500
                self.background2copy.rect.y = -500

            self.background1.rect.y += 4
            self.background1copy.rect.y += 4
            self.background2.rect.y += 4
            self.background2copy.rect.y += 4
            self.screen.fill((250, 250, 250))
            self.screen.blit(self.background1.image , self.background1.rect)
            self.screen.blit(self.background1copy.image , self.background1copy.rect)
            self.screen.blit(self.background2.image , self.background2.rect)
            self.screen.blit(self.background2copy.image , self.background2copy.rect)
            self.enemies.draw(self.screen)
            self.projectiles.draw(self.screen)
            self.screen.blit(self.player.image, self.player.rect.center)
            myfont = pygame.font.SysFont("8-Bit Madness",50)
            livesremaining = myfont.render("Lives: " + str(self.player.health),1,(255,0,0))
            self.screen.blit(livesremaining,(510,0))
            score = myfont.render("Score: " + str(self.score),1,(255,0,0))
            self.screen.blit(score,(0,0))
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
            pygame.mixer.Sound.play(self.gameOverSound)
            print("game over")
            print("Score : " + str(self.score))
            option = input("enter again to play again or quit to quit")
            if option == "again":
                self.state = "AGAIN"
            elif option == "quit":
                self.state = "GAME OVER"
                pygame.quit()
                sys.exit()
        #pass
