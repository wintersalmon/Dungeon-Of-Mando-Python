# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusBattleExecute
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType
from mandom.dungeon import Dungeon

class StatusBattleExecute(Status):
    def __init__(self):
        super().__init__('StatusBattleExecute', StatusType.battle_execute, StatusType.battle_end)
    
    def update(self,dungeon):
        print('StatusBattleExecute')
        
        monster = dungeon.battle.battle_monster
        weapons = dungeon.battle.weapon_in_dungeon
        hero    = dungeon.battle.challenge_hero
        
        battle_lost = True
        for weapon in weapons:
            if weapon.can_slayer_monster(monster):
                battle_lost = False
        
        if battle_lost:
            damage = monster.damage()
            hero.give_damage(damage)
        
        return self.success_end_status()
        
