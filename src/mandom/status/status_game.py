# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusGame
#

from mandom.status.status import DynamicStatus, Status
from mandom.status.status_round import StatusRound
from mandom.status.status_type import StatusType


# Status Game
class StatusGameStart(Status):
    def __init__(self):
        super().__init__(StatusType.game_start)

    def execute(self, dungeon):
        dungeon.phase_game.start()
        return True


class StatusGameNextRound(DynamicStatus):
    def __init__(self, dungeon):
        super().__init__(StatusType.game_next_round, lambda: dungeon.phase_game.has_next_round())
        self.add_child(StatusRound(dungeon))

    def execute(self, dungeon):
        return True


class StatusGameEnd(Status):
    def __init__(self):
        super().__init__(StatusType.game_end)

    def execute(self, dungeon):
        dungeon.phase_game.end()
        return True


class StatusGame(Status):
    def __init__(self, dungeon):
        super().__init__(StatusType.game_init)
        self.add_child(StatusGameStart())
        self.add_child(StatusGameNextRound(dungeon))
        self.add_child(StatusGameEnd())

    def execute(self, dungeon):
        return True
