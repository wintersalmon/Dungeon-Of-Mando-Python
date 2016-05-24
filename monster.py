# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Monster

class Monster:
    def __init__(self,name,damage):
        self.__name   = name
        self.__damage = damage

    def __str__(self):
        return self.__name

    def name(self):
        return self.__name

    def damage(self):
        return self.__damage


## Actual Monsters

class GoblinMonster(Monster):
    NAME = 'Goblin'
    def __init__(self):
        super().__init__(GoblinMonster.NAME, 1)

class SkeletonWarriorMonster(Monster):
    NAME = 'SkeletonWarrior'
    def __init__(self):
        super().__init__(SkeletonWarriorMonster.NAME, 2)

class OrkMonster(Monster):
    NAME = 'Ork'
    def __init__(self):
        super().__init__(OrkMonster.NAME, 3)

class VampireMonster(Monster):
    NAME = 'Vampire'
    def __init__(self):
        super().__init__(VampireMonster.NAME, 4)

class GolamMonster(Monster):
    NAME = 'Golam'
    def __init__(self):
        super().__init__(GolamMonster.NAME, 5)

class ReaperMonster(Monster):
    NAME = 'Reaper'
    def __init__(self):
        super().__init__(ReaperMonster.NAME, 6)

class SatanMonster(Monster):
    NAME = 'Satan'
    def __init__(self):
        super().__init__(SatanMonster.NAME, 7)

class DragonMonster(Monster):
    NAME = 'Dragon'
    def __init__(self):
        super().__init__(DragonMonster.NAME, 9) 
