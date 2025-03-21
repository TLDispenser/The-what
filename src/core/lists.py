class Lists:
	_instance = None

	def __new__(cls, *args, **kwargs):
		if not cls._instance:
			cls._instance = super(Lists, cls).__new__(cls, *args, **kwargs)
			cls._instance._initialized = False
		return cls._instance

	def __init__(self):
		if self._initialized:
			return
		self.bullets = []
		self.projectiles = []
		self.enemies = []
		self.players = [] # Why the FUCK am I adding this?
		self._initialized = True

	def append_bullet(self, bullet):
		self.bullets.append(bullet)

	def append_projectile(self, projectile):
		self.projectiles.append(projectile)

	def append_enemy(self, enemy):
		self.enemies.append(enemy)
	
	def append_player(self, player):
		self.players.append(player)

	def get_bullets(self):
		return self.bullets

	def get_projectiles(self):
		return self.projectiles

	def get_enemies(self):
		return self.enemies
	
	def get_players(self):
		return self.players
