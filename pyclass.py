class Board(object):
	def __init__(self, positions):
		self.positions = positions;

	def Choose_position(player):
		# Escolhe posição do tabuleiro e marca com simbolo de jogador
		pass

class Init(object):
	def __init__(self, gameInCourse, players):
		self.gameInCourse = gameInCourse
		self.players = players

	def Config(screen, stage, conf):
		new_conf = conf.copy()
		active_menu = stage.execute_menu(screen, conf)
		while True:
			new_conf  = load.change_conf(new_conf, active_menu)
			if new_conf['mode'] == [1]:
				mode = "Full Mode"
			else:
				mode = "Windowed"
			active_menu = change_conf.execute_menu(screen, new_conf)
			if active_menu == 2:
				pygame.quit()
				load.save_conf(new_conf)
				return new_conf
			if active_menu == 1:
				break
		return 1

	def Run(size, screen):
		self.gameInCourse = True
		if(gameInCourse == 1):
			self.End_game()
		self.Choose_player()
		active_menu = board.execute_menu(screen, conf)
		while True:
			if active_menu == 1:
				# Player make move
				pass
			if active_menu == 2: # Configurations
				active_menu = this.Config(screen, configu, conf)
			if active_menu == 3: #Back to principal
				return 1 

	def Choose_player():
		# Escolhe se é 'X' ou 'O'
		pass

	def End_game():
		if(gameInCourse == 0):
			return	

	def Winner():
		#Verifica se as condições de vitória foram satisfeitas
		pass

class Stage(object):
	def __init__(self, image, position, buttons, layouts):
		self.image = image
		self.position = position
		self.buttons = buttons
		self.layouts = layouts

	def print_stage(self, screen, conf):
		screen.blit(self.image, (self.position[0], self.position[1]))
		for button in self.buttons + self.layouts:
			try: 
				button.print_button(screen)
			except:
				button.print_button(screen, conf)

	def detect_button(self):
		for button in self.buttons:
			button.set_button()
			try:
				if button.active and button.side:
					return button.function() + button.side
			except:
				pass
			if button.active:
				return button.function()

	def execute_menu(self, screen, conf):	
		pygame.font.init()
		while True:
			screen.fill(0)		
			self.print_stage(screen, conf)
			command = self.detect_button()
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN and not command == None:
					return command
				if event.type == pygame.QUIT:
	        				game.ex(None)
			pygame.display.flip()

class button(object):
	def __init__(self, image, text, position, func):
		self.image = image
		self. text = text
		self.active = 0
		self.position = position
		self.func = func

	def print_button(self, screen):
		picture = pygame.transform.scale(self.image, (int(self.image.get_width()*1.09), int(self.image.get_height()*1.09)))
		D = picture.get_width() - self.image.get_width(), picture.get_height() - self.image.get_height()
		if not self.active:
			screen.blit(self.image, (self.position[0] , self.position[1]))
		else: 
			screen.blit(picture, (self.position[0] - D[0]/2, self.position[1] - D[1]/2))
		screen.blit(self.text, (self.position[0] + self.image.get_width()/2\
			- self.text.get_width()/2, self.position[1] + self.text.get_height()))

	def set_button(self):
		cursor = pygame.mouse.get_pos()
		if cursor[0] > self.position[0] and cursor[0] < self.position[0] + self.image.get_width() and \
		cursor[1] > self.position[1] and cursor[1] < self.position[1] + self.image.get_height():
			self.active = 1
		else:
			self.active = 0

	def function(self):
		if self.active:
			return self.func