# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusTurn
#


from mandom.status.status_type import StatusType
from mandom.status.status import Status


class StatusTurnStart(Status):
    def __init__(self):
        super().__init__(StatusType.turn_start)

    def execute(self, dungeon):
        dungeon.phase_turn.start()
        return True


class StatusTurnExecute(Status):
    def __init__(self):
        super().__init__(StatusType.turn_execute)

    def execute(self, dungeon):
        return dungeon.phase_turn.execute()


class StatusTurnEnd(Status):
    def __init__(self):
        super().__init__(StatusType.turn_end)

    def execute(self, dungeon):
        dungeon.phase_turn.end()
        return True


class StatusTurn(Status):
    def __init__(self):
        super().__init__(StatusType.turn_init)
        self.add_child(StatusTurnStart())
        self.add_child(StatusTurnExecute())
        self.add_child(StatusTurnEnd())

    def execute(self, dungeon):
        return True
