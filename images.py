import pygame, os.path

path = "Resources/Images/"
exten = ".png"

def load_image():
	check = 0
	return check

background_menu = pygame.image.load(path + "Cover_Menu" + exten)  # 0
Menubutton = pygame.image.load(path + "Menubutton" + exten) # 1
Cab1 = pygame.image.load(path + "cabe1" + exten) # 2
Cab2 = pygame.image.load(path + "cabe2" + exten) # 3
Cab3 = pygame.transform.flip(Cab2, True, False) # 4 
Cab4 = pygame.image.load(path + "cabe3" + exten) # 5
Cab5 = pygame.transform.flip(Cab4, True, False) # 6
tronco1 = pygame.image.load(path + "tronco1" + exten) # 7
tronco2 = pygame.image.load(path + "tronco2" + exten) # 8
tronco3 = pygame.transform.flip(tronco2, True, False) # 9
braco1 = pygame.image.load(path + "braco1" + exten) # 10 
braco11 = pygame.image.load(path + "braco11" + exten) # 11
seta = pygame.image.load(path + "seta" + exten) # 12
braco1 = pygame.transform.scale(braco1, (int(braco1.get_width()*0.5), int(braco1.get_height()*0.5)))
braco11 =  pygame.transform.scale(braco11, (int(braco11.get_width()*0.5), int(braco11.get_height()*0.5)))
braco2 = pygame.transform.flip(braco1, True, False) # 13
braco22 = pygame.transform.flip(braco11, True, False) # 14
perna21 = pygame.image.load(path + "perna" + exten) # 15
perna21 = pygame.transform.scale(perna21, (int(perna21.get_width()*0.4), int(perna21.get_height()*0.4)))
perna22 =  pygame.transform.flip(perna21, True, False) # 16
icon = pygame.image.load(path + "icon" + exten) # 17
eye = pygame.image.load(path + "eye" + exten) # 18