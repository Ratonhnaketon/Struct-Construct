import pygame, images, audio

# Load game and profile

path = "Profile/"

def load():
	check = 0
	check += audio.load_audio()
	check += images.load_image()
	if check > 0:
		print("Error:" + str(check))
		exit(check)
	return conf()

def conf():
	while True:
		try:
			f = open(path + "conf.txt", "r")
		except IOError as e:
			write_default(path)
		else:
			break
	info = read_conf(f)
	f.close()
	return info.copy()

# If file 'conf.txt' does not exit create one and set to default

def write_default(path):
	f = open(path + "conf.txt", "w") 
	pygame.init()
	f.write(str(pygame.display.Info().current_w) + " " + str(pygame.display.Info().current_h) + "\n")
	pygame.quit()
	f.write("0.4\n")
	f.write("0.3\n")
	f.write("1\n")	
	f.write("None\n")
	f.close()
	return f

def read_conf(f):
	info = {}
	i = []
	for word in f.readline().split():
		i.append(int(word))
	info['size'] = i
	i = []
	for word in f.readline().split():
		i.append(float(word))
	info['brightness'] =  i
	i = []
	for word in f.readline().split():
		i.append(float(word))
	info['sound'] =  i
	i = []
	for word in f.readline().split():
		i.append(int(word))
	info['mode'] =  i
	info['save'] =  f.readline().split()
	return info.copy()
     
def load_everthing():
	resources = [images.background_menu, images.Menubutton, images.Cab1, \
	images.Cab2, images.Cab3, images.Cab4, images.Cab5, images.tronco1, \
	images.tronco2, images.tronco3, images.braco1, images.braco11, images.seta, \
	images.braco2, images.braco22, images.perna21, images.perna22, images.icon,\
	images.eye]
	return resources

def change_conf(info, option):
	if(option == 100):
		if info['mode'] == [1]:
			info['mode'] = [0]
			return info
		if info['mode'] == [0]:
			info['mode'] =  [1]
			return info
	if(option > 100 and option < 103):
		if info['size'] == [640, 480]:
			if option == 102:
				info['size'] = [800, 600]
			return info
		if info['size'] == [800, 600]:
			if option == 101:
				info['size'] = [640, 480]
			if option == 102:
				info['size'] = [960, 720]
			return info
		if info['size'] == [960, 720]:
			if option == 101:
				info['size'] = [800, 600]
			if option == 102:
				info['size'] = [1024, 768]
			return info
		if info['size'] == [1024, 768]:
			if option == 101:
				info['size'] = [960, 720]	
			if option == 102:
				info['size'] = [1152, 864]
			return info
		if info['size'] == [1152, 864]:
			if option == 101:
				info['size'] = [1024, 768]
			if option == 102:
				info['size'] = [1280, 720]
			return info
		if info['size'] == [1280, 720]:
			if option == 101:
				info['size'] = [1152, 864]
			if option == 102:
				info['size'] = [1280, 1024]
			return info
		if info['size'] == [1280, 1024]:
			if option == 101:
				info['size'] = [1280, 720]
			else:
				info['size'] = [1366, 760]
			return info
		if info['size'] == [1366, 760]:
			if option == 101:
				info['size'] = [1280, 1024]
			else:
				info['size'] = [1440, 960]
			return info
		if info['size'] == [1440, 960]:
			if option == 101:
				info['size'] = [1366, 760]
			else:
				info['size'] = [1600, 900]
			return info
		if info['size'] == [1600, 900]:
			if option == 101:
				info['size'] = [1440, 960]
			else:
				info['size'] = [1920, 1080]
			return info
		if info['size'] == [1920, 1080]:
			if option == 101:
				info['size'] = [1600, 900]
			return info

def save_conf(info):
	f = open(path + "conf.txt", "w") 
	f.write(str(info['size'][0]) + " " +  str(info['size'][1]) + "\n")
	f.write(str(info['brightness'][0]) + "\n")
	f.write(str(info['sound'][0]) + "\n")
	f.write(str(info['mode'][0]) + "\n")
	f.write(str(info['save'][0]) + "\n")
	f.close()