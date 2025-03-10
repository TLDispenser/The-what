import pygame
import random
import os
from src.core.player import Player
from src.core.camera import Camera
from src.core.background import Background
from src.core.gui import draw_hud

# Initialize pygame
pygame.init()

# Set window title
pygame.display.set_caption("Gargatron")

# Create the screen with proper dimensions
original_width, original_height = 320, 240
screen = pygame.display.set_mode((original_width, original_height), pygame.SCALED)
background = Background('assets/background.png', screen)

# Ensure display is properly set 
pygame.display.flip()


bullets = []
projectiles = []
enemies = []

def main():
  # Clear the screen
  screen.fill((0, 0, 0))

  # Do logic

  camera.move(player1.position)
  player1.move_player()
  background.update(camera.get_pos())

  # Then Draw

  background.draw()
  player1.draw_player(screen, camera.get_pos())

  # This one's weird

  for bullet in bullets:
    bullet.move()
    bullet.draw(screen, camera)

  draw_hud(screen, player1.get_stats())

  # Update display
  pygame.display.update()


running = True

print("RUNNING!")

player1 = Player(10, 10, bullets, projectiles)
camera = Camera(0, 0, screen)

clock = pygame.time.Clock()

# Game loop
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    elif event.type == pygame.VIDEORESIZE:
      new_width = event.w
      new_height = int(new_width * 3 / 4)
      screen = pygame.display.set_mode((new_width, new_height), pygame.SCALED)
      background = Background('assets/background.png', screen)

  # Run game logic and ensure screen updates are visible
  main()
  

  
  # Ensure display updates are processed
  pygame.display.flip()
  
  # Cap the frame rate
  clock.tick(60)

print("CLOSING!")

pygame.quit()
quit()
