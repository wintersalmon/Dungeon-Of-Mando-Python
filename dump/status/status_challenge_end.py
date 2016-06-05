# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusChallengeEnd
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusChallengeEnd(Status):
    def __init__(self):
        super().__init__('StatusChallengeEnd', StatusType.challenge_end, StatusType.round_end)
    
    def update(self, dungeon):
        print('StatusChallengeEnd')
        
        hero = dungeon.challenge.challenge_hero
        challenger = dungeon.challenge.challenge_player
        if hero.armor() > 0:
            challenger.gain_victory_point()
        else:
            challenger.lose_life_point()
            
        return self.success_end_status()