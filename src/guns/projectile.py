import math
import numpy as np
import pygame


class Projectile:
    def __init__(self, starting_x, starting_y, angle, gx, gy):
        self.gx = gx
        self.gy = gy
        self.x = starting_x
        self.y = starting_y
        self.velocity = 800
        self.img = pygame.image.load("images/bullet.png").convert_alpha()
        self.img = pygame.transform.smoothscale(
            self.img, (self.img.get_width() * 0.4, self.img.get_height() * 0.4)
        )
        self.angle = angle
        self.img = pygame.transform.rotozoom(self.img, -math.degrees(self.angle), 1)
        self.img.convert_alpha()
        self.tot_dis = 800
        self.dis_traveled = 0
        self.dead = False
        self.id = "proj"
        self.damage = 10

    def move_projectile(self, delta_time):
        if self.angle != None:
            self.x += math.cos(self.angle) * self.velocity * delta_time
            self.y += math.sin(self.angle) * self.velocity * delta_time
            self.dis_traveled += self.velocity * delta_time

    def draw(self, screen, delta_time):
        self.move_projectile(delta_time)
        screen.blit(
            self.img,
            (self.x - self.img.get_width() / 2, self.y - self.img.get_height() / 2),
        )

    def projectile_dead(self):
        if self.dis_traveled >= self.tot_dis or self.dead == True:
            return True
        return False

    def kill_projectile(self):
        self.dead = True

    def get_img(self):
        return (self.img)
    
    def get_pos(self):
        return (self.x, self.y)

    def get_info(self):
        return (self.x, self.y, self.id, self.angle)