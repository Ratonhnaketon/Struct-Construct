import pygame
from pyclass import *

Start = button(resources[1], font.render("Start", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 - 75), 4)
Settings = button(resources[1], font.render("Settings", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 2)
RESOLUTION = conf_button(resources[1], font.render(str(conf["size"]), True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 + 25), 100, resources[12])
SCREEN_MODE = button(resources[1], font.render(mode, True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 100)	
Exit = button(resources[1], font.render("Exit", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 75), 0)
Return = button(resources[1], font.render("Return", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 75), 1)
Settings_Layout = layout(Settings, (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2))
principal = Stage(resources[0], (0, 0), (Start, Settings, Exit), ())
configu = Stage(resources[0], (0, 0), (Return, SCREEN_MODE, RESOLUTION), (Settings_Layout,))
RESOLUTION = conf_button(resources[1], font.render(str(new_conf["size"]), True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 + 25), 100, resources[12])
SCREEN_MODE = button(resources[1], font.render(mode, True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 100)				
APPLY = button(resources[1], font.render("Apply", True,  (255, 255, 255)), \
		(screen.get_width()/2 + resources[1].get_width() , screen.get_height()/2 + 75), 2)
change_conf = Stage(resources[0], (0, 0), (Return, SCREEN_MODE, RESOLUTION, APPLY), (Settings_Layout,))
board = Stage(resources[0], (0, 0), (Settings, position1, position2, position3, \
	position4, position5, position6, position7, position8, position9), ())
#position1 = button(, , 1)
#position2 = button(, , 2)
#position3 = button(, , 3)
#position4 = button(, , 4)
#position5 = button(, , 5)
#position6 = button(, , 6)
#position7 = button(, , 7)
#position8 = button(, , 8)
#position9 = button(, , 9)