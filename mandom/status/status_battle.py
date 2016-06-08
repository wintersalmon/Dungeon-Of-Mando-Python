# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusBattle
#

from mandom.dungeon import Dungeon
from mandom.status.status_type import StatusType

from mandom.containers.tree_node import TreeNode
from mandom.containers.dynamic_tree_node import DynamicTreeNode

class StatusBattleStart(TreeNode):
    def __init__(self):
        super().__init__(StatusType.battle_start)
        
    def execute(self, dungeon):
        dungeon.phase_battle.start()
        return True

class StatusBattleExecute(TreeNode):
    def __init__(self):
        super().__init__(StatusType.battle_execute)

    def execute(self, dungeon):
        dungeon.phase_battle.execute()
        return True

class StatusBattleEnd(TreeNode):
    def __init__(self):
        super().__init__(StatusType.battle_end)
        
    def execute(self, dungeon):
        dungeon.phase_battle.end()
        return True
        
class StatusBattle(TreeNode):
    def __init__(self):
        super().__init__(StatusType.battle_init)
        self.add_child(StatusBattleStart())
        self.add_child(StatusBattleExecute())
        self.add_child(StatusBattleEnd())

    def execute(self, dungeon):
        return True
