from Weapon import Weapon

import time
import sys

def create_json_file(arg):
	filename = "Weapons" + str(time.time()) + ".json"
	f = open(str(filename), "w")
	f.write(arg)

def weapon_generation(l, weapon_type):
	str_array_json = "["
	for i in range(l):
		w = Weapon()
		w.generate(weapon_type)
		print(w.generate_json())
		str_array_json += w.generate_json()
		if i < l - 1:
			str_array_json += ","
	str_array_json += " ]"
	create_json_file(str_array_json)

def main():
	start = time.time()
	
	if sys.argv[1] == "test" :
		weapon_generation(1, "SHOTGUN")
		exit(0)

	if len(sys.argv) < 3:
		print("usage : 1st argument is an integer determining the number of weapons generated, the second argument is a string determining the weapon type : \n")
		print("ASSAULT_RIFLE : generates assault rifle type weapon properties")
		print("SHOTGUN : generates shotgun type weapon properties")
		print("SNIPER_RIFLE : generates sniper rifle type weapon properties")
		exit(0)


	if len(sys.argv) == 3:
		weapon_generation(int(sys.argv[1]), sys.argv[2])


	
	
	end = time.time()

	print("Time elapsed " + str(end - start))
 

if __name__ == "__main__":
	main()