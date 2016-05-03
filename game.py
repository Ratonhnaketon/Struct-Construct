import pygame, load, math
from gameclass import *

# Start Game

def run(conf, resources):
	pygame.init()
	pygame.display.set_icon(resources[17])
	pygame.display.set_caption('Struct Construct')
	screen = pygame.display.set_mode((conf["size"][0], conf["size"][1]))
	resources[0] = pygame.transform.smoothscale(resources[0], conf["size"])
	if conf["mode"] == [1]:
		pygame.display.toggle_fullscreen()
		mode = "Full Mode"
	else:
		mode = "Windowed"
	font = pygame.font.Font(None, 24)
	Start = button(resources[1], font.render("Start", True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 - 75), 4)
	Settings = button(resources[1], font.render("Settings", True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 2)
	RESOLUTION = conf_button(resources[1], font.render(str(conf["size"]), True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 + 25), 100, resources[12])
	SCREEN_MODE = button(resources[1], font.render(mode, True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 100)	
	Credits = button(resources[1], font.render("Credits", True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 25), 3)
	Exit = button(resources[1], font.render("Exit", True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 75), 0)
	Return = button(resources[1], font.render("Return", True,  (255, 255, 255)), \
		(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 75), 1)
	Settings_Layout = layout(Settings, (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2))
	Credits_Layout = layout(Credits, (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2))
	first_menu = Stage(resources[0], (0, 0), 1, (Start, Settings, Credits, Exit), (), conf["size"])
	second_menu = Stage(resources[0], (0, 0), 2, (Return, SCREEN_MODE, RESOLUTION), (Settings_Layout,), conf["size"])
	third_menu = Stage(resources[0], (0, 0), 3, (Return,), (Credits_Layout,), conf["size"])
	active_menu = 1
	while True:
		if active_menu == 1:
			active_menu = first_menu.execute_menu(screen, conf)
		elif active_menu == 2:
			active_menu = second_menu.execute_menu(screen, conf)
			new_conf = conf.copy()
			while active_menu > 99:
				new_conf  = load.change_conf(new_conf, active_menu)
				if new_conf['mode'] == [1]:
					mode = "Full Mode"
				else:
					mode = "Windowed"
				RESOLUTION = conf_button(resources[1], font.render(str(new_conf["size"]), True,  (255, 255, 255)), \
				(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 + 25), 100, resources[12])
				SCREEN_MODE = button(resources[1], font.render(mode, True,  (255, 255, 255)), \
				(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 100)				
				APPLY = button(resources[1], font.render("Apply", True,  (255, 255, 255)), \
				(screen.get_width()/2 + resources[1].get_width() , screen.get_height()/2 + 75), 2)
				change_second_menu = Stage(resources[0], (0, 0), 2, (Return, SCREEN_MODE, \
				RESOLUTION, APPLY), (Settings_Layout,), new_conf["size"])
				active_menu = change_second_menu.execute_menu(screen, new_conf)
				if active_menu == 2:
					pygame.quit()
					load.save_conf(new_conf)
					return new_conf
				if active_menu == 1:
					break
			active_menu = 1
		elif active_menu == 3:
			active_menu = third_menu.execute_menu(screen, conf)
		elif active_menu == 4:
			star(conf["size"], screen, resources)
		if active_menu == 0:
			ex(None)

# Start new history

def star(size, screen, resources):
	ex(size)

# Exit Game
# Any variable ex recieves will serve for nothing

def ex(trash):
	pygame.quit()
	exit(0)
