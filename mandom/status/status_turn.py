# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusTurn
#

from mandom.dungeon import Dungeon
from mandom.status.status_type import StatusType

from mandom.containers.tree_node import TreeNode
from mandom.containers.dynamic_tree_node import DynamicTreeNode

class StatusTurnStart(TreeNode):
    def __init__(self):
        super().__init__(StatusType.turn_start)
    def execute(self, dungeon):
        dungeon.phase_turn.start()
        return True

class StatusTurnExecute(TreeNode):
    def __init__(self):
        super().__init__(StatusType.turn_execute)
    def execute(self, dungeon):
        return dungeon.phase_turn.execute()

class StatusTurnEnd(TreeNode):
    def __init__(self):
        super().__init__(StatusType.turn_end)
    def execute(self, dungeon):
        dungeon.phase_turn.end()
        return True
        
class StatusTurn(TreeNode):
    def __init__(self, dungeon):
        super().__init__(StatusType.turn_init)
        self.add_child(StatusTurnStart())
        self.add_child(StatusTurnExecute())
        self.add_child(StatusTurnEnd())
    def execute(self, dungeon):
        return True

