# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusRound
#

from mandom.dungeon import Dungeon
from mandom.status.status_type import StatusType

from mandom.containers.tree_node import TreeNode
from mandom.containers.dynamic_tree_node import DynamicTreeNode

from mandom.status.status_turn import StatusTurn
from mandom.status.status_challenge import StatusChallenge 

class StatusRoundStart(TreeNode):
    def __init__(self):
        super().__init__(StatusType.round_start)

class StatusRoundNextTurn(DynamicTreeNode):
    def __init__(self, dungeon):
        condition_statement = lambda :dungeon.phase_round.has_next_turn()
        super().__init__(StatusType.round_next_turn, condition_statement)
        self.add_child(StatusTurn(dungeon))
        # self.add_child(StatusTurn(dungeon))
        # self.add_child(StatusTurn(dungeon))
        # self.add_child(StatusTurn(dungeon))

class StatusRoundChallenge(TreeNode):
    def __init__(self, dungeon):
        super().__init__(StatusType.round_challenge)
        self.add_child(StatusChallenge(dungeon))

class StatusRoundEnd(TreeNode):
    def __init__(self):
        super().__init__(StatusType.round_end)

class StatusRound(TreeNode):
    def __init__(self, dungeon):
        super().__init__(StatusType.round)
        self.add_child(StatusRoundStart())
        self.add_child(StatusRoundNextTurn(dungeon))
        self.add_child(StatusRoundChallenge(dungeon))
        self.add_child(StatusRoundEnd())