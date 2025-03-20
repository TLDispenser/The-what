
class Lists:
	def __init__(self):
		self.bullets = []
		self.projectiles = []
		self.enemies = []

	def append_bullet(self, bullet):
		self.bullets.append(bullet)
		# print(self.bullets)

	def append_projectile(self, projectile):
		self.projectiles.append(projectile)
		# print(self.projectiles)

	def append_enemy(self, enemy):
		self.enemies.append(enemy)

	def get_bullets(self):
		return self.bullets

	def get_projectiles(self):
		return self.projectiles

	def get_enemies(self):
		return self.enemies
