import pygame
import random
from math import *
from src.meta.spritearray import make_sprite_array
from src.core.lists import Lists

class Fireable:
	def __init__(self, x, y, direction, source, speed):
		self.lists = Lists()  # Use singleton instance
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
			self.velocity = (self.velocity[0] - (self.velocity[0]/20), self.velocity[1] - (self.velocity[1]/20))
			print(self.velocity)
		else:
			self.velocity = (self.direction_matrix[self.direction][0] * self.init_speed, self.direction_matrix[self.direction][1] * self.init_speed)

		self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

class Bullet(Fireable):
	def __init__(self, x, y, direction, source):
		super().__init__(x, y, direction, source, 15)
		self.sprite = make_sprite_array('assets/fireables/lazer.png', 4, 16)
		self.explosion_radius = 128
	
	def draw(self, screen, camera):
		direction_num = {
			'up': 3,
			'down': 1,
			'left': 2,
			'right': 0
		}
		screen.blit(self.sprite[direction_num[self.direction]+1], (self.position[0] - camera.get_pos()[0], self.position[1] - camera.get_pos()[1]))

class Rocket(Fireable):
	def __init__(self, x, y, direction, source):
		super().__init__(x, y, direction, source, 10)
		self.sprite = make_sprite_array('assets/fireables/rocket.png', 4, 16)
		self.explosion_radius = 128
		self.exploding = False
	
	def knockback(self, obj):
		distance = sqrt((obj.position[0] - self.position[0])**2 + (obj.position[1] - self.position[1])**2)
		if distance < self.explosion_radius:
			force = (self.explosion_radius - distance) / self.explosion_radius * 15
			angle = atan2(obj.position[1] - self.position[1], obj.position[0] - self.position[0])
			
			dirX = cos(angle)
			dirY = sin(angle)
			
			obj.velocity = (obj.velocity[0] + dirX * force, obj.velocity[1] + dirY * force)
	
	def do_damage(self, object):
		damage = 0
		distance = sqrt((object.position[0] - self.position[0])**2 + (object.position[1] - self.position[1])**2)
		if distance < self.explosion_radius:
			damage = (self.explosion_radius - distance) / self.explosion_radius*3
		
		return damage
	
	def explode(self):
		self.exploding = True
		for enemy in self.lists.get_enemies():
			enemy.health -= self.do_damage(enemy)
			self.knockback(enemy)
		
		for player in self.lists.get_players():
			player.health -= self.do_damage(player)
			self.knockback(player)

		for projectile in self.lists.get_projectiles():
			if projectile != self and not projectile.exploding:
				projectile.explode()     

		self.lists.get_projectiles().remove(self)
	
	def move(self, do_drag=True):
		super().move(do_drag)
		if abs(self.velocity[0]) < 0.1 and abs(self.velocity[1]) < 0.1:
			self.explode()
	
	def draw(self, screen, camera):
		direction_num = {
			'up': 3,
			'down': 1,
			'left': 2,
			'right': 0
		}
		screen.blit(self.sprite[direction_num[self.direction]+1], (self.position[0] - camera.get_pos()[0], self.position[1] - camera.get_pos()[1]))