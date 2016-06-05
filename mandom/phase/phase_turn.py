# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseTurn
#

class PhaseTurn():
    def __init__(self, phase_round):
        self.__phase_round = phase_round
        self.monster_in_deck     = phase_round.monster_in_deck
        self.monster_in_dungeon  = phase_round.monster_in_dungeon
        self.weapon_in_dungeon   = phase_round.weapon_in_dungeon
        self.player_in_round     = phase_round.player_in_round
        
        self.turn_action = None
        self.turn_player = None
        self.turn_draw_monster  = None
        self.turn_remove_weapon = None

    def reset(self):
        self.monster_in_deck     = self.__phase_round.monster_in_deck
        self.monster_in_dungeon  = self.__phase_round.monster_in_dungeon
        self.weapon_in_dungeon   = self.__phase_round.weapon_in_dungeon
        self.player_in_round     = self.__phase_round.player_in_round
        
        self.turn_action = None
        self.turn_player = self.player_in_round[0] if self.player_in_round else None
        self.turn_draw_monster = self.monster_in_deck[-1] if self.monster_in_deck else None
        self.turn_remove_weapon = None
    
    def start(self):
        self.reset()
    
    def end(self):
        # if first player is head of player_in_round move to tail
        if self.cur_turn_player == self.player_in_round[0]:
            player = self.player_in_round.pop(0)
            self.player_in_round.append(player)
        
        
    def action_pass(self):
        # remove player from player_in_round
        self.player_in_round.remove(self.cur_turn_player)
    
    def action_monster_add(self):
        # move top monster_in_deck to monster_in_dungeon
        monster = self.monster_in_deck.pop(-1)
        self.monster_in_dungeon.append(monster)
    
    def action_weapon_remove(self):
        # remove top monster_in_deck
        # remove selected_weapon in weapon_in_dungeon
        self.monster_in_deck.pop(-1)
        self.weapon_in_dungeon.remove(self.selected_weapon)
    