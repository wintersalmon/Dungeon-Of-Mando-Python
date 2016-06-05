# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# StatusGame
#

from mandom.dungeon import Dungeon
from mandom.status.status_type import StatusType

from mandom.containers.tree_node import TreeNode
from mandom.containers.dynamic_tree_node import DynamicTreeNode


from mandom.status.status_round import StatusRound

# Status Game
class StatusGameStart(TreeNode):
    def __init__(self):
        super().__init__(StatusType.game_start)

class StatusGameNextRound(DynamicTreeNode):
    def __init__(self, dungeon):
        condition_statement = lambda :dungeon.phase_game.has_next_round()
        super().__init__(StatusType.game_next_round, condition_statement)
        self.add_child(StatusRound(dungeon))
        # self.add_child(StatusRound(dungeon))
        # self.add_child(StatusRound(dungeon))
        # self.add_child(StatusRound(dungeon))
    
class StatusGameEnd(TreeNode):
    def __init__(self):
        super().__init__(StatusType.game_end)
        
class StatusGame(TreeNode):
    def __init__(self, dungeon):
        super().__init__(StatusType.game)
        self.add_child(StatusGameStart())
        self.add_child(StatusGameNextRound(dungeon))
        self.add_child(StatusGameEnd())

