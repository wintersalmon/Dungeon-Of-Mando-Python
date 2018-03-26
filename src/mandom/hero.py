# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# hero
#


class Hero(object):
    def __init__(self):
        self.__basic_armor = 3
        self.__armor = 0
        self.__weapons_equipped = list()

    def armor(self):
        return self.__armor

    def give_damage(self, damage):
        armor_left = self.__armor - damage
        self.__armor = armor_left if armor_left > 0 else 0

    def equip_weapon(self, weapons_equipped):
        self.__weapons_equipped = weapons_equipped

    def reset_armor(self):
        equipped_weapon_armor = [weapon.armor() for weapon in self.__weapons_equipped]
        total_armor = sum(equipped_weapon_armor)
        self.__armor = self.__basic_armor + total_armor
