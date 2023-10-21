import pygame
import time
from guns.pistol import Pistol
from guns.projectile import Projectile
from resources.player import Player
from resources.ammo import Ammo
from resources.rock import Rock
from resources.tree import Tree
from resources.shield import Shield
from GameState import GameState

pygame.init()
WORLD_WIDTH, WORLD_HEIGHT = (10000, 10000)

WIDTH = 1200
HEIGHT = 800
class Run:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("EduShoot")
        self.clock = pygame.time.Clock()
        self.player = Player(2000, 2000, 50, 50)
        self.bg = pygame.image.load("images/green_background.png").convert()
        self.bg = pygame.transform.smoothscale(self.bg, (WIDTH, HEIGHT))
        self.screen.blit(self.bg, (0, 0))
        self.localx = 0
        self.localy = 0
        self.game_state = GameState()
        self.game_state.initialize_random(100)
        #self.bg = self.background


        self.projectiles = []

    def shoot_bullets(self):
        self.player.weapon.set_angle()
        self.player.set_angle()

        if (pygame.mouse.get_pressed()[0]):
            player_x, player_y = self.player.weapon.get_pos()
            if(self.player.weapon.can_shoot()):
                temp_proj = Projectile(player_x, player_y, self.player.weapon.get_angle())
                self.projectiles.append(temp_proj)

    def render_projectiles(self, delta_time):
        for proj in self.projectiles:
            proj.draw(self.screen, delta_time)

    # inspired by Steve Paget pygame functions
    def render_background(self):
        self.localx += self.player.dir_x
        self.localy += self.player.dir_y
        xOff = (0 - self.localx % WIDTH)
        yOff = (0 - self.localy % HEIGHT)

        self.screen.blit(self.bg, (xOff, yOff))
        self.screen.blit(self.bg, (xOff + WIDTH, yOff))
        self.screen.blit(self.bg, (xOff, yOff + HEIGHT))
        self.screen.blit(self.bg, (xOff + WIDTH, yOff + HEIGHT))

    def render_game_state(self):
        for ammo in self.game_state.ammo:
            self.screen.blit(ammo.img, (ammo.x - self.player.x + WIDTH / 2 - ammo.w / 2, ammo.y - self.player.y + HEIGHT / 2 - ammo.h / 2))
        for rock in self.game_state.rocks:
            self.screen.blit(rock.img, (rock.x - self.player.x + WIDTH / 2 - rock.w / 2, rock.y - self.player.y + HEIGHT / 2 - rock.h / 2))
        for shield in self.game_state.rocks:
            self.screen.blit(shield.img, (shield.x - self.player.x + WIDTH / 2 - shield.w / 2, shield.y - self.player.y + HEIGHT / 2 - shield.h / 2))
        for tree in self.game_state.rocks:
            self.screen.blit(tree.img, (tree.x - self.player.x + WIDTH / 2 - tree.w / 2, tree.y - self.player.y + HEIGHT / 2 - tree.h / 2))
          
    def run(self):
        previous_time = time.perf_counter()
        running = True
        while running:
            delta_time = time.perf_counter() - previous_time
            previous_time = time.perf_counter()
            self.player.weapon.increase_time(delta_time)

            self.render_background()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


            self.shoot_bullets()
            self.render_projectiles(delta_time)
            self.player.update(delta_time)

            self.player.draw(self.screen)
            self.player.weapon.draw(self.screen)
            self.render_game_state()
            pygame.display.flip()

            self.clock.tick(60)

        pygame.quit()

game = Run()
game.run()
