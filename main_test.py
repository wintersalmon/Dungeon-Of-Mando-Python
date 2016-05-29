# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# test script for dungeon of mandom
#
'''

def test_containers():
    pass

def test_events():
    pass

def test_monsters():
    pass

def test_status():
    pass

def test_weapons():
    pass

def test_hero():
    pass
    
def test_player():
    pass
    
def test_status_manager():
    pass

def test_dungeon():
    pass

'''
from mandom.weapons.weapon_armor import WeaponArmor
from mandom.hero import Hero
def test_hero():
    h = Hero()
    print(h.armor())
    h.equipe_weapon([WeaponArmor()])
    print(h.armor())
    return True








from mandom.status.status_type import StatusType
def test_status_type():
    for status in StatusType:
        print(status)
    return True

def test_status_manager():
    pass







from mandom.dungeon import Dungeon, Player

def test_dungeon():
    dungeon = Dungeon()
    
    players = [ Player('kein'), Player('salmon'), Player('sshong'), Player('wool') ]
    
    for player in players:
        dungeon.game.add_player(player)
    
    print('### TEST GAME ###')
    game = dungeon.game
    
    test_print_items_with_title('players', game.player_list())
    test_print_items_with_title('monsters', game.monster_list())
    test_print_items_with_title('weapons', game.weapon_list())
    
    print('### TEST ROUND ###')
    round = dungeon.round
    round.reset()
    
    test_print_items_with_title('player_in_round', round.player_in_round)
    test_print_items_with_title('monster_in_deck', round.monster_in_deck)
    test_print_items_with_title('monster_in_dungeon', round.monster_in_dungeon)
    test_print_items_with_title('weapon_in_dungeon', round.weapon_in_dungeon)
    
    
    print('### TEST TURN ###')


    print('### TEST CHALLENGE ###')
    
    
    print('### TEST BATTLE ###')
    return True


def test_print_items_with_title(title,items):
    print('{}({}) : '.format(title,len(items)), end=' ')
    for item in items:
        print(item, end=' ')
    print('')



def test_cases(title, test_function, test_case):
    print('Test {} start'.format(title))
    for case, expected_result in test_cases:
        result = test_function(case)
        if result != expected_result:
            print('Case({}) Failed : result({}) but expected({})'.format(case, result, expected_result))
    print('Test {} end'.format(title))

def test(title, test_function):
    print('Test {} begin : '.format(title), end=' ')
    if test_function() == True:
        print('Complete !!!')
    else:
        print('Failed !!!')

if __name__ == "__main__":
    test('Dungeon', test_dungeon)
    test('Hero', test_hero)
    test('StatusType', test_status_type)
