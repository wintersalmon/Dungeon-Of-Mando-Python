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

def start():
    dungeon_controller.game_start()
    return True


def is_running():
    return dungeon_controller.game_running()

def update():
    while dungeon_controller.last_status_execute_success:
        dungeon_controller.update()
    return True

        
def show():
    dungeon_viewer.show()
    return True

def command():
    dungeon_controller.update_command()
    dungeon_controller.update()
    return True



def test():
    start()
    while is_running():
        update()
        show()
        command()
    
test()





######## debug
def test_debug():
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
        while dungeon_controller.last_status_execute_success:
            if not dungeon_controller.game_running():
                print('gameover')
                exit(0)
            dungeon_viewer.show()
            dungeon_controller.update()
        dungeon_viewer.show()
        dungeon_controller.update_command()
        dungeon_controller.update()


    print('gameover')




    
