# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# Recorder
#

class Recorder:
    def __init__(self):
        self.events = []

    def record_size(self):
        return len(self.events)

    def record_item_at(self, idx):
        return self.events[idx]

    def record_insert(self, item):
        self.events.append(item)
    
    def record_remove(self, item):
        self.events.remove(item)
    
