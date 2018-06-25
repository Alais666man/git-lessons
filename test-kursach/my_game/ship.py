import pygame

from config import *
from abc import abstractmethod
from shoot import Laser


class Ship(pygame.sprite.Sprite):
    def __init__(self, ):
        super().__init__()  #call Sprite initializer
        self.image = pygame.Surface((50, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT
        self.rect.x = SHIP_POS_X
        self.rect.y = SHIP_POS_Y
        self.frame = pygame.display.get_surface().get_size()
        self.health = 100
        self.delay = 150
        self.last_time_shoot = pygame.time.get_ticks()

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def shoot(self):
        pass


class ShipPlayer(Ship):
    def update(self):
        self.image = pygame.image.load('image/ship1.png')
        self.speed_x = 0
        self.speed_y = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.speed_x -= 8
        elif keys[pygame.K_RIGHT]:
            self.speed_x += 8
        elif keys[pygame.K_UP]:
            self.speed_y -= 8
        elif keys[pygame.K_DOWN]:
                self.speed_y += 8
        elif keys[pygame.K_SPACE]:
            self.shoot()

        self.rect.y += self.speed_y
        self.rect.x += self.speed_x

        if self.rect.right > SCREEN_WIDTH - 29:
            self.rect.right = SCREEN_WIDTH -29
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > SCREEN_HEIGHT -95:
            self.rect.bottom = SCREEN_HEIGHT -95
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        self.current = pygame.time.get_ticks()
        if self.current - self.last_time_shoot > self.delay:
            self.last_time_shoot = self.current
            self.laser = Laser(self.rect.centerx + 4, self.rect.bottom - 25)
            ALL_SPRITES.add(self.laser)
            LASER_SHOTS.add(self.laser)
            self.laser_sound = pygame.mixer.Sound('sound/Laser_Shoot9.ogg')
            self.laser_sound.set_volume(0.3)
            self.laser_sound.play()
