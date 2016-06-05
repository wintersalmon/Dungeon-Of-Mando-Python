# Salmonjoon
# DungeonOfMandom
# 2016.06.04
#
# Main
#

from mandom.dungeon import Dungeon
from mandom.dungeon_controller import DungeonController

dungeon = Dungeon()
dungeon_controller = DungeonController(dungeon)

dungeon_controller.start_game()

while True:
    if dungeon_controller.has_next_event():
        next_event = dungeon_controller.next_event()
        dungeon.update(event)
    line = input('continue? (y|n)')
    if line != 'y':
        break

print('gameover')