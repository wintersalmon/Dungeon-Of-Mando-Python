# Salmonjoon
# DungeonOfMandom
# 2016.06.01
#
# PhaseBattle
#

class PhaseBattle():
    def __init__(self, phase_challenge):
        self.monster_in_dungeon = phase_challenge.monster_in_dungeon
        self.weapon_in_dungeon  = phase_challenge.weapon_in_dungeon
        self.challenge_player   = phase_challenge.challenge_player
        self.challenge_hero     = phase_challenge.challenge_hero
        
        self.battle_monster = None
        self.battle_damage  = 0
        self.battle_win     = False

        
    def reset(self):
        self.battle_monster = self.monster_in_dungeon[-1] if self.monster_in_dungeon else None
        self.battle_damage  = self.battle_monster.damage() if self.battle_monster else 0
        self.battle_win     = False

    def start(self):
        self.reset()
        
    def execute(self):
        for weapon in self.weapon_in_dungeon:
            if weapon.can_slayer_monster(self.battle_monster):
                self.battle_win = True
                break

        if self.battle_win:
            return
        else:
            self.challenge_hero.give_damage(self.battle_damage)

    def end(self):
        self.monster_in_dungeon.remove(self.battle_monster)
        

    