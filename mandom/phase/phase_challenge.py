# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseChallenge
#

from mandom.hero   import Hero

class PhaseChallenge():
    def __init__(self, phase_round):
        self.__phase_round = phase_round
        
        self.monster_in_dungeon  = self.__phase_round.monster_in_dungeon
        self.weapon_in_dungeon   = self.__phase_round.weapon_in_dungeon
        self.player_in_round     = self.__phase_round.player_in_round
        
        self.challenge_player = None
        self.challenge_hero = Hero()

    def reset(self):
        self.monster_in_dungeon  = self.__phase_round.monster_in_dungeon
        self.weapon_in_dungeon   = self.__phase_round.weapon_in_dungeon
        self.player_in_round     = self.__phase_round.player_in_round
        
        self.challenge_player = self.player_in_round[0] if self.player_in_round else None
        self.challenge_hero.equipe_weapon(self.weapon_in_dungeon)
        
    def start(self):
        self.reset()
        
    def has_next_battle(self):
        # if armor > 0 and monsters > 0 continue
        armor    = self.challenge_hero.armor()
        monsters = len(self.monster_in_dungeon)
        
        if armor > 0 and monsters > 0:
            return True
        else:
            return False
        
    def end(self):
        # hero has armor left   : player gain victorypoint
        # hero has no life left : player lose lifepoint
        if self.hero.armor() > 0:
            self.challenge_player.gain_victory_point()
        else:
            self.challenge_player.lose_life_point()