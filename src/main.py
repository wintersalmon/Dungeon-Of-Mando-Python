# Salmonjoon
# DungeonOfMandom
# 2016.06.04
#
# Main
#

from mandom.dungeon import Dungeon
from mandom.dungeon_controller import DungeonController
from mandom.dungeon_viewer import DungeonViewer
from mandom.player import Player

player_names = ['salmonjoon', 'kein', 'sshong91', 'wool']

dungeon = Dungeon()
# dungeon = DumyDungeon()
for name in player_names:
    player = Player(name)
    dungeon.phase_game.add_player(player)

dungeon_viewer = DungeonViewer(dungeon)
dungeon_controller = DungeonController(dungeon)


def start():
    dungeon_controller.game_start()
    dungeon.phase_game.start()
    dungeon.phase_round.start()
    return True


def is_running():
    return dungeon_controller.game_running()


def update():
    # while dungeon_controller.last_status_execute_success:
    #    dungeon_controller.update()
    dungeon_controller.update()
    # print(dungeon_controller.get_last_event())
    return True


def num_of_player_in_game():
    return dungeon_viewer.num_of_player_in_game()


def get_player_life_point(player_num):
    return dungeon_viewer.get_player_life_point(player_num)


def get_player_victor_point(player_num):
    return dungeon_viewer.get_player_victor_point(player_num)


def get_player_name(player_num):
    return dungeon_viewer.get_player_name(player_num)


def get_current_turn_player_number():
    return dungeon_viewer.get_current_turn_player()


def num_of_monster_in_deck():
    return dungeon_viewer.num_of_monster_in_deck()


def num_of_monster_in_dungeon():
    return dungeon_viewer.num_of_monster_in_dungeon()


def num_of_weapon_in_dungeon():
    return dungeon_viewer.num_of_weapon_in_dungeon()


def top_monster_code_in_deck():
    return int(dungeon_viewer.top_monster_in_deck())


def top_monster_in_dungeon():
    return int(dungeon_viewer.top_monster_in_dungeon())


def hero_remaining_armor():
    return dungeon_viewer.hero_remaining_armor()


def get_draw_monster_name():
    return dungeon_viewer.get_draw_monster_name()


def get_battle_monster_name():
    return dungeon_viewer.get_battle_monster_name()


def has_player_passed(playerNumber):
    return dungeon_viewer.has_player_passed(playerNumber)


def is_players_turn(playerNumber):
    return dungeon_viewer.is_players_turn(playerNumber)


def action_turn_pass():
    return dungeon_controller.action_turn_pass()


def action_turn_monster_to_dungeon():
    return dungeon_controller.action_turn_monster_to_dungeon()


def action_turn_weapon_remove(weaponNumber):
    return dungeon_controller.action_turn_weapon_remove(weaponNumber)


def get_last_event():
    return dungeon_controller.get_last_event()


def get_event_count():
    return dungeon_controller.get_event_count()


def get_event(i):
    return dungeon_controller.get_event(i)


def has_weapon(num):
    return dungeon_viewer.has_weapon(num)


def is_status_turn_start():
    return dungeon_viewer.is_status_turn_start()


def is_status_battle_start():
    return dungeon_viewer.is_status_battle_start()


def is_status_battle_end():
    return dungeon_viewer.is_status_battle_end()


def get_battle_monster_damage():
    return dungeon_viewer.get_battle_monster_damage()


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
        print(dungeon.event_recorder[-1])
        show()
        if dungeon_controller.require_command_input_turn():
            line = input('command : ')
            if line == 'p':
                action_turn_pass()
            elif line == 'm':
                action_turn_monster_to_dungeon()
            elif line in '123456':
                weaponNumber = int(line)
                action_turn_weapon_remove(weaponNumber)
            update()
        # command()


######## debug
def test_debug():
    player_names = ['salmonjoon', 'kein', 'sshong91', 'wool']

    dungeon = Dungeon()
    # dungeon = DumyDungeon()
    for name in player_names:
        player = Player(name)
        dungeon.phase_game.add_player(player)

    dungeon_viewer = DungeonViewer(dungeon)
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


# test()
test_debug()
