# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusChallengeStart
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType

class StatusChallengeStart(Status):
    def __init__(self):
        super().__init__('StatusChallengeStart', StatusType.challenge_start, StatusType.next_battle)
    
    def update(dungeon):
        print('StatusChallengeStart')
        
        dungeon.challenge.reset()
        
        return self.success_end_status()