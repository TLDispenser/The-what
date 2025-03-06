import pygame
import random
from player import Player

pygame.init()

screen = pygame.display.set_mode((400, 300))


def main():
  player1.move_player()

  player1.draw_player(screen)

  pygame.display.update()


running = True

print("RUNNING!")

player1 = Player(10, 10)

while running:
  for event in pygame.event.get():
    if event == pygame.QUIT:
      running = False

  main()

print("CLOSING!")

pygame.quit()
quit()
