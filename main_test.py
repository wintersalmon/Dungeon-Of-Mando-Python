# Salmonjoon
# DungeonOfMandom
# 2016.06.13
#
# Main Test 
#

from mandom.mandom import Mandom
from mandom.mandom_controller import MandomController
from mandom.mandom_viewer import MandomViewer
def test_mandom_package_create():
    mandom = Mandom()
    controller = MandomController()
    viewer = MandomViewer()
    return True

if __name__ == "__main__":
    test_mandom_package_create()
    print('all test passed')





'''



import sys

class TestError(Exception):
    def __init__(self,value):
        self.value = value
    def __str__(self):
        return repr(self.value)
        

def print_error(prefix, msg):
    msg = '[{}] : {}'.format(prefix, msg)
    print(msg)


def test(title, test_function):
    print('Test {} begin'.format(title))
    result = 'completed' if test_function() else 'failed'
    print('Test {} {}'.format(title, result))





from mandom.weapons.weapon_armor import WeaponArmor
from mandom.hero import Hero
def test_hero():
    try:
        hero = Hero()
        if hero.armor() != 0:
            raise TestError('hero init failed')
        
        hero.equipe_weapon([WeaponArmor()])
        if hero.armor() != 8:
            raise TestError('hero equipe_weapon failed')
    except TestError as e:
        print_error('TestError', e)
        return False
    return True


from mandom.status.status_type import StatusType
def test_status_type():
    try:
        for status in StatusType:
            status
    except TestError as e:
        print_error('Error', e)
        return False
    return True

def test_status_manager():
    pass







from mandom.dungeon import Dungeon, Player
from mandom.status_manager import StatusManager

def test_dungeon():
    dungeon = Dungeon()
    
    players = [ Player('kein'), Player('salmon'), Player('sshong'), Player('wool') ]
    
    for player in players:
        dungeon.game.add_player(player)
    
    manager = StatusManager(dungeon)
    manager.start()
    
    while not manager.is_end():
        line = input('press something')
        manager.next()

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


if __name__ == "__main__":
    test('Dungeon', test_dungeon)
    # test('Hero', test_hero)
    # test('StatusType', test_status_type)
'''