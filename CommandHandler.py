from Weapon import Weapon

class CommandHandler:
    
    @staticmethod
    def printHelp():
        print("usage : 1st argument is an integer determining the number of weapons generated, the second argument is a string determining the weapon type : \n")
        print("ASSAULT_RIFLE : generates assault rifle type weapon properties")
        print("SHOTGUN : generates shotgun type weapon properties")
        print("SNIPER_RIFLE : generates sniper rifle type weapon properties")
        exit(0)

    @staticmethod
    def argsHandler(arg1=None, arg2=None):
        if arg1 is None and arg2 is None:
            self.printHelp()
        
        if arg1 is not None and arg2 is not None:
            w.weapon_generation(arg1, arg2)
