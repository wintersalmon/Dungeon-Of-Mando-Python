# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseGame
#


from mandom.monsters.monster_dragon import MonsterDragon
from mandom.monsters.monster_goblin import MonsterGoblin
from mandom.monsters.monster_golam import MonsterGolam
from mandom.monsters.monster_ork import MonsterOrk
from mandom.monsters.monster_reaper import MonsterReaper
from mandom.monsters.monster_satan import MonsterSatan
from mandom.monsters.monster_skeleton_warrior import MonsterSkeletonWarrior
from mandom.monsters.monster_vampire import MonsterVampire
from mandom.weapons.weapon_armor import WeaponArmor
from mandom.weapons.weapon_hero_sword import WeaponHeroSword
from mandom.weapons.weapon_holy_grail import WeaponHolyGrail
from mandom.weapons.weapon_shield import WeaponShield
from mandom.weapons.weapon_spear import WeaponSpear
from mandom.weapons.weapon_torch import WeaponTorch


class PhaseGame(object):
    def __init__(self):
        self.__monster_in_game = list()
        self.__weapon_in_game = list()
        self.__player_in_game = list()

        # init __monster_in_game
        self.__monster_in_game.append(MonsterGoblin())
        self.__monster_in_game.append(MonsterGoblin())
        self.__monster_in_game.append(MonsterSkeletonWarrior())
        self.__monster_in_game.append(MonsterSkeletonWarrior())
        self.__monster_in_game.append(MonsterOrk())
        self.__monster_in_game.append(MonsterOrk())
        self.__monster_in_game.append(MonsterVampire())
        self.__monster_in_game.append(MonsterVampire())
        self.__monster_in_game.append(MonsterGolam())
        self.__monster_in_game.append(MonsterGolam())
        self.__monster_in_game.append(MonsterReaper())
        self.__monster_in_game.append(MonsterSatan())
        self.__monster_in_game.append(MonsterDragon())

        # init __weapon_in_game
        self.__weapon_in_game.append(WeaponArmor())
        self.__weapon_in_game.append(WeaponHeroSword())
        self.__weapon_in_game.append(WeaponHolyGrail())
        self.__weapon_in_game.append(WeaponShield())
        self.__weapon_in_game.append(WeaponSpear())
        self.__weapon_in_game.append(WeaponTorch())

    def start(self):
        for player in self.__player_in_game:
            player.reset()

    def has_next_round(self):
        # has winner
        for player in self.__player_in_game:
            if player.victory_point() == 2:
                return False

        # has only one surviver
        survivers = 0
        for player in self.__player_in_game:
            if player.life_point() > 0:
                survivers += 1

        if survivers == 1:
            return False

        return True

    def end(self):
        pass

    def add_player(self, player):
        self.__player_in_game.append(player)

    def remove_player(self, player):
        self.__player_in_game.remove(player)

    def monster_list(self):
        return self.__monster_in_game

    def weapon_list(self):
        return self.__weapon_in_game

    def player_list(self):
        return self.__player_in_game

    def clone_monster_list(self):
        return self.__monster_in_game.copy()

    def clone_weapon_list(self):
        return self.__weapon_in_game.copy()

    def clone_player_list(self):
        return self.__player_in_game.copy()
