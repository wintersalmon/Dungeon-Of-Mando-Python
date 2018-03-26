# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# DungeonStatusController
#

from mandom.status.status_game import StatusGame


class DungeonStatusController(object):
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.start_status = StatusGame(dungeon)

        self.saved_parent_status = list()
        self.current_status = None
        self.current_child_idx = 0

    def begin(self):
        self.saved_parent_status.clear()
        self.current_status = self.start_status
        self.current_child_idx = -1

    def has_next(self):
        if self.current_status != None:
            return True
        else:
            return False

    def next(self):
        if self.current_child_idx == -1:
            self.current_child_idx += 1
            return self.current_status
        elif self.MoveToChild():
            return self.next()
        elif self.MoveToParent():
            return self.next()
        else:
            self.current_status = None
            return None

    def MoveToChild(self):
        child = self.current_status.get_child(self.current_child_idx)
        if child == None:
            return False
        else:
            parent = (self.current_child_idx + 1, self.current_status)
            self.saved_parent_status.append(parent)
            self.current_child_idx = -1
            self.current_status = child
            return True

    def MoveToParent(self):
        if len(self.saved_parent_status) == 0:
            return False
        else:
            parent = self.saved_parent_status.pop(-1)
            self.current_child_idx = parent[0]
            self.current_status = parent[1]
            return True
