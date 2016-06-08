# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusChallenge
#

from mandom.dungeon import Dungeon
from mandom.status.status_type import StatusType

from mandom.containers.tree_node import TreeNode
from mandom.containers.dynamic_tree_node import DynamicTreeNode

from mandom.status.status_battle import StatusBattle

class StatusChallengeStart(TreeNode):
    def __init__(self):
        super().__init__(StatusType.challenge_start)
    def execute(self, dungeon):
        return dungeon.phase_challenge.start()


class StatusChallengeNextBattle(DynamicTreeNode):
    def __init__(self, dungeon):
        condition_statement = lambda :dungeon.phase_challenge.has_next_battle()
        super().__init__(StatusType.challenge_next_battle, condition_statement)
        self.add_child(StatusBattle())
        # self.add_child(StatusBattle())
        # self.add_child(StatusBattle())
        # self.add_child(StatusBattle())
    def execute(self, dungeon):
        return True

class StatusChallengeEnd(TreeNode):
    def __init__(self):
        super().__init__(StatusType.challenge_end)
    def execute(self, dungeon):
        dungeon.phase_challenge.end()
        return True
        
class StatusChallenge(TreeNode):
    def __init__(self, dungeon):
        super().__init__(StatusType.challenge_init)
        self.add_child(StatusChallengeStart())
        self.add_child(StatusChallengeNextBattle(dungeon))
        self.add_child(StatusChallengeEnd())
    def execute(self, dungeon):
        return True

