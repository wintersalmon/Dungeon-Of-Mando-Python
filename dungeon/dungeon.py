# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# dungeon
#

from monster  import GoblinMonster, SkeletonWarriorMonster, OrkMonster, VampireMonster, GolamMonster, ReaperMonster, SatanMonster, DragonMonster
from weapon   import TorchWeapon, HolyGrailWeapon, SpearWeapon, ArmorWeapon, ShieldWeapon, HeroSwordWeapon
from hero     import Hero
from player   import Player
from recorder import Recorder


class Dungeon():
    def __init__(self):
        self.game  = DungeonGameData()
        self.round = DungeonRoundData(self.game)
        self.turn  = DungeonTurnData(self.round)
        self.challenge = DungeonChallengeData(self.round)
        self.battle    = DungeonBattleData(self.challenge)

        
class DungeonGameData():
    def __init__(self):
        self.__monster_in_game = list()
        self.__weapon_in_game  = list()
        self.__player_in_game  = list()
        
        # init __monster_in_game
        self.__monster_in_game.append(GoblinMonster())
        self.__monster_in_game.append(GoblinMonster())
        self.__monster_in_game.append(SkeletonWarriorMonster())
        self.__monster_in_game.append(SkeletonWarriorMonster())
        self.__monster_in_game.append(OrkMonster())
        self.__monster_in_game.append(OrkMonster())
        self.__monster_in_game.append(VampireMonster())
        self.__monster_in_game.append(VampireMonster())
        self.__monster_in_game.append(GolamMonster())
        self.__monster_in_game.append(GolamMonster())
        self.__monster_in_game.append(ReaperMonster())
        self.__monster_in_game.append(SatanMonster())
        self.__monster_in_game.append(DragonMonster())
        
        # init __weapon_in_game
        self.__weapon_in_game.append(TorchWeapon())
        self.__weapon_in_game.append(HolyGrailWeapon())
        self.__weapon_in_game.append(SpearWeapon())
        self.__weapon_in_game.append(ArmorWeapon())
        self.__weapon_in_game.append(ShieldWeapon())
        self.__weapon_in_game.append(HeroSwordWeapon())
        

    def monster_list(self):
        return self.__monster_in_game

    def weapon_list(self):
        return self.__weapon_in_game
    
    def player_list(self):
        return self.__player_in_game
    
    def monster(self,idx):
        if idx in range(len(self.__monster_in_game)):
            return self.__monster_in_game[idx]
        return None
        
    def weapon(self,idx):
        if idx in range(len(self.__weapon_in_game)):
            return self.__weapon_in_game[idx]
        return None
    
    def player(self,idx):
        if idx in range(len(self.__player_in_game)):
            return self.__player_in_game[idx]
        return None
    
    
    def number_of_monsters(self):
        return len(self.__monster_in_game)
    
    def number_of_weapons(self):
        return len(self.__weapon_in_game)
        
    def number_of_players(self):
        return len(self.__player_in_game)
        
        
    def clone_monster_list(self):
        return self.__monster_in_game.copy()
    
    def clone_weapon_list(self):
        return self.__weapon_in_game.copy()
        
    def clone_player_list(self):
        return self.__player_in_game.copy()
    
    
    def add_player(self,player):
        self.__player_in_game.append(player)
    
    def remove_player(self,player):
        self.__player_in_game.remove(player)
        

        
class DungeonRoundData():
    def __init__(self, dungeon_game_data):
        self.__dungeon_game_data  = dungeon_game_data
        
        self.player_in_round    = list()
        self.monster_in_deck    = list()
        self.monster_in_dungeon = list()
        self.weapon_in_dungeon  = list()
    
    def reset(self):
        self.monster_in_deck    = self.__dungeon_game_data.clone_monster_list()
        self.monster_in_dungeon = list()
        self.weapon_in_dungeon  = self.__dungeon_game_data.clone_weapon_list()
        self.player_in_round    = self.__dungeon_game_data.clone_player_list()

    
class DungeonTurnData():
    def __init__(self, dungeon_round_data):
        # self.dungeon_round_data = dungeon_round_data
        self.monster_in_deck     = dungeon_round_data.monster_in_deck
        self.monster_in_dungeon  = dungeon_round_data.monster_in_dungeon
        self.weapon_in_dungeon   = dungeon_round_data.weapon_in_dungeon
        self.player_in_round     = dungeon_round_data.player_in_round
        
        self.turn_action = None
        self.turn_player = None
        self.turn_draw_monster  = None
        self.turn_remove_weapon = None

    def reset(self):
        self.turn_action = None
        self.turn_player = self.player_in_round[0] if self.player_in_round else None
        self.turn_draw_monster = self.monster_in_deck[-1] if self.monster_in_deck else None
        self.turn_remove_weapon = None
    

class DungeonChallengeData():
    def __init__(self, dungeon_round_data):
        self.monster_in_dungeon  = dungeon_round_data.monster_in_dungeon
        self.weapon_in_dungeon   = dungeon_round_data.weapon_in_dungeon
        self.player_in_round     = dungeon_round_data.player_in_round
        
        self.challenge_player = None
        self.challenge_hero = Hero()

    def reset(self):
        self.challenge_player = self.player_in_round[0] if self.player_in_round else None
        self.challenge_hero.equipe_weapon(self.weapon_in_dungeon)
        

class DungeonBattleData():
    def __init__(self, dungeon_challenge_data):
        self.dungeon_challenge_data = dungeon_challenge_data
        self.monster_in_dungeon = dungeon_challenge_data.monster_in_dungeon
        self.weapon_in_dungeon  = dungeon_challenge_data.weapon_in_dungeon
        self.challenge_player   = dungeon_challenge_data.challenge_player
        self.challenge_hero     = dungeon_challenge_data.challenge_hero
        
        self.battle_monster = None
        # self.battle_damage  = 0
        
    def reset(self):
        self.battle_monster = self.monster_in_dungeon[-1] if self.monster_in_dungeon else None
        # self.battle_damage  = self.battle_monster.damage() if self.battle_monster else 0


def test_print_items_with_title(title,items):
    print('{}({}) : '.format(title,len(items)), end=' ')
    for item in items:
        print(item, end=' ')
    print('')

def test_script():
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
if __name__ == "__main__":
    test_script()