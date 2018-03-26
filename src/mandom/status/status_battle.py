# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusBattle
#

from mandom.status.status import Status
from mandom.status.status_type import StatusType


class StatusBattleStart(Status):
    def __init__(self):
        super().__init__(StatusType.battle_start)

    def execute(self, dungeon):
        dungeon.phase_battle.start()
        return True


class StatusBattleExecute(Status):
    def __init__(self):
        super().__init__(StatusType.battle_execute)

    def execute(self, dungeon):
        dungeon.phase_battle.execute()
        return True


class StatusBattleEnd(Status):
    def __init__(self):
        super().__init__(StatusType.battle_end)

    def execute(self, dungeon):
        dungeon.phase_battle.end()
        monster = dungeon.phase_battle.battle_monster
        damage = dungeon.phase_battle.battle_damage
        result = 'win' if dungeon.phase_battle.battle_win else 'recieved {} damage'.format(damage)
        event = 'battle vs {} {}'.format(monster, result)
        dungeon.event_recorder.append(event)
        return True


class StatusBattle(Status):
    def __init__(self):
        super().__init__(StatusType.battle_init)
        self.add_child(StatusBattleStart())
        self.add_child(StatusBattleExecute())
        self.add_child(StatusBattleEnd())

    def execute(self, dungeon):
        return True
