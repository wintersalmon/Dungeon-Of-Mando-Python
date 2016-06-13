# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# 
#

# from mandom.dungeon import Dungeon
from mandom.dumy_dungeon import DumyDungeon
from mandom.dungeon_status_controller import DungeonStatusController

if __name__ == "__main__":
    print('START TEST')
    
    dungeon = DumyDungeon()
    
    status_controller = DungeonStatusController(dungeon)
    
    status_controller.begin()
    
    while status_controller.has_next():
        status = status_controller.next()
        print(status)
    
    print('END TEST')
    