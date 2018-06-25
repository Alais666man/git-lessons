import pygame
from config import *


class Explosion(pygame.sprite.Sprite):
    def __init__(self, center):
        super().__init__()
        self.image = EXPLOSIONS_AN[0]
        self.rect = self.image.get_rect(center=center)
        self.frame = 0
        self.last_exp = pygame.time.get_ticks()
        self.frame_rate = 10

    def update(self):
        self.current = pygame.time.get_ticks()
        if self.current - self.last_exp > self.frame_rate:
            self.last_exp = self.current
            self.frame += 1
            if self.frame == len(EXPLOSIONS_AN):
                self.kill()
            else:
                self.image = EXPLOSIONS_AN[self.frame]
                self.rect = self.image.get_rect(center=self.rect.center)
