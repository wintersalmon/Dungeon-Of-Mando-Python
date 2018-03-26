# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# DummyDungeon
#


class DummyPhaseGame(object):
    def __init__(self):
        self.counter = -1
        self.max_counter = 3

    def has_next_round(self):
        self.counter += 1
        return self.counter < self.max_counter


class DummyPhaseRound(object):
    def __init__(self):
        self.counter = -1
        self.max_counter = 3

    def has_next_turn(self):
        self.counter += 1
        return self.counter < self.max_counter


class DummyPhaseChallenge(object):
    def __init__(self):
        self.counter = -1
        self.max_counter = 3

    def has_next_battle(self):
        self.counter += 1
        return self.counter < self.max_counter


class DummyDungeon(object):
    def __init__(self):
        self.phase_game = DummyPhaseGame()
        self.phase_round = DummyPhaseRound()
        self.phase_challenge = DummyPhaseChallenge()
