# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusNextBattle
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusNextBattle(Status):
    def __init__(self):
        super().__init__('StatusNextBattle', StatusType.next_battle, StatusType.battle_start, StatusType.challenge_end)
    
    def update(dungeon):
        print('StatusNextBattle')
        
        monster_count = len(dungeon.challenge.monster_in_dungeon)
        hero_armor    = dungeon.challenge.challenge_hero.armor()
        
        if hero_armor > 0 and monster_count > 0:
            return self.success_end_status()
        else:
            return self.failed_end_status()