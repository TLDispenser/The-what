import pygame
import random
import os
from player import Player
from camera import Camera

# Initialize pygame
pygame.init()

# Set window title
pygame.display.set_caption("My Game")

# Create the screen with proper dimensions
screen = pygame.display.set_mode((320, 240))


# Ensure display is properly set 
pygame.display.flip()


def main():
  # Clear the screen
  screen.fill((0, 0, 0))
  
  
  
  # Move and draw player
  player1.move_player()
  player1.draw_player(screen, camera.get_pos())
  
  camera.move(player1.position)

  # Update display
  pygame.display.update()


running = True

print("RUNNING!")

player1 = Player(10, 10)
camera = Camera(0, 0)

clock = pygame.time.Clock()

# Game loop
while running:
  # Handle events
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Run game logic and ensure screen updates are visible
  main()
  
  # Ensure display updates are processed
  pygame.display.flip()
  
  # Cap the frame rate
  clock.tick(60)

print("CLOSING!")

pygame.quit()
quit()
