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
    
    def execute(self):
        if self.turn_action == 0:   # Pass
            self.action_pass()
            return True
            
        elif self.turn_action == 1 and self.turn_draw_monster != None: # Add Monster To Dungeon
            self.action_monster_add()
            return True
            
        elif self.turn_action == 2 and self.turn_remove_weapon != None: # Remove Monster And Weapon
            self.action_monster_remove()
            self.action_weapon_remove()
            return True
        else:
            return False
            
            
    def end(self):
        # if first player is head of player_in_round move to tail
        if self.turn_player == self.player_in_round[0]:
            player = self.player_in_round.pop(0)
            self.player_in_round.append(player)
        
    def action_pass(self):
        # remove player from player_in_round
        self.player_in_round.remove(self.turn_player)
    
    def action_monster_add(self):
        # move top monster_in_deck to monster_in_dungeon
        monster = self.monster_in_deck.pop(-1)
        self.monster_in_dungeon.append(monster)
        
    def action_monster_remove(self):
        # remove top monster_in_deck
        self.monster_in_deck.pop(-1)
    
    def action_weapon_remove(self):
        # remove selected_weapon in weapon_in_dungeon
        try:
            self.weapon_in_dungeon.remove(self.turn_remove_weapon)
        except:
            return False
        return True
        # self.weapon_in_dungeon.pop(self.turn_remove_weapon)
    