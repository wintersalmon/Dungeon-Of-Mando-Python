# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# hero
#

class Hero():
    def __init__(self):
        self.__starting_armor = 3
        self.__armor = 0
        self.__equiped_weapon_list = list()
    
    def armor(self):
        return self.__armor
        
    def equipe_weapon(self, weapon_list):
        armor = self.__starting_armor
        for weapon in weapon_list:
            armor += weapon.armor()
        self.__armor = armor
        self.__equiped_weapon_list = weapon_list
    