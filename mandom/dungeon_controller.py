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
        self.current_status = None
        
    def game_start(self):
        self.status_controller.begin()
        self.current_status = None
    
    def game_running(self):
        return self.status_controller.has_next()
    
    def update(self):
        self.current_status = self.status_controller.next()
        print(self.current_status)
