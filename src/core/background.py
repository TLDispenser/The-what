import pygame

class Background:
	def __init__(self, image_file, screen):
		self.image = pygame.image.load(image_file).convert()
		self.rect = self.image.get_rect()
		self.screen = screen
		self.y = 0

	def update(self, camera_pos):
		self.x = -camera_pos[0] % self.rect.width
		self.y = -camera_pos[1] % self.rect.height

	def draw(self):
		self.screen.blit(self.image, (self.x, self.y))
		self.screen.blit(self.image, (self.x - self.rect.width, self.y))
		self.screen.blit(self.image, (self.x, self.y - self.rect.height))
		self.screen.blit(self.image, (self.x - self.rect.width, self.y - self.rect.height))
