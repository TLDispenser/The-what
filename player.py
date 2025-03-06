import pygame


class Player:

  def __init__(self, x, y):
    self.position = (x, y)
    self.velocity = (0, 0)
    self.direction = "none"

  def move_player(self):
    for event in pygame.event.get():
      if event == pygame.KEYDONW:
        if event == pygame.key.UP:
          print("IMPLIMENT UP YOU FU-")

  def draw_player(self, surface):
    pygame.draw.rect(surface, (255, 255, 255),
                     pygame.Rect(self.position, (30, 30)))
