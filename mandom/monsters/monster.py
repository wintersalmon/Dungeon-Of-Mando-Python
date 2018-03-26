# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# Monster
#


class Monster:
    def __init__(self, code, name, damage):
        self.__code = code
        self.__name = name
        self.__damage = damage

    def __str__(self):
        return self.__name

    def code(self):
        return self.__code

    def name(self):
        return self.__name

    def damage(self):
        return self.__damage
