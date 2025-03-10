import pygame
from src.weapons.weapons import PewGun, RocketLauncher, RotaryGun, OverheatRotaryGun, JaFLazerGun
from src.meta.spritearray import make_sprite_array

class Player:

  def __init__(self, x, y, bullets, projectiles):
    self.position = (x, y)
    self.velocity = (0, 0)
    self.direction = "right"
    self.drag = 20
    self.boost_bar = 400
    self.current_boostmul = 0
    self.boostmul = 2
    self.boosting = False
    self.boost_lock = False
    self.health = 7
    self.ammo = 100
    self.weapons = [
      "pewgun",
      "rocketlauncher",
      "rotarygun",
      "overheatgun",
      "jaflazergun",
      PewGun(),
      RocketLauncher(),
      RotaryGun(),
      OverheatRotaryGun(),
      JaFLazerGun()
    ]
    self.selected_weapon = 0
    self.sprite_dir = "assets/sprites/player/ship/"
    self.flames_dir = "assets/sprites/player/flames/"
    self.sprites = {
      "pewgun": make_sprite_array(self.sprite_dir+'base.png', 4, 16, False),
      "rocketlauncher": make_sprite_array(self.sprite_dir+'missile.png', 4, 16, False),
      "rotarygun": make_sprite_array(self.sprite_dir+'rotary.png', 8, 16, True),
      "overheatgun": make_sprite_array(self.sprite_dir+'overheat.png', 8, 16, True),
      "jaflazergun": make_sprite_array(self.sprite_dir+'lazer.png', 8, 16, True)
    }
    self.flames = {
      "up": make_sprite_array(self.flames_dir+'up.png', 8, 16, True),
      "down": make_sprite_array(self.flames_dir+'down.png', 8, 16, True),
      "left": make_sprite_array(self.flames_dir+'left.png', 8, 16, True),
      "right": make_sprite_array(self.flames_dir+'right.png', 8, 16, True)
    }
    
    self.did_press_v = False
    
    self.flame_animtimer = 0

    self.bullets = bullets
    self.projectiles = projectiles

    self.hitbox = pygame.Rect(self.position[0], self.position[1], 16, 16)

  def move_player(self):
    keys = pygame.key.get_pressed()
    pressing_direction = keys[pygame.K_LEFT] or keys[pygame.K_RIGHT] or keys[pygame.K_UP] or keys[pygame.K_DOWN]
    if keys[pygame.K_LEFT]:
      self.direction = "left"
    elif keys[pygame.K_RIGHT]:
      self.direction = "right"

    if keys[pygame.K_UP]:
      self.direction = "up"
    elif keys[pygame.K_DOWN]:
      self.direction = "down"
      
    if self.direction == "left" and keys[pygame.K_LEFT]:
      self.velocity = (self.velocity[0] - (0.33 * self.current_boostmul), self.velocity[1])
    elif self.direction == "right" and keys[pygame.K_RIGHT]:
      self.velocity = (self.velocity[0] + (0.33 * self.current_boostmul), self.velocity[1])
    elif self.direction == "up" and keys[pygame.K_UP]:
      self.velocity = (self.velocity[0], self.velocity[1] - (0.33 * self.current_boostmul))
    elif self.direction == "down" and keys[pygame.K_DOWN]:
      self.velocity = (self.velocity[0], self.velocity[1] + (0.33 * self.current_boostmul))

      
    # Update position based on velocity
    self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])

    self.velocity = (self.velocity[0] - (self.velocity[0]/self.drag),
                     self.velocity[1] - (self.velocity[1]/self.drag),)
    
    if keys[pygame.K_LSHIFT] and self.boost_bar > 0 and not self.boost_lock and pressing_direction:
      self.boosting = True
    else:
      self.boosting = False

    if self.boosting:
      self.boost_bar -= 1
      if self.boost_bar <= 0:
        self.boosting = False
        self.boost_lock = True
        self.boost_bar = 0
      self.current_boostmul = self.boostmul
    else:
      self.current_boostmul = 1
      if self.boost_bar < 400:
        self.boost_bar += 1
      if self.boost_bar >= 400:
        self.boost_lock = False

    if keys[pygame.K_v]:
        if not self.did_press_v:
            self.selected_weapon += 1
            self.selected_weapon %= len(self.weapons)//2
            print(self.weapons[self.selected_weapon])
            self.did_press_v = True
    else:
        self.did_press_v = False
    
    self.max_ammo, self.ammo = self.weapons[self.selected_weapon+(len(self.weapons)//2)].get_ammo_stats()
    if keys[pygame.K_c]:
      self.weapons[self.selected_weapon+(len(self.weapons)//2)].shoot(self.position[0], self.position[1], self.direction, "Player", self.bullets)
    else:
      self.weapons[self.selected_weapon+(len(self.weapons)//2)].did_fire = False



  def draw_player(self, surface, offset):
    the_thing = int(self.sprites[self.weapons[self.selected_weapon]][0])+1
    direction_num = {
      "left": 3*the_thing,
      "right": 1*the_thing,
      "up": 4*the_thing,
      "down": 2*the_thing
    }
    self.flame_offset = (0, 0)
    if self.direction == "left":
      self.flame_offset = (14, 0)
    elif self.direction == "right":
      self.flame_offset = (-14, 0)
    elif self.direction == "up":
      self.flame_offset = (0, 14)
    elif self.direction == "down":
      self.flame_offset = (0, -14)
    
    self.flame_animtimer += 1
    self.flame_animtimer %= len(self.flames[self.direction])-1
    
    # Draw the sprite onto the surface at the player's position
    surface.blit(self.flames[self.direction][self.flame_animtimer+1], (self.position[0] - offset[0] + self.flame_offset[0], self.position[1] - offset[1] + self.flame_offset[1]))
    surface.blit(self.sprites[self.weapons[self.selected_weapon]][direction_num[self.direction]], (self.position[0] - offset[0], self.position[1] - offset[1]))

  def get_stats(self):
    round_pos = (round(self.position[0]), round(self.position[1]))
    return (self.health, self.ammo, self.weapons[self.selected_weapon], self.boost_bar, round_pos)
