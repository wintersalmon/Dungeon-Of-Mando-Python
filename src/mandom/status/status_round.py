# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusRound
#

from mandom.status.status import Status, DynamicStatus
from mandom.status.status_challenge import StatusChallenge
from mandom.status.status_turn import StatusTurn
from mandom.status.status_type import StatusType


class StatusRoundStart(Status):
    def __init__(self):
        super().__init__(StatusType.round_start)

    def execute(self, dungeon):
        dungeon.phase_round.start()
        return True


class StatusRoundNextTurn(DynamicStatus):
    def __init__(self, dungeon):
        super().__init__(StatusType.round_next_turn, lambda: dungeon.phase_round.has_next_turn())
        self.add_child(StatusTurn())

    def execute(self, dungeon):
        return True


class StatusRoundChallenge(Status):
    def __init__(self, dungeon):
        super().__init__(StatusType.round_challenge)
        self.add_child(StatusChallenge(dungeon))

    def execute(self, dungeon):
        return True


class StatusRoundEnd(Status):
    def __init__(self):
        super().__init__(StatusType.round_end)

    def execute(self, dungeon):
        dungeon.phase_round.end()
        return True


class StatusRound(Status):
    def __init__(self, dungeon):
        super().__init__(StatusType.round_init)
        self.add_child(StatusRoundStart())
        self.add_child(StatusRoundNextTurn(dungeon))
        self.add_child(StatusRoundChallenge(dungeon))
        self.add_child(StatusRoundEnd())

    def execute(self, dungeon):
        return True
