import pygame
from pyclass import *
# from definitions import *

pygame.init()
font = pygame.font.Font(None, 24)
# pygame.display.set_icon(Colocar Imagem)
pygame.display.set_caption('Struct Construct')
screen = pygame.display.set_mode([800, 600])
if conf["mode"] == [1]:
	pygame.display.toggle_fullscreen()
	mode = "Full Mode"
else:
	mode = "Windowed"
while True:
	if active_menu == 1: # Menu principal
		active_menu = principal.execute_menu(screen, conf)
	elif active_menu == 2: # Créditos
		pass
	elif active_menu == 3: # Configurações 
		active_menu = Config(screen, configu, conf)
	elif active_menu == 4: # Iniciar nova partid
		active_menu = Run(screen, board, conf)
	else:
		exit(0)

