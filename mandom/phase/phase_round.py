# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseRound
#

import random

class PhaseRound():
    def __init__(self, phase_game):
        self.__phase_game  = phase_game
        
        self.player_in_round    = list()
        self.monster_in_deck    = list()
        self.monster_in_dungeon = list()
        self.weapon_in_dungeon  = list()
        
        self.last_challenger = None
    
    def reset(self):
        self.monster_in_deck    = self.__phase_game.clone_monster_list()
        self.monster_in_dungeon = list()
        self.weapon_in_dungeon  = self.__phase_game.clone_weapon_list()
        self.player_in_round    = self.__phase_game.clone_player_list()
        self.last_challenger    = None


    def start(self):
        self.reset()
        self.shuffle_deck()
        
    def has_next_turn(self):
        # more then one player in round
        if len(self.player_in_round) > 1:
            return True
        else:
            return False
        
    def end(self):
        self.last_challenger = self.player_in_round[0] if self.player_in_round else None
    

    def shuffle_deck(self):
        deck_size = len(self.monster_in_deck)
        random.seed()
        for i in range(0,100):
            idx = random.randrange(0,deck_size)
            monster = self.monster_in_deck.pop(idx)
            self.monster_in_deck.append(monster)