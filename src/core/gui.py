import pygame
from src.meta.spritearray import make_sprite_array

def draw_hud(screen, stats):
	health, ammo, weapon, boost, position = stats
	# Draw health bar
	pygame.draw.rect(screen, (255, 0, 0), pygame.Rect(10, 10, (health/7)*100, 10))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 10, 100, 10), 2)
	
	# Draw ammo bar
	pygame.draw.rect(screen, (0, 0, 255), pygame.Rect(10, 30, ammo, 10))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 30, 100, 10), 2)
	
	# Draw boost bar
	pygame.draw.rect(screen, (0, 255, 0), pygame.Rect(10, 50, (boost/400)*100, 10))
	pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(10, 50, 100, 10), 2)
	
	# Draw weapon
	# screen.blit(weapon, (10, 70))
	
	# Draw position
	font = pygame.font.Font(None, 36)
	text = font.render(str(position), True, (255, 255, 255))
	screen.blit(text, (10, 90))
	
	pygame.display.flip()