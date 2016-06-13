# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# Monster
#

class Monster:
    def __init__(self,code,name,damage):
        self.__code   = code # if isinstance(code,MonsterType) else MonsterType.Nothing
        self.__name   = name
        self.__damage = damage

    def __str__(self):
        return self.__name
    
    def code(self):
        return self.__code

    def name(self):
        return self.__name

    def damage(self):
        return self.__damage







'''


if __name__ == "__main__":
    for m_type in MonsterType:
        print(m_type, m_type.value)
    monsters = []
    
    monsters.append(GoblinMonster())
    monsters.append(SkeletonWarriorMonster())
    monsters.append(OrkMonster())
    
    monsters.append(VampireMonster())
    monsters.append(GolamMonster())
    monsters.append(ReaperMonster())
    
    monsters.append(SatanMonster())
    monsters.append(DragonMonster())
    
    print(monsters)





    NAME = 'Goblin'
    NAME = 'SkeletonWarrior'
    NAME = 'Ork'
    NAME = 'Vampire'
    NAME = 'Golam'
    NAME = 'Reaper'
    NAME = 'Satan'
    NAME = 'Dragon'
'''