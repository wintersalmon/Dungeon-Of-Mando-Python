# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# Weapon
#

class Weapon:
    def __init__(self, code, name, armor, can_slayer_monsters):
        self.__code   = code # if isinstance(code, WeaponType) else WeaponType.noname
        self.__name   = name
        self.__armor  = armor
        self.__can_slayer_monsters = can_slayer_monsters # if isinstance(__can_slayer_monsters, list) else []

    def __str__(self):
        return self.__name
        
    def code(self):
        return self.__code
        
    def name(self):
        return self.__name
    
    def armor(self):
        return self.__armor
        
    def reset_slayer_monster(self):
        self.__can_slayer_monsters.clear()
        
    def add_slayer_monster(self, monster_code):
        self.__can_slayer_monsters.append(monster_code)

    def can_slayer_monster(self,monster):
        return monster.code() in self.__can_slayer_monsters
