#Imports
import pygame
import sys
from pygame.locals import *
import random
import time

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
coins_count = 0
r = 0

#coin settings
coin_original = pygame.image.load("./lab9/res/coin.png")
coin3_original = pygame.image.load("./lab9/res/coin3.png")
coin5_original = pygame.image.load("./lab9/res/coin5.png")
coin_scaled = pygame.transform.scale(coin_original, (30, 30))
coin_scaled3 = pygame.transform.scale(coin3_original, (30, 30))
coin_scaled5 = pygame.transform.scale(coin5_original, (30, 30))

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
background = pygame.image.load("./lab9/res/AnimatedStreet.png")

#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./lab9/res/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self, image, value):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.value = value
        self.rect.centerx = random.randint(40, SCREEN_WIDTH - 40)
        self.rect.top = 0
    
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()
          
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("./lab9/res/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
        
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

#Setting up Sprites        
P1 = Player()
E1 = Enemy()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Game Loop
while True:   
    #Cycles through all events occuring  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
            random_number = random.randint(1, 100)
            if random_number <= 60:  # 60% chance for coin1
                coin = Coin(coin_scaled, 1)
            elif random_number <= 90:  # 30% chance for coin3
                coin = Coin(coin_scaled3, 3)
            else:  # 10% chance for coin5
                coin = Coin(coin_scaled5, 5)
            coins.add(coin)
            all_sprites.add(coin)      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    #scores and coins on screen
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coinss = font_small.render(str(coins_count), True, BLACK)
    DISPLAYSURF.blit(coinss, (355, 5))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)
        DISPLAYSURF.blit(coin_scaled, (320, 0))
        
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('./lab9/res/crash.wav').play()
        time.sleep(1)           
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))    
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(2)
        pygame.quit()
        sys.exit() 

    #coin cillecting
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    for coin in collected_coins:
        pygame.mixer.Sound("./lab9/res/coin_collect.mp3").play()
        coins_count += coin.value   
    
    pygame.display.update()
    FramePerSec.tick(FPS)
