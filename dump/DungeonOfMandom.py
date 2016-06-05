# Salmonjoon
# DungeonOfMandom
# 2016.05.19

from dungeon import Dungeon
from controller import DungeonController
from viewer import DungeonViewer
from status_for_dungeon import STATUS, START_STATUS_CODE, END_STATUS_CODE
from player import Player



game = Dungeon()
controller = DungeonController(game)
viewer = DungeonViewer(game)
player_names = set(['Salmon', 'Kein', 'Sshong', 'Wool'])

for name in player_names:
    player = Player(name)
    game.connect_player(player)

while controller.running():
    controller.update()
    viewer.show()

print('##### END MAIN #####')

