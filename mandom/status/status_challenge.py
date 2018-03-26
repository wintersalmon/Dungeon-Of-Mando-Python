# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusChallenge
#

from mandom.status.status import Status, DynamicStatus
from mandom.status.status_battle import StatusBattle
from mandom.status.status_type import StatusType


class StatusChallengeStart(Status):
    def __init__(self):
        super().__init__(StatusType.challenge_start)

    def execute(self, dungeon):
        return dungeon.phase_challenge.start()


class StatusChallengeNextBattle(DynamicStatus):
    def __init__(self, dungeon):
        super().__init__(StatusType.challenge_next_battle, lambda: dungeon.phase_challenge.has_next_battle())
        self.add_child(StatusBattle())

    def execute(self, dungeon):
        return True


class StatusChallengeEnd(Status):
    def __init__(self):
        super().__init__(StatusType.challenge_end)

    def execute(self, dungeon):
        dungeon.phase_challenge.end()
        return True


class StatusChallenge(Status):
    def __init__(self, dungeon):
        super().__init__(StatusType.challenge_init)
        self.add_child(StatusChallengeStart())
        self.add_child(StatusChallengeNextBattle(dungeon))
        self.add_child(StatusChallengeEnd())

    def execute(self, dungeon):
        return True
