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

class StatusTurnExecute(TreeNode):
    def __init__(self):
        super().__init__(StatusType.turn_execute)

class StatusTurnEnd(TreeNode):
    def __init__(self):
        super().__init__(StatusType.turn_end)
        
class StatusTurn(TreeNode):
    def __init__(self, dungeon):
        super().__init__(StatusType.turn)
        self.add_child(StatusTurnStart())
        self.add_child(StatusTurnExecute())
        self.add_child(StatusTurnEnd())

