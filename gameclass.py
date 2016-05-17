import pygame, game, load, math, random

resources = load.load_everthing()

# Tela de menu
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

# Tela Principal do game
class gameStage(Stage):
	
	controlID = 0

	def __init__(self, image, buttons, layouts, size, gameMode):
		Stage.__init__(self, image, buttons, layouts, size)
		self.gameMode = gameMode
		self.bars = []
		self.bonds = []
		self.grounds = []

	# Guarda todos os objetos do tipo juncao
	def generateBonds(self):
		for bar in self.bars:
			for bond in bar.bonds:
				self.bonds.append(bond)

	def createBar(self, number):
		for i in range(number):
			self.bars.append(barObject(gameStage.controlID))
			gameStage.controlID += 1

		self.generateBonds()	

	def createGround(self, positions):
		for i in range(len(positions)):
			self.grounds.append(groundObject(positions[i], 0, i))

	def detectBar(self):
		objectList = []
		for bar in self.bars:
			if bar.detect_bar():
				objectList.append(bar)
				for bond in bar.bonds:
					if bond.active:
						objectList.append(bond)

		return objectList

	def print_bars(self, screen):
		for bar in self.bars:
			bar.print_bar(screen)
			for bond in bar.bonds:
				bond.print_bond(screen)
				
	def print_ground(self, screen):
		for ground in self.grounds:
			ground.print_ground(screen)

	def execute_menu(self, screen, conf):
		pygame.font.init()
		running = True
		keys = [False, False, False]
		if self.gameMode > 0:
			timer = timerObject()
			USEREVENT = 31
			pygame.time.set_timer(USEREVENT, 10)
			if self.gameMode == 1:
				timer.setTime(241)
				self.createBar(14)
			elif self.gameMode == 2:
				timer.setTime(211)
				self.createBar(5)
			elif self.gameMode == 3:
				timer.setTime(181)
				self.createBar(5)
			elif self.gameMode == 4:
				timer.setTime(161)
				self.createBar(5)
			elif self.gameMode == 5:
				timer.setTime(131)
				self.createBar(5)
			elif self.gameMode == 6:
				timer.setTime(101)
				self.createBar(5)
			elif self.gameMode == 7:
				timer.setTime(71)
				self.createBar(5)
			elif self.gameMode == 8:
				timer.setTime(41)
				self.createBar(5)
			elif self.gameMode == 9: 
				timer.setTime(21)
				self.createBar(5)
		else:
			self.createBar(10)
			self.createGround([[0, 2*screen.get_height()/3], \
			[2*screen.get_width()/3, 2*screen.get_height()/3]])

		try:
			timer.start()
		except:
			pass
		
		while True:
			screen.fill(0)		
			self.print_stage(screen, conf)
			self.print_ground(screen)
			self.print_bars(screen)
			command = self.detect_button()
			if running:
				objectList = self.detectBar()
			for event in pygame.event.get():
				try:
					if event.type == USEREVENT:
						timer.updateTime()
				except:
					pass
				
				if event.type == pygame.MOUSEBUTTONDOWN:
					if not command == None:
						if not command == 2:
							try:
								timer.finish()
							except:
								pass
						if command == 5:
							# Gerar matriz de adjacência
							pass
						else:
							return command

					if event.button == 1:
						keys[0] = True

					if event.button == 2:
						keys[1] = True

					if event.button == 3:
						keys[2] = True

				if event.type == pygame.QUIT:
					game.ex()

				if event.type == pygame.MOUSEBUTTONUP:
					if event.button == 1:
						keys[0] = False
					if event.button == 2:
						keys[1] = False
					if event.button == 3:
						keys[2] = False

			try:
				if timer.checkEnd():
					timer.finish()
					running = False
					objectList = []
			except:
				pass
			
			cursor = pygame.mouse.get_pos()
			if len(objectList) > 0:
				if keys[0]:
					objectList[0].move(cursor)
				if keys[1]:
					objectList[1].change_bond_status(self.bonds)
					keys[1] = False
				if keys[2]:
					objectList[0].rotate(cursor)

			try:
				timer.printTime(screen, [screen.get_width() - 10, 50])
			except:
				pass
			
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

# Botão
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

