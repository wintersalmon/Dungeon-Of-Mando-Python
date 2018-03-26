# Salmonjoon
# DungeonOfMandom
# 2016.06.04
#
# TreeNode
#


class TreeNode(object):
    def __init__(self, data):
        self.__data = data
        self.__children = list()

    def data(self):
        return self.__data

    def add_child(self, child):
        self.__children.append(child)

    def num_of_child(self):
        return len(self.__children)

    def get_child(self, idx):
        try:
            child = self.__children[idx]
        except IndexError:
            child = None
        return child
