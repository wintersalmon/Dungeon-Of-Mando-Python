# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseRound
#

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
        
    def has_next_turn(self):
        # more then one player in round
        if len(self.player_in_round) > 1:
            return True
        else:
            return False
        
    def end(self):
        self.last_challenger = self.player_in_round[0] if self.player_in_round else None
    

    