#Botão com mais de 1 opção de escolha
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
		self.bonds = []
		self.create_bond(2)
		barObject.controlID += 2
		self.id = identification
		# Cria posicao falsa do cursor
		cursor = (random.randint(-1000, 1000)), (random.randint(-1000, 1000))
		self.rotate(cursor)
		self.update_bond_position()

	# Atualiza as posições das juncoes em relação a barra de treliça
	def update_bond_position(self):
		center = (self.size[0]/2, self.size[1]/2)
		self.bonds[0].position = (self.position[0] + center[0] - \
		math.cos(self.angle) * (self.sizeBase[0]/2), \
		self.position[1] + center[1] - math.sin(self.angle) * (self.sizeBase[0])/2)
		self.bonds[1].position = (self.position[0] + center[0] + \
		math.cos(self.angle) * (self.sizeBase[0]/2), \
		self.position[1] + center[1] + math.sin(self.angle) * (self.sizeBase[0])/2)

	# Detecta se o cursor está dentro dos limites da treliça.
	# Detecta também qual junta o cursor do mouse esta mais proximo
	def detect_bar(self):
		cursor = pygame.mouse.get_pos()
		position = (int(cursor[0] - self.position[0]), int(cursor[1] - self.position[1]))
		if cursor[0] > self.position[0] and cursor[0] < self.position[0] + self.size[0] and \
		cursor[1] > self.position[1] and cursor[1] < self.position[1] + self.size[1]:
			if self.mask.get_at(position):
				r1 = math.sqrt((self.bonds[0].position[0] - cursor[0])**2 + \
				(self.bonds[0].position[1] - cursor[1])**2)
				r2 = math.sqrt((self.bonds[1].position[0] - cursor[0])**2 + \
				(self.bonds[1].position[1] - cursor[1])**2)
				if r1 < r2:
					self.bonds[0].active = 1
					self.bonds[1].active = 0
				else:
					self.bonds[1].active = 1
					self.bonds[0].active = 0

				return 1
			else:
				self.bonds[0].active = self.bonds[1].active = 0
				return 0
		else:
			self.bonds[0].active = self.bonds[1].active = 0
			return 0

	def print_bar(self, screen):
		screen.blit(self.image, self.position)

	# Atualiza a posicao do centro da barra em relacao ao eixo central 
	# com a posicao do mouse apenas se nao houver juntas
	def move(self, cursor): 
		for bond in self.bonds:
			if len(bond.joints) > 0:
				return

		size = self.mask.get_size()
		self.position[0] = cursor[0] - size[0]/2
		self.position[1] = cursor[1] - size[1]/2
		self.update_bond_position()

	# Rotaciona a barra em relacao ao eixo central com a posicao do mouse
	# apenas se nao houver juntas
	def rotate(self, cursor):
		for bond in self.bonds:
			if len(bond.joints) > 0:
				return

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
			self.bonds.append(bond(i))

class groundObject(object):
	def __init__(self, position, friction, identification):
		picture = resources[4]
		resize = 1
		self.image = pygame.transform.scale(picture, \
		(int(picture.get_width()*resize), int(picture.get_height()*resize)))
		self.size = (self.image.get_width(), self.image.get_height())
		self.position = position
		self.friction = friction
		self.id = identification
		# Precisa de bond também

	def print_ground(self, screen):
		screen.blit(self.image, self.position)

	# função para atrito

# Objeto que junta barras
class bond(object):
	def __init__(self, identification):
		self.position = (0, 0)
		self.active = 0
		self.id = identification
		self.radius = 20
		self.joints = []
		self.others = []

	# Cria vinculo com objeto do tipo juncao que esteja tocando
	def change_bond_status(self, bonds):
		for bond in bonds:
			r = math.sqrt((self.position[0] - bond.position[0])**2 + \
			(self.position[1] - bond.position[1])**2)
			if 2*self.radius >= int(r) and not int(r) == 0:
				remove = False
				for joint in self.joints:
					if joint == bond:
						remove = True
						self.joints.remove(bond)
						bond.joints.remove(self)
				
				if not remove:		
					self.joints.append(bond)
					bond.joints.append(self)

	def print_bond(self, screen):
		if len(self.joints) > 0:
			pygame.draw.circle(screen, (0, 0, 0), (int(self.position[0]), \
				int(self.position[1])), int(self.radius), 0)
		else:
			pygame.draw.circle(screen, (0, 0, 0), (int(self.position[0]), \
			int(self.position[1])), int(self.radius), 1)

# Temporizador
class timerObject(object):

	started = False
	lastTime = 0

	def __init__(self):
		self.time = 0

	def setTime(self, time):
		if not timerObject.started:
			self.time = time*1000
		else:
			self.time = timerObject.lastTime

	def start(self):
		if not timerObject.started:
			timerObject.started = True

	def updateTime(self):
		if timerObject.started:
			self.time -= 10

	def checkEnd(self):
		if self.time <= 0:
			timerObject.lastTime = self.time = 0
			return True
		else:
			timerObject.lastTime = self.time
			return False

	def finish(self):
		if timerObject.started:
			timerObject.started = False

	def printTime(self, screen, position):
		font = pygame.font.Font(None, 50)
		survivedtext = font.render(str(int((self.time) / \
		60000)) + ":" + str(int((self.time) \
		/ 1000 % 60)).zfill(2), True, (0, 0, 0))
		textRect = survivedtext.get_rect()	
		textRect.topright = position
		screen.blit(survivedtext, textRect)
