import random
import json
import time

class Weapon:

    weapon_name = ["bringer", "widow", "world", "endless", "chaos"]

    def __init__(self):
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
        self.name = str(random.choice(self.weapon_name) + " " + random.choice(self.weapon_name))
        if weapon_type == "ASSAULT_RIFLE":
            self.dmg = random.randint(1, 20)
            self.clip_size = random.randint(15, 50)
            self.rarity = random.randint(0, 10)
        elif weapon_type == "SHOTGUN":
            if random.randint(0, 1) == 1 :
                self.is_bolt_action = True
            else:
                self.is_bolt_action = False
            self.dmg = random.randint(80, 100)
            self.clip_size = random.randint(4, 11)
            self.rarity = random.randint(0, 10)
        elif weapon_type == "SNIPER_RIFLE":
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

        


        
