import pygame


TITLE = 'Space Bustard'
FPS = 60

"""Screen and background"""
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 735

SHIP_POS_X = (SCREEN_WIDTH * 0.45)
SHIP_POS_Y = (SCREEN_HEIGHT * 0.7)
SHIP_LOCATION = (SHIP_POS_X, SHIP_POS_Y)

MAX_STARS = 200

PY_SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

"""Colors"""
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

"""Sprites"""
ALL_SPRITES = pygame.sprite.Group()
ENEMY_SHIPS = pygame.sprite.Group()
LASER_SHOTS = pygame.sprite.Group()

HEALTH_BAR_LEN = 100
HEALTH_BAR_HEIGHT = 10
SHIP_HEALTH = 100

EXPLOSIONS_AN = [pygame.image.load('image/explosions/explosion0.png'),
                 pygame.image.load('image/explosions/explosion1.png'),
                 pygame.image.load('image/explosions/explosion2.png'),
                 pygame.image.load('image/explosions/explosion3.png'),
                 pygame.image.load('image/explosions/explosion4.png'),
                 pygame.image.load('image/explosions/explosion5.png'),
                 pygame.image.load('image/explosions/explosion6.png'),
                 pygame.image.load('image/explosions/explosion7.png'),
                 pygame.image.load('image/explosions/explosion8.png'),
                 pygame.image.load('image/explosions/explosion9.png'),
                 pygame.image.load('image/explosions/explosion10.png'),
                 pygame.image.load('image/explosions/explosion11.png'),
                 pygame.image.load('image/explosions/explosion12.png'),
                 pygame.image.load('image/explosions/explosion13.png'),
                 pygame.image.load('image/explosions/explosion14.png'),
                 pygame.image.load('image/explosions/explosion15.png')
                 ]
