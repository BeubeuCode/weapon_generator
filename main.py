from Weapon import Weapon
from CommandHandler import CommandHandler

import time
import sys

def create_json_file(arg):
	filename = "Weapons" + str(time.time()) + ".json"
	f = open(str(filename), "w")
	f.write(arg)

def weapon_generation(l, weapon_type):
	if l is not int:
		l = int(l)
	
	if l == 1:
		w = Weapon()
		if weapon_type == "ASSAULT_RIFLE" or weapon_type == "SHOTGUN" or weapon_type == "SNIPER_RIFLE":
			w.generate(weapon_type)
		else:
			print("FATAL ERROR")
			raise ValueError("INVALID WEAPON TYPE")
			exit(1)
		w.generate_json(w)
	else:
		list = []
		if weapon_type == "ASSAULT_RIFLE" or weapon_type == "SHOTGUN" or weapon_type == "SNIPER_RIFLE":
			w.generate(weapon_type)
		else:
			print("FATAL ERROR")
			raise ValueError("INVALID WEAPON TYPE")
			exit(1)
def main():
	start = time.time()
	
	if len(sys.argv) == 1:
		CommandHandler.printHelp()

	elif sys.argv[1] == "test" :
		weapon_generation(1, "SHOTGUN")
		exit(0)

	elif len(sys.argv) < 3:
		CommandHandler.printHelp()

	elif len(sys.argv) == 3:
		weapon_generation(int(sys.argv[1]), sys.argv[2])

	end = time.time()

	print("Time elapsed " + str(end - start))
 

if __name__ == "__main__":
	main()