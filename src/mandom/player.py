# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# player


class Player(object):
    def __init__(self, name):
        self.__name = name
        self.__victory_point = 0
        self.__life_point = 2
        self.__removed_weapons = []
        self.__removed_monsters = []

    def __str__(self):
        return self.__name

    def name(self):
        return self.__name

    def victory_point(self):
        return self.__victory_point

    def life_point(self):
        return self.__life_point

    def gain_victory_point(self):
        self.__victory_point += 1
        return self.__victory_point

    def lose_life_point(self):
        self.__life_point -= 1
        if self.__life_point < 0:
            self.__life_point = 0
        return self.__life_point

    def reset(self):
        self.__victory_point = 0
        self.__life_point = 2


def test_player():
    names = ['aaa', 'bbb', 'ccc', 'ddd']
    players = list(map(lambda name: Player(name), names))
    for player in players:
        print(type(player), player, player.life_point(), player.victory_point())


if __name__ == "__main__":
    test_player()
