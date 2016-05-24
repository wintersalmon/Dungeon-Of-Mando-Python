# Salmonjoon
# DungeonOfMandom
# 2016.05.19

import monster

class Weapon:
    def __init__(self, name, armor, can_slayer_monster_list):
        self.__name   = name
        self.__armor  = armor
        if isinstance(can_slayer_monster_list,list):
            self.__can_slayer_monster_list = can_slayer_monster_list
        else:
            self.__can_slayer_monster_list = []

    def __str__(self):
        return self.__name
    
    def name(self):
        return self.__name
    
    def armor(self):
        return self.__armor

    def can_slayer_monster(self,monster):
        return monster.name() in self.__can_slayer_monster_list



## Actual Weapons

class TorchWeapon(Weapon):
    monster_list = [monster.GoblinMonster.NAME, monster.SkeletonWarriorMonster.NAME, monster.OrkMonster.NAME]
    def __init__(self):
        super().__init__('Torch', 0, TorchWeapon.monster_list)

class HolyGrailWeapon(Weapon):
    monster_list = [monster.SkeletonWarriorMonster.NAME, monster.VampireMonster.NAME, monster.ReaperMonster.NAME]
    def __init__(self):
        super().__init__('HolyGrail', 0, HolyGrailWeapon.monster_list)

class SpearWeapon(Weapon):
    monster_list = [monster.DragonMonster.NAME]
    def __init__(self):
        super().__init__('Spear', 0, SpearWeapon.monster_list)

class ArmorWeapon(Weapon):
    monster_list = []
    def __init__(self):
        super().__init__('Armor', 5, ArmorWeapon.monster_list)

class ShieldWeapon(Weapon):
    monster_list = []
    def __init__(self):
        super().__init__('Shield', 3, ShieldWeapon.monster_list)

class HeroSwordWeapon(Weapon):
    monster_list = []
    def __init__(self):
        super().__init__('HeroSword', 0, HeroSwordWeapon.monster_list)

    def DeclareSlayerableMonster(self,monsterName):
        self.__can_slayer_monster_list.clear()
        self.__can_slayer_monster_list.append(monsterName)
