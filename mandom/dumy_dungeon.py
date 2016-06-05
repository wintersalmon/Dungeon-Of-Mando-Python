# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# DumyDungeon
#

class DumyPhaseGame():
    def __init__(self):
        self.counter = -1
        self.max_counter = 3
        
    def has_next_round(self):
        self.counter += 1
        return self.counter < self.max_counter

class DumyPhaseRound():
    def __init__(self):
        self.counter = -1
        self.max_counter = 3

        
    def has_next_turn(self):
        self.counter += 1
        return self.counter < self.max_counter


class DumyPhaseChallenge():
    def __init__(self):
        self.counter = -1
        self.max_counter = 3

        
    def has_next_battle(self):
        self.counter += 1
        return self.counter < self.max_counter



class DumyDungeon():
    def __init__(self):
        self.phase_game   = DumyPhaseGame()
        self.phase_round  = DumyPhaseRound()
        self.phase_challenge = DumyPhaseChallenge()
