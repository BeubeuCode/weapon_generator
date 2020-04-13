import random
import json
import time

class Weapon:
    def __init__(self):
        self.weapon_name = []
        with open('names.json') as json_file:
            names = json.load(json_file)
            self.weapon_name = names["first_word"].copy()

        random.seed(time.time())
        self.type = ""
        self.name = "NULL_WEAPON"
        self.dmg = 0
        self.clip_size = 0
        self.max_ammo = 500
        self.rarity = 0
        self.is_bolt_action = False
    
    def generate(self, weapon_type):
        self.type = str(weapon_type)
        self.name = str(random.choice(self.weapon_name))
        if weapon_type == "ASSAULT_RIFLE":
            self.name = self.name + " Rifle"
            self.dmg = random.randint(1, 20)
            self.clip_size = random.randint(15, 50)
            self.rarity = random.randint(0, 10)
        elif weapon_type == "SHOTGUN":
            self.name = self.name + " Shotgun"
            if random.randint(0, 1) == 1 :
                self.is_bolt_action = True
            else:
                self.is_bolt_action = False
            self.dmg = random.randint(80, 100)
            self.clip_size = random.randint(4, 11)
            self.rarity = random.randint(0, 10)
        elif weapon_type == "SNIPER_RIFLE":
            self.name = self.name + " Sniper"
            self.is_bolt_action = True
            self.dmg = random.randint(90, 100)
            self.clip_size = random.randint(1, 10)
            self.rarity = random.randint(0, 10)

            

    def to_string(self):
        print(self.name + " " + str(self.rarity) + " " + str(self.dmg))

    def generate_json(self):
        returned_json = {}
        returned_json["name"] = self.name
        returned_json["type"] = self.type
        returned_json["rarity"] = self.rarity
        returned_json["is_bolt_action"] = self.is_bolt_action
        returned_json["dmg"] = self.dmg
        returned_json["clip_size"] = self.clip_size
        returned_json["max_ammo"] = self.max_ammo
        return json.dumps(returned_json, sort_keys=False, indent=4)

    def create_json_file(self, arg):
        filename = "Weapons" + str(time.time()) + ".json"
        f = open(str(filename), "w")
        f.write(arg)

    def weapon_generation(self, l, weapon_type):
        str_array_json = "["
        for i in range(l):
            self.generate(weapon_type)
            print(self.generate_json())
            str_array_json += self.generate_json()
            if i < l - 1:
                str_array_json += ","
        str_array_json += " ]"
        self.create_json_file(str_array_json)

    