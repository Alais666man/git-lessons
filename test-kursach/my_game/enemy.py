import pygame
from random import randrange
from abc import abstractmethod
from config import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(SCREEN_WIDTH - self.rect.width)
        self.rect.y = randrange(-100, -40)
        self.speed_y = randrange(1, 6)

    @abstractmethod
    def update(self):
        pass


class EnemyShip(Enemy):
    def update(self):
        self.image = pygame.image.load('image/antmaker.png')
        self.rect.y += self.speed_y
        if self.rect.top > SCREEN_HEIGHT + 10 or self.rect.left < -25 or self.rect.right > SCREEN_WIDTH + 20:
            self.rect.x = randrange(SCREEN_WIDTH - self.rect.width)
            self.rect.y = randrange(-100, -40)
            self.speed_y = randrange(1, 8)
