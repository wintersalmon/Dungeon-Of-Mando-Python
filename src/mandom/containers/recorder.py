# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# Recorder
#


class Recorder(object):
    def __init__(self):
        self.events = []

    def size(self):
        return len(self.events)

    def at(self, idx):
        return self.events[idx]

    def insert(self, item):
        self.events.append(item)

    def remove(self, item):
        self.events.remove(item)
