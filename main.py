# Salmonjoon
# DungeonOfMandom
# 2016.06.04
#
# Main
#

from mandom.dungeon import Dungeon
from mandom.dumy_dungeon import DumyDungeon
from mandom.dungeon_viewer import DungeonViewer
from mandom.dungeon_controller import DungeonController

from mandom.player import Player

player_names = ['salmonjoon', 'kein', 'sshong91', 'wool']

dungeon = Dungeon()
# dungeon = DumyDungeon()
for name in player_names:
    player = Player(name)    
    dungeon.phase_game.add_player(player)

dungeon_viewer     = DungeonViewer(dungeon)
dungeon_controller = DungeonController(dungeon)

dungeon_controller.game_start()
while dungeon_controller.game_running():
    dungeon_controller.update()
    # dungeon_viewer.update()
    dungeon_viewer.show()
    
    line = input()

print('gameover')
