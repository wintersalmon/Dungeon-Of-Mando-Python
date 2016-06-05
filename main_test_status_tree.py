# Salmonjoon
# DungeonOfMandom
# 2016.06.04
#
# Test script
#

# from mandom.dungeon import Dungeon
from mandom.dumy_dungeon import DumyDungeon
from mandom.status.status_game import StatusGame

def print_all_node_preorder(node):
    if node == None:
        return False
    
    print(node.data())
    idx = 0
    while print_all_node_preorder(node.get_child(idx)):
        idx += 1
        if idx > 1000:
            raise IndexRangeError
    return True

if __name__ == "__main__":
    print('START TEST')
    
    dungeon = DumyDungeon()
    
    status = StatusGame(dungeon)
    
    print_all_node_preorder(status)
    
    print('END TEST')
    