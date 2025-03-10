import pygame
import random
import math
from meta.spritearray import make_sprite_array

class Fireable:
    def __init__(self, x, y, direction, source, speed):
        self.position = (x, y)
        self.direction = direction
        self.source = source
        self.init_speed = speed
        self.direction_matrix = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }
        self.velocity = (self.direction_matrix[self.direction][0] * self.init_speed, self.direction_matrix[self.direction][1] * self.init_speed)
    
    def move(self, do_drag=False):
        if do_drag:
            self.velocity = ((self.velocity[0] - self.velocity[0]/20) * self.direction_matrix[self.direction][0], (self.velocity[1] - self.velocity[1]/20) * self.direction_matrix[self.direction][1])
        else:
            self.velocity = (self.direction_matrix[self.direction][0] * self.init_speed, self.direction_matrix[self.direction][1] * self.init_speed)

        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])


class Bullet(Fireable):
    def __init__(self, x, y, direction, source):
        super().__init__(x, y, direction, source, 15)
        self.sprite = make_sprite_array('assets/fireables/lazer.png', 4, 16)
    
    def draw(self, screen, camera):
        direction_num = {
            'up': 3,
            'down': 1,
            'left': 2,
            'right': 0
        }
        screen.blit(self.sprite[direction_num[self.direction]+1], (self.position[0] - camera.get_pos()[0], self.position[1] - camera.get_pos()[1]))

