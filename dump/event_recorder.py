# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# EventRecorder

class EventRecorder:
    def __init__(self):
        self.events = []

    def event_list_size(self):
        return len(self.events)

    def event_at(self,index):
        return self.events[index]

    def event_insert(self,event):
        self.events.append(event)
    
