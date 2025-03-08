import pygame
from spritearray import make_sprite_array

class Player:

  def __init__(self, x, y):
    self.position = (x, y)
    self.velocity = (0, 0)
    self.direction = "right"
    self.drag = 20
    self.boost_bar = 400
    self.current_boostmul = 0
    self.boostmul = 2
    self.boosting = False
    self.boost_lock = False
    self.weapons = [
      # PewGun,
      "pewgun",
      # RocketLauncher,
      "rocketlauncher",
      # RotaryGun,
      "rotarygun",
      # OverheatRotaryGun,
      "overheatgun",
      # JaFLazerGun,
      "jaflazergun"
    ]
    self.selected_weapon = 0
    
    
    self.sprites = {
      "pewgun": make_sprite_array('assets/sprites/base.png', 4, 16, False),
      "rocketlauncher": make_sprite_array('assets/sprites/missile.png', 4, 16, False),
      "rotarygun": make_sprite_array('assets/sprites/rotary.png', 8, 16, True),
      "overheatgun": make_sprite_array('assets/sprites/overheat.png', 8, 16, True),
      "jaflazergun": make_sprite_array('assets/sprites/lazer.png', 8, 16, True)
    }
    
    
    self.did_press_v = False

  def move_player(self):
    keys = pygame.key.get_pressed()
    pressing_direction = keys[pygame.K_LEFT] and keys[pygame.K_RIGHT] and keys[pygame.K_UP] and keys[pygame.K_DOWN]
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
    
    if keys[pygame.K_LSHIFT]:
      self.current_boostmul = self.boostmul
    else:
      self.current_boostmul = 1
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_v]:
        if not self.did_press_v:
            self.selected_weapon += 1
            self.selected_weapon %= len(self.weapons)
            print(self.weapons[self.selected_weapon])
            self.did_press_v = True
    else:
        self.did_press_v = False



  def draw_player(self, surface, offset):
    the_thing = int(self.sprites[self.weapons[self.selected_weapon]][0])+1
    direction_num = {
      "left": 3*the_thing,
      "right": 1*the_thing,
      "up": 4*the_thing,
      "down": 2*the_thing
    }
    
    # Draw the sprite onto the surface at the player's position
    surface.blit(self.sprites[self.weapons[self.selected_weapon]][direction_num[self.direction]], (self.position[0] - offset[0], self.position[1] - offset[1]))
    
    
    
    
    
    
    
    
    