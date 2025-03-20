from src.weapons import fireables
from src.core.lists import Lists

class Weapon:

	def __init__(self):
		self.max_ammo = 100
		self.ammo = 100
		self.damage = 10
		self.did_fire = False
		self.has_special_shoot = False  # Add has_special_shoot variable
		self.fireabletype = "bullet"
		self.lists = Lists()

	def shoot(self, x, y, direction, source):
		pass
	
	def reload(self):
		self.ammo += 1
		if self.ammo > self.max_ammo:
			self.ammo = self.max_ammo
	
	def get_ammo_stats(self):
		return self.max_ammo, self.ammo
	
class PewGun(Weapon):
	def __init__(self):
		super().__init__()
		self.has_special_shoot = False  # Initialize has_special_shoot
		self.fireabletype = "bullet"

	def shoot(self, x, y, direction, source):
		if not self.did_fire:
			if self.ammo > 0 and source == "Player":
				self.ammo -= 1
				self.lists.append_bullet(fireables.Bullet(x, y, direction, source))
				self.did_fire = True
		self.did_fire = True

class RocketLauncher(Weapon):
	def __init__(self):
		super().__init__()
		self.charge_time = 3
		self.max_ammo = 4
		self.ammo = 4
		self.has_special_shoot = False  # Initialize has_special_shoot
		self.fireabletype = "projectile"

	def shoot(self, x, y, direction, source):
		if not self.did_fire:
			if self.ammo > 0 and source == "Player":
				self.ammo -= 1
				self.lists.append_projectile(fireables.Rocket(x, y, direction, source))  # Placeholder for rocket
				self.did_fire = True
		self.did_fire = True

class RotaryGun(Weapon):
	def __init__(self):
		super().__init__()
		self.charge_time = 0.5
		self.charge_timer = 0
		self.max_ammo = 30
		self.ammo = 30
		self.refire_time = 3 / 40
		self.refire_timer = 0
		self.has_special_fire = True
		self.can_bg_charge = True
		self.has_special_shoot = True  # Initialize has_special_shoot

	def shoot(self, x, y, direction, source):
		self.did_fire = True

	def special_shoot(self, x, y, direction, source):
		if self.did_fire:
			if self.refire_timer > self.refire_time * 60:
				self.ammo -= 1
				self.lists.append_bullet(fireables.Bullet(x, y, direction, source))
				self.refire_timer = 0
			else:
				self.refire_timer += 1
		if self.ammo <= 0:
			self.did_fire = False

	def charge(self):
		if self.ammo < self.max_ammo:
			self.charge_timer += 1
			if self.charge_timer >= self.charge_time * 60:
				self.ammo += 1
				self.charge_timer = 0

class OverheatRotaryGun(Weapon):
	def __init__(self):
		super().__init__()
		self.charge_time = 0.5
		self.charge_timer = 0
		self.max_ammo = 32
		self.ammo = 1
		self.refire_time = 3 / 30
		self.refire_timer = 0
		self.has_special_fire = True
		self.can_bg_charge = True
		self.inverse_ammo = True
		self.has_special_shoot = True  # Initialize has_special_shoot

	def shoot(self, x, y, direction, source):
		self.did_fire = True

	def special_shoot(self, x, y, direction, source):
		if self.did_fire:
			if self.refire_timer > self.refire_time * 60:
				self.ammo += 1
				self.lists.append_bullet(fireables.Bullet(x, y, direction, source))
				self.refire_timer = 0
			else:
				self.refire_timer += 1
		if self.ammo >= self.max_ammo:
			# Add overheat logic here
			self.ammo = self.max_ammo

	def charge(self):
		if self.ammo > 1:
			self.charge_timer += 1
			if self.charge_timer >= self.charge_time * 60:
				self.ammo -= 1
				self.charge_timer = 0

class JaFLazerGun(Weapon):
	def __init__(self):
		super().__init__()
		self.charge_time = 8
		self.max_ammo = 256
		self.ammo = 256
		self.has_special_shoot = False  # Initialize has_special_shoot

	def shoot(self, x, y, direction, source):
		if self.ammo > 0:
			# Add laser shooting logic here
			self.ammo -= 1
			self.lists.append_bullet(fireables.Bullet(x, y, direction, source))

	def charge(self):
		if self.ammo < self.max_ammo:
			self.charge_timer += 1
			if self.charge_timer >= self.charge_time * 60:
				self.ammo += 1
				self.charge_timer = 0