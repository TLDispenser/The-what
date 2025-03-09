import pygame
from meta.spritesheet import SpriteSheet

def make_sprite_array(sprite: str, sprite_num: int, size: int, double: float=True):
  sprite = SpriteSheet(sprite)
  img = None
  temp_sheet = [double]
  toil_and_trouble = int(double)*sprite_num
  
  for i in range(0, sprite_num+toil_and_trouble):
    img = sprite.get_image(0, size*i, size, size)
    temp_sheet.append(img)
  
  return temp_sheet