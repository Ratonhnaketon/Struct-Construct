import pygame, load, math, random
from gameclass import *

# Start Game

def run(conf, resources):
	pygame.init()
	# pygame.display.set_icon(resources[17])
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
	ModeOne = button(resources[1], font.render("Challenge", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 - 25), 2)
	ModeTwo = button(resources[1], font.render("Free", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 25), 3)
	Settings = button(resources[1], font.render("Settings", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 2)
	RESOLUTION = conf_button(resources[1], font.render(str(conf["size"]), True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 + 25), 100, resources[2])
	SCREEN_MODE = button(resources[1], font.render(mode, True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 100)	
	Credits = button(resources[1], font.render("Credits", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 25), 3)
	Exit = button(resources[1], font.render("Exit", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 75), 0)
	Return = button(resources[1], font.render("Return", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 + 75), 1)
	one = button(resources[1], font.render("1", True,  (255, 255, 255)), \
	(screen.get_width()/2 - 170, screen.get_height()/2 - 125), 2)
	two = button(resources[1], font.render("2", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 - 125), 3)
	three = button(resources[1], font.render("3", True,  (255, 255, 255)), \
	(screen.get_width()/2 + 60, screen.get_height()/2 - 125), 4)
	four = button(resources[1], font.render("4", True,  (255, 255, 255)), \
	(screen.get_width()/2 - 170, screen.get_height()/2 - 75), 5)
	five = button(resources[1], font.render("5", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 - 75), 6)
	six = button(resources[1], font.render("6", True,  (255, 255, 255)), \
	(screen.get_width()/2 + 60 , screen.get_height()/2 - 75), 7)
	seven = button(resources[1], font.render("7", True,  (255, 255, 255)), \
	(screen.get_width()/2 - 170, screen.get_height()/2 - 25), 8)
	eight = button(resources[1], font.render("8", True,  (255, 255, 255)), \
	(screen.get_width()/2 - resources[1].get_width()/2 , screen.get_height()/2 - 25), 9)
	nine = button(resources[1], font.render("9", True,  (255, 255, 255)), \
	(screen.get_width()/2 + 60, screen.get_height()/2 - 25), 10)
	thanksTo = layout(resources[8], font.render("",\
	True,  (0, 0, 0)), (screen.get_width()/2 - resources[8].get_width()/2, resources[1].get_height()/2 + 100))
	
	GameModes = layout(resources[1], font.render("Game Modes", True,  (255, 255, 255)), (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2 + 100))
	Settings_Layout = layout(resources[1], font.render("Settings", True,  (255, 255, 255)), (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2))
	Challenges = layout(resources[1], font.render("Challenges", True,  (255, 255, 255)), (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2 + 100))
	Credits_Layout = layout(resources[1], font.render("Credits", True,  (255, 255, 255)), (screen.get_width()/2 - resources[1].get_width()/2, resources[1].get_height()/2))	
	first_menu = Stage(resources[0], (Start, Settings, Credits, Exit), (), conf["size"])
	second_menu = Stage(resources[0], (Return, SCREEN_MODE, RESOLUTION), (Settings_Layout,), conf["size"])
	third_menu = Stage(resources[0], (Return,), (Credits_Layout, thanksTo), conf["size"])
	mode_game = Stage(resources[0], (Return, ModeOne, ModeTwo), (GameModes,), conf["size"])
	select_challenge = Stage(resources[0], (Return, one, two, three, four, five, six, seven, \
	eight, nine), (Challenges,), conf["size"])
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
				(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 + 25), 100, resources[2])
				SCREEN_MODE = button(resources[1], font.render(mode, True,  (255, 255, 255)), \
				(screen.get_width()/2 - resources[1].get_width()/2, screen.get_height()/2 - 25), 100)				
				APPLY = button(resources[1], font.render("Apply", True,  (255, 255, 255)), \
				(screen.get_width()/2 + resources[1].get_width() , screen.get_height()/2 + 75), 2)
				change_second_menu = Stage(resources[0], (Return, SCREEN_MODE, \
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
			#Modos de jogo						
			active_menu = mode_game.execute_menu(screen, conf)
			if active_menu == 2:
				active_menu = select_challenge.execute_menu(screen, conf)
				if active_menu == 2:
					star(screen, resources, 1, conf)
				if active_menu == 3:
					star(screen, resources, 2, conf)
				if active_menu == 4:
					star(screen, resources, 3, conf)
				if active_menu == 5:
					star(screen, resources, 4, conf)
				if active_menu == 6:
					star(screen, resources, 5, conf)
				if active_menu == 7:
					star(screen, resources, 6, conf)
				if active_menu == 8:
					star(screen, resources, 7, conf)
				if active_menu == 9:
					star(screen, resources, 8, conf)
				if active_menu == 10:
					star(screen, resources, 9, conf)

			elif active_menu == 3:
				star(screen, resources, 0, conf)

			active_menu = 1
		if active_menu == 0:
			ex()

# Start game

def star(screen, resources, gameMode, conf):
	font = pygame.font.Font(None, 24)
	Return = button(resources[1], font.render("Return", True,  (255, 255, 255)), \
	(0, 0), 1)
	Restart = button(resources[1], font.render("Restart", True,  (255, 255, 255)), \
	(110, 0), 2)
	Exit = button(resources[1], font.render("Exit", True,  (255, 255, 255)), \
	(220 , 0), 0)
	Finish = button(resources[1], font.render("Finish", True,  (255, 255, 255)), \
	(screen.get_width() - resources[1].get_width() , 0), 5)
	mode_game = gameStage(resources[3], (Return, Restart, Exit, Finish), (), conf["size"], gameMode)
	active_menu = mode_game.execute_menu(screen, conf)
	while True:
		if active_menu == 0:
			ex()
		elif active_menu == 1:
			return
		elif active_menu == 2:
			return star(screen, resources, gameMode, conf)

def ex():
	pygame.quit()
	exit(0)

