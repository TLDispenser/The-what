import pygame

class Camera:
  def __init__(self, x, y, screen):
    self.position = (x, y)
    self.velocity = (0, 0)
    self.tween = 0.15
    self.screen = screen
  
  def move(self, target):
    target_x_dist = target[0] - self.position[0]
    target_y_dist = target[1] - self.position[1]
    
    if abs(target_x_dist) > 0.02 or abs(target_y_dist) > 0.02:
      self.position = (
        self.position[0] + target_x_dist * self.tween,
        self.position[1] + target_y_dist * self.tween
      )
  
  def get_pos(self):
    screen_width = self.screen.get_width()
    screen_height = self.screen.get_height()
    return (self.position[0] - screen_width / 2, self.position[1] - screen_height / 2)