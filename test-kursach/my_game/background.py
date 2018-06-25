from random import randrange, choice
from config import *


class StarBackGround(object):
    def __init__(self):
        self.screen = PY_SCREEN
        self.stars = []
        for i in range(MAX_STARS):
            star = [randrange(0, self.screen.get_width() - 1),
                    randrange(0, self.screen.get_height() - 1),
                    choice([1, 2, 3])
                    ]
            self.stars.append(star)

    def update(self):
        for star in self.stars:
            star[1] += star[2]
            if star[1] >= self.screen.get_height():
                star[1] = 0
                star[0] = randrange(0, self.screen.get_width())
                star[2] = choice([1, 2, 3])

    def draw_background(self):
        for star in self.stars:
            if star[2] == 1:
                color = (100, 100, 100)
            elif star[2] == 2:
                color = (190, 190, 190)
            elif star[2] == 3:
                color = (255, 255, 255)

            self.screen.fill(color, (star[0], star[1], star[2], star[2]))
