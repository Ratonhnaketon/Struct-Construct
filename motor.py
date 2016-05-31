import pygame, load

resources = load.load_everthing()

class motor(object):
	def __init__(self):
		self.numberBond = 0
		self.numberBars = 0
		self.active = 0
		self.victory = 0
		self.supports = 0
		# Declaracao de matriz
		# Matrix = [[0 for x in range(w)] for y in range(h)] 

	def genMatriz(self, bonds, numberBond):
		if self.active:
			return

		jointList = []
		self.numberBond = numberBond
		for bond in bonds:
			for joint in bond.joints:
				jointList.append(joint.id)

		jointList = list(set(jointList))
		jointList.sort()
		count = 0
		i = 0
		while i < len(jointList):
			if jointList[i] > 0:
				if jointList[i] % 2 == 1:
					count += 1
					if i + 1 < len(jointList) and jointList[i + 1] % 2 == 0:
						i += 1

				else:
					count += 1
			else:
				self.supports += 1

			i += 1

		self.numberBars = count

	# Adiciona um 'peso' em um dos nos da estrutura aleatoriamente
	def addForce(self):
		pass

	# Soluciona a estrutura
	# 1º: Verifica se e isostatica
	# 2º: Recebe uma matriz e descobre o valor das forcas em cada no e verifica
	# se nao e maior que a forca limite do no
	def solution(self):
		if self.active:
			return
		if self.firstStep():
			if self.secondStep():
				self.victory = True

		self.active = 1

	# Estrutura isostatica:
	# m = 2j - 3
	def firstStep(self):
		if self.supports != 2:
			print("Todos os apoios não foram utilizados")
			return False
		else:
			print("Todos os apoios foram utilizados!")

		if self.numberBars >= (2*self.numberBond - 3):
			if self.numberBars == (2*self.numberBond - 3):
				print("A matriz é isoestática!")
				return True
			else:
				print("A matriz é hiperestática!")

		else:
			print("A matriz é hipostática!")

		return False

	# HUE HUE
	def secondStep(self):
		return True

	# Calcula a forca limite que os nos aguentam
	# Quanto maior o numero de barras num no, maior sua forca
	def nodeResist(self):
		pass

	def printResult(self, screen):
		if self.active:
			if self.victory == True:
				image = pygame.transform.scale(resources[9], \
				(int(screen.get_width()), int(screen.get_height())))
				screen.blit(image, (0, 50))
			else:
				image = pygame.transform.scale(resources[10], \
				(int(screen.get_width()), int(screen.get_height())))
				screen.blit(image, (0, 50))
				