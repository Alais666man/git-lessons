import pygame

from ship import *
import background
from config import *
from enemy import *
from explosions import *


class MyGame:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        self.screen = PY_SCREEN
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.running = True

    def sprite(self):
        """All graphics"""
        self.all_sprites = ALL_SPRITES
        self.enemy_ships = ENEMY_SHIPS
        self.laser_shots = LASER_SHOTS

        self.background = background.StarBackGround()
        self.ship = ShipPlayer()

        self.all_sprites.add(self.ship)

        # enemies in one time
        for i in range(6):
            self.enemy()
            self. score = 0
        self.run()

    def run(self):
        """Game loop"""
        pygame.mixer.music.load('sound/Thistle.ogg')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(loops=-1)

        self.game = True
        while self.game:
            self.screen.fill(BLACK)
            self.clock.tick(FPS)

            self.event()
            self.update()

            self.draw()

    def update(self):
        """Sprites and colisions updates"""
        self.all_sprites.update()
        hits = pygame.sprite.spritecollide(self.ship, self.enemy_ships, True)

        for hit in hits:
            self.ship.health -= 25
            self.explosion_an = Explosion(hit.rect.center)

            self.enemy()
            self.all_sprites.add(self.explosion_an)

            if self.ship.health <= 0:
                self.game = False

        self.explosion_sounds = pygame.mixer.Sound('sound/Explosion30.ogg')
        self.explosion_sounds.set_volume(0.3)
        self.hits = pygame.sprite.groupcollide(self.enemy_ships, self.laser_shots, True, True)
        for hit in self.hits:
            self.score += 50
            self.explosion_sounds.play()
            self.explosion_an = Explosion(hit.rect.center)
            self.all_sprites.add(self.explosion_an)

            self.enemy()

    def event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.game:
                    self.game = False
                self.running = False

    def enemy(self):
        """Spawn a new enemy"""
        self.enemies = EnemyShip()
        self.all_sprites.add(self.enemies)
        self.enemy_ships.add(self.enemies)

    def health_draw(self, screen, x, y, amount):
        """Drawing a helth bar"""
        self.amount = amount
        self.x = x
        self.y = y
        self.screen = screen
        if self.amount < 0:
            self.amount = 0

        self.percentage = (self.amount / 100) * HEALTH_BAR_LEN
        self.empty_rect = pygame.Rect(self.x, self.y, HEALTH_BAR_LEN, HEALTH_BAR_HEIGHT)
        self.percentage_rect = pygame.Rect(self.x, self.y, self.percentage, HEALTH_BAR_HEIGHT)
        pygame.draw.rect(self.screen, BLUE, self.percentage_rect)
        pygame.draw.rect(self.screen, WHITE, self.empty_rect, 2)

    def text_draw(self, surface, text, size, x, y):
        """Drawing score"""
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.surface = surface

        self.font_name = pygame.font.match_font('Purisa', True)
        self.font = pygame.font.Font(self.font_name, self.size)
        self.text_surface = self.font.render(self.text, True, WHITE)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.midtop = (self.x, self.y)
        self.surface.blit(self.text_surface, self.text_rect)

    def draw(self):
        """All draws"""
        self.screen.fill(BLACK)
        self.background.update()
        self.background.draw_background()
        self.all_sprites.draw(self.screen)
        self.text_draw(self.screen, str('Score: ' + str(self.score)), 18, 50, 0)
        self.health_draw(self.screen, 700, 25, self.ship.health)
        pygame.display.flip()

    def show_start_screen(self):
        """Show start screen"""
        self.screen.fill(BLACK)
        self.text_draw(self.screen, TITLE, 48, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.text_draw(self.screen, "Arrows to move, Space to Attack", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.text_draw(self.screen, "Press a key to play", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        """Show game over screen"""
        if not self.running:
            return
        self.screen.fill(BLACK)
        self.text_draw(self.screen, "SPACE BUSTARDS TAKE YOU!", 48, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4)
        self.text_draw(self.screen, "Score: " + str(self.score), 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
        self.text_draw(self.screen, "Press a key to play again", 22, SCREEN_WIDTH / 2, SCREEN_HEIGHT * 3 / 4)
        pygame.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.type == pygame.K_ESCAPE:
                        waiting = False
                        self.running = False

                if event.type == pygame.KEYDOWN:
                    waiting = False
                    self.running = True


g = MyGame()
g.show_start_screen()
while g.running:
    g.sprite()
    g.show_go_screen()

pygame.quit()
