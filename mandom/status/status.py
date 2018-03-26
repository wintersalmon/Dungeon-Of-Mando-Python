from mandom.containers.dynamic_tree_node import DynamicTreeNode
from mandom.containers.tree_node import TreeNode


class Status(TreeNode):
    def __init__(self, data):
        super().__init__(data)

    def execute(self, dungeon):
        raise NotImplementedError


class DynamicStatus(DynamicTreeNode):
    def __init__(self, data, condition_statement):
        super().__init__(data, condition_statement)

    def execute(self, dungeon):
        raise NotImplementedError
