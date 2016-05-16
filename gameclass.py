import pygame, game, load, math, random

resources = load.load_everthing()

# Tela de fundo
class Stage(object):
	def __init__(self, image, buttons, layouts, size):
		self.image = image
		self.buttons = buttons
		self.layouts = layouts
		self.size = size

	def print_stage(self, screen, conf):
		screen.blit(self.image, (0, 0))
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
					game.ex()

			pygame.display.flip()

class gameStage(Stage):
	
	controlID = 0

	def __init__(self, image, buttons, layouts, size, gameMode):
		Stage.__init__(self, image, buttons, layouts, size)
		self.gameMode = gameMode
		self.bars = []
		self.grounds = []

	def createBar(self, number):
		for i in range(number):
			self.bars.append(barObject(gameStage.controlID))
			gameStage.controlID += 1

	def createGround(self, positions):
		for i in range(len(positions)):
			self.grounds.append(groundObject(positions[i], 0, i))

	def removeBars(self):
		self.bars = []
		controlID = 0

	def detectBar(self):
		for bar in self.bars:
			bar.detect()
			if bar.active:
				return bar

		return None					

	def print_bars(self, screen):
		for bar in self.bars:
			bar.print_bar(screen)
			for bond in bar.bond:
				bond.print_bond(screen)

	def print_ground(self, screen):
		for ground in self.grounds:
			ground.print_ground(screen)

	def execute_menu(self, screen, conf):
		pygame.font.init()
		# Não esquecer do gameMode
		self.createBar(5)
		self.createGround([[0, 2*screen.get_height()/3], \
		[2*screen.get_width()/3, 2*screen.get_height()/3]])
		keys = [False, False]
		while True:
			screen.fill(0)		
			self.print_stage(screen, conf)
			self.print_ground(screen)
			self.print_bars(screen)
			command = self.detect_button()
			bar = self.detectBar()
			for event in pygame.event.get():
				if event.type == pygame.MOUSEBUTTONDOWN:
					if not command == None:
						return command

					if event.button == 1:
						keys[0] = True

					if event.button == 3:
						keys[1] = True

				if event.type == pygame.QUIT:
					game.ex()

				if event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						keys[0] = False
					if event.button == 3:
						keys[1] = False

			cursor = pygame.mouse.get_pos()
			if not bar == None:
				if keys[0]:
					bar.move(cursor)
				if keys[1]:
					bar.rotate(cursor)

			pygame.display.flip()

class layout(object):
	def __init__(self, image, text, position):
		self.image = image
		self.text = text
		self.position = position

	def print_button(self, screen):
		screen.blit(self.image, self.position)
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
			screen.blit(self.image, self.position)
		else: 
			screen.blit(picture, (self.position[0] - D[0]/2, self.position[1] - D[1]/2))
		screen.blit(self.text, (self.position[0] + self.image.get_width()/2 \
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
		screen.blit(self.image, self.position)
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

class barObject(object):

	controlID = 0

	def __init__(self, identification):
		picture = resources[5]
		resize = 0.14
		self.angle = 0
		self.original = pygame.transform.scale(picture, \
		(int(picture.get_width()*resize), int(picture.get_height()*resize)))
		self.image = self.original
		self.mask = pygame.mask.from_surface(self.image)
		self.size = self.mask.get_size()
		self.sizeBase = self.original.get_size()
		info = load.conf()
		self.position = [random.randint(int(info['size'][0]/14), int(4*info['size'][0]/5)), \
		random.randint(int(info['size'][1]/6), int(info['size'][1]/5))]
		self.bond = []
		self.create_bond(2)
		barObject.controlID += 2
		self.id = identification
		self.active = 0
		cursor = (random.randint(-1000, 1000)), (random.randint(-1000, 1000))
		self.rotate(cursor)
		self.update_bond_position()

	def update_bond_position(self):
		center = (self.size[0]/2, self.size[1]/2)
		self.bond[0].position = (self.position[0] + center[0] - \
		math.cos(self.angle) * (self.sizeBase[0]/2), \
		self.position[1] + center[1] - math.sin(self.angle) * (self.sizeBase[0])/2)
		self.bond[1].position = (self.position[0] + center[0] + \
		math.cos(self.angle) * (self.sizeBase[0]/2), \
		self.position[1] + center[1] + math.sin(self.angle) * (self.sizeBase[0])/2)
		# Atualização da posição em relação a treliça

	def detect(self):
		cursor = pygame.mouse.get_pos()
		position = (int(cursor[0] - self.position[0]), int(cursor[1] - self.position[1]))
		if cursor[0] > self.position[0] and cursor[0] < self.position[0] + self.size[0] and \
		cursor[1] > self.position[1] and cursor[1] < self.position[1] + self.size[1]:
			if self.mask.get_at(position):
				self.active = 1

			else:
				self.active = 0
			# Detectar também se há contato entre bonds


	def print_bar(self, screen):
		screen.blit(self.image, self.position)

	def move(self, cursor):
		size = self.mask.get_size()
		self.position[0] = cursor[0] - size[0]/2
		self.position[1] = cursor[1] - size[1]/2
		self.update_bond_position()

	def rotate(self, cursor):
		self.angle = math.atan2(cursor[1] - self.position[1] - \
		self.size[1]/2, cursor[0] - self.position[0] - self.size[0]/2)
		center = (self.size[0]/2, self.size[1]/2)
		self.image = pygame.transform.rotate(self.original, 180 - self.angle * 57.29)
		self.mask = pygame.mask.from_surface(self.image)
		self.size = self.mask.get_size()
		self.position[0] += center[0] - self.size[0]/2		
		self.position[1] += center[1] - self.size[1]/2
		self.update_bond_position()

	def create_bond(self, number):
		for i in range(number):
			self.bond.append(bond(i))

class groundObject(object):
	def __init__(self, position, friction, identification):
		picture = resources[4]
		resize = 1
		self.image = pygame.transform.scale(picture, (int(picture.get_width()*resize), int(picture.get_height()*resize)))
		self.size = (self.image.get_width(), self.image.get_height())
		self.position = position
		self.friction = friction
		self.id = identification
		# Precisa de bond também

	def print_ground(self, screen):
		screen.blit(self.image, self.position)

	# função para atrito

class bond(object):
	def __init__(self, identification):
		self.position = (0, 0)
		self.active = 0
		self.id = identification
		self.radius = 20
		self.others = []

	def detect_bond(self, bond):
		myBondPosition = -1
		if bond.position[0] > self.position[0] - self.radius  \
		and bond.position[0] < self.position[0] + self.radius and \
		bond.position[1] > self.position[1] - self.radius and \
		bond.position[1] < self.position[1] + self.radius:
			r = int(math.sqrt((myBondPosition[0] - bond.position[0])**2 \
			+ (myBondPosition[1] - bond.position[1])**2))
			if r <= self.radius:
				# Isto não vai funcionar
				if self.active:
					self.active = 0
				else:
					self.active = 1
		else:
			return

	def print_bond(self, screen):
		if self.active == 1:
			pygame.draw.circle(screen, (0, 0, 0), (int(self.position[0]), \
				int(self.position[1])), int(self.radius), 0)
		else:
			pygame.draw.circle(screen, (0, 0, 0), (int(self.position[0]), \
			int(self.position[1])), int(self.radius), 1)
