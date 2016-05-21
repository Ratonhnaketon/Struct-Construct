from game import *
from load import *

info = load()
resources = load_everthing()
while True:
	info = run(info, resources)	