import pygame
import game

# Tela de fundo
class Stage(object):
	def __init__(self, image, position, active, buttons, layouts, size):
		self.image = image
		self.position = position
		#self.active = active
		self.buttons = buttons
		self.layouts = layouts
		self.size = size

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

class layout(object):
	def __init__(self, button, position):
		self.image = button.image
		self.text = button.text
		self.position = position

	def print_button(self, screen):
		screen.blit(self.image, (self.position[0] , self.position[1]))
		screen.blit(self.text, (self.position[0] + self.image.get_width()/2\
			- self.text.get_width()/2, self.position[1] + self.text.get_height()))

# Botões "clicáveis"
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

class conf_button(button):
	def __init__(self, image, text, position, func, arrow):
		button.__init__(self, image, text, position, func)
		self.arrowLeft = pygame.transform.scale(arrow, (int(self.image.get_width()*0.18), int(self.image.get_height()*0.18*3)))
		self.arrowRight = pygame.transform.rotate(self.arrowLeft, 180)
		self.positionLeft = self.position[0] - 1.5*self.arrowLeft.get_width(), self.position[1] + self.arrowLeft.get_height()/2
		self.positionRight =  self.position[0] + self.image.get_width() + self.arrowRight.get_width()/2, self.position[1] + \
		self.arrowRight.get_height()/2
		self.side = 0

	def check_possible_side(self, conf):
		check = 0
		if conf['size'][0] > 640 and conf['size'][1] > 480:
			check += 1
		if conf['size'][0] < 1920 and conf['size'][1] < 1080:
			check += 2
		return check

	def print_button(self, screen, conf):
		D = self.arrowLeft.get_width() - self.image.get_width(), self.arrowLeft.get_height() - self.image.get_height()
		screen.blit(self.image, (self.position[0] , self.position[1]))
		screen.blit(self.text, (self.position[0] + self.image.get_width()/2 - self.text.get_width()/2, self.position[1] + self.text.get_height()))
		check = self.check_possible_side(conf)
		if check == 1 or check == 3:
			screen.blit(self.arrowLeft, (self.positionLeft))
		if check >= 2:
			screen.blit(self.arrowRight, (self.positionRight))

	def set_button(self):
		cursor = pygame.mouse.get_pos()
		if cursor[0] > self.positionLeft[0] and cursor[0] < self.positionLeft[0] + self.arrowLeft.get_width() and \
		cursor[1] > self.positionLeft[1] and cursor[1] < self.positionLeft[1] + self.arrowLeft.get_height():
			self.active = 1
			self.side = 1
		elif cursor[0] > self.positionRight[0] and cursor[0] < self.positionRight[0] + self.arrowRight.get_width() and \
		cursor[1] > self.positionRight[1] and cursor[1] < self.positionRight[1] + self.arrowRight.get_height():
			self.active = 1
			self.side = 2
		else:
			self.active = 0
			self.side = 0

def bar_button(object):
	def __init__(self, bar, button, position, func, button_position):
		self.bar = bar
		self.button = button
		self.position = position
		self.func = func 
		self.button_position = button_position

	def printf_button(button, button_position):
		pass

	def move_button(button, button_position):
		pass

	def print_bar(bar, position):
		pass