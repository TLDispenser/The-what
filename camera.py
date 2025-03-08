import pygame

class Camera:
  def __init__(self, x, y):
    self.position = (x, y)
    self.velocity = (0, 0)
    self.tween = 0.15
  
  def move(self, target):
    target_x_dist = target[0] - self.position[0]
    target_y_dist = target[1] - self.position[1]
    
    if target_x_dist > 0.02 and target_y_dist:
      self.position = (
        self.position[0] + target_x_dist*self.tween,
        self.position[1] + target_y_dist*self.tween
        )
  
  def get_pos(self):
    return (self.position[0] + (pygame.get_window_width()/2)