# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# DungeonController
#

from mandom.dungeon import Dungeon
from mandom.dungeon_status_controller import DungeonStatusController

class DungeonController():
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.status_controller = DungeonStatusController(self.dungeon)
    def start_game(self):
        pass
    
    def has_next_event(self):
        return False
        
    def next_event(self):
        return None