# Salmonjoon
# DungeonOfMandom
# 2016.06.04
#
# DynamicTreeNode
#

from mandom.containers.tree_node import TreeNode


class DynamicTreeNode(TreeNode):
    def __init__(self, data, condition_statement):
        super().__init__(data)
        self.condition_statement = condition_statement

    def get_child(self, idx):
        if self.condition_statement():
            return super().get_child(0)
        else:
            return None
