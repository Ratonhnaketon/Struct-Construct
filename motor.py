class motor(object):
	def __init__(self, n, elements):
		self.n = n
		self.elements = elements
		# Declaracao de matriz
		# Matrix = [[0 for x in range(w)] for y in range(h)] 

	def genMatriz(self, ):
		pass

	# Adiciona um 'peso' em um dos nos da estrutura aleatoriamente
	def addForce(self):
		pass

	# Soluciona a estrutura
	# 1º: Verifica se e isostatica
	# 2º: Recebe uma matriz e descobre o valor das forcas em cada no e verifica
	# se nao e maior que a forca limite do no
	def solution(self):
		pass
		if(firstStep(self)):
			secondStep(self)

	# Estrutura isostatica:
	# m = 2j - 3
	def firstStep(self):
		pass
		if numero_de_barras >= (2*numero_de_nos - 3):
			if numero_de_barras == (2*numero_de_nos - 3):
				print("A matriz é isoestática!")
				return true
			else:
				print("A matriz é hiperestática!")
				return false

		print("A matriz é hipostática!")
		return false

	def secondStep(self):
		pass

#########################################################################################################################################################

		# Aqui tem um tuto de como baixar as paradas no Arch
		# http://antarch.calepin.co/setting-up-a-python-environment-in-arch-linux-advanced.html
		# Baixando o Pip
		# http://stackoverflow.com/questions/27557516/how-do-i-install-pip-on-arch-linux

		# Aqui tem um tuto de como usar a 'scipy.linalg'
		# http://docs.scipy.org/doc/scipy/reference/tutorial/linalg.html		

		# Aqui tem um tuto de como instalar o 'SciPy' no ubuntu, Gentoo e Fedora
		# https://www.scipy.org/install.html

#########################################################################################################################################################
		# É... Nao sei inicializa variavel e usar "for"
		# A matriz deve ser inicializada zerada
		# https://pythonhosted.org/apgl/SparseGraph.html#

		matriz[ 2*len(matriz_adjacencia[0]) ][len(matriz_adjacencia)+3]
		
		int coluna = 0
		int linha = 0
		for int lin = 0; lin < 2*len(matriz_adjacencia[0]); lin+=2: # pula de dois em dois, pq uma linha é do "eixo x", e a outra do "eixo y"
			coluna = 0
			for int col = 0; col < len(matriz_adjacencia); col++:
				matriz[col][lin] = -math.cos('angulo_da_barra')*matriz_adjacencia[linha][coluna] # cosseno do angulo da barra
				matriz[col][lin+1] = -math.sin('angulo_da_barra')*matriz_adjacencia[linha][coluna] # seno do angulo da barra
				coluna +=1

			linha +=1
#########################################################################################################################################################
		# Supondo que o suporte de "duas restricoes" esta no mesmo lugar da primeira barra
		# e o suporte de "uma restricao" esta no mesmo lugar da ultima barra
		#
		# Se ele inverter, da nada

		# isso é sempre verdadeiro
		matriz[0][tamanho_col-2] = 1
		matriz[1][tamanho_col-1] = 1
		matriz[tamanho_lin][tamanho_col] = 1
#########################################################################################################################################################
		# Agora inverte a matriz, usando a biblioteca 'numpy'
		# http://docs.scipy.org/doc/numpy-1.10.1/reference/routines.linalg.html
		linalg.inv(matriz)
		# Arranja o lugar onde o peso esta localizado
		# Cria um vetor "resultado" com o tamanho da linha da matriz

		# É assim que se cria um vetor?
		# http://vpython.org/contents/docs/vector.html
		resultado = vector(lin)
		pesos = vector()
		for int lin = 0; lin < len(matriz); lin++:
			for int col = 0; col < len(matriz[0]); col++:
				resultado[lin] += matriz[lin][col]*pesos[col]

		nodeResist(resultado)


	# Calcula a forca limite que os nos aguentam
	# Quanto maior o numero de barras num no, maior sua forca
	def nodeResist(self, []resultado):
		forca = 69169

		for int i = 0; i < len(resultado); i++:
			if(resultado[i] > forca):
				print("A forca no no "+i+" é maior do que deveria ser!")
				return
		print("A ponte esta correta!")
