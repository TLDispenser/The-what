import pygame
import random
import os
from src.core.player import Player
from src.core.camera import Camera
from src.core.background import Background
from src.core.gui import draw_hud
from src.core.lists import Lists

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

# Initialize big boy variables
lists = Lists()
lists.append_player(Player(0, 0))

camera = Camera(0, 0, screen)

# Initialize clock
clock = pygame.time.Clock()

def main():


	# Clear the screen
	screen.fill((0, 0, 0))



	# Do logic
	camera.move(lists.get_players()[0].position)
	lists.get_players()[0].move_player()
	background.update(camera.get_pos())

	# Then Draw
	background.draw()
	lists.get_players()[0].draw_player(screen, camera.get_pos())

	# This one's weird
	# ... REAL WEIRD

	# Debugging: Print the state of the lists object
	# print(f"Bullets in lists: {lists.bullets}")
	# print(f"Projectiles in lists: {lists.projectiles}")

	bullets = lists.bullets
	projectiles = lists.get_projectiles()

	for bullet in bullets:
		bullet.move()
		bullet.draw(screen, camera)
	
	for projectile in projectiles:
		projectile.move()
		projectile.draw(screen, camera)

	draw_hud(screen, lists.get_players()[0].get_stats())

	# Update display
	pygame.display.update()

running = True
paused = False

print("RUNNING!")

pressing_p = False

# Game loop
while running:

	lists = Lists()

	keys = pygame.key.get_pressed()
	
	if keys[pygame.K_p]:
		if not pressing_p:
			paused = not paused
			pressing_p = True
	else:
		pressing_p = False
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
	if not paused:
		main()
	else:
		# Display
		screen.fill((0, 0, 0))
		font = pygame.font.Font(None, 36)
		text = font.render("PAUSED", True, (255, 255, 255))
		screen.blit(text, (10, 10))
		pygame.display.update()
	

	# Ensure display updates are processed
	pygame.display.flip()
	
	# Cap the frame rate
	clock.tick(60)

print("CLOSING!")

pygame.quit()
quit()
