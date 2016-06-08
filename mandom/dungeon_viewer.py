# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# DungeonViewer
#

from mandom.dungeon import Dungeon
from mandom.status.status_type import StatusType
from mandom.monsters.monster_type import MonsterType

class DungeonViewer():
    def __init__(self, dungeon):
        self.dungeon = dungeon
    
    # def update(self):
    #     print('update DungeonViewer')
    
    def num_of_player_in_game(self):
        try:
            num = len(self.dungeon.phase_game.player_list() )
        except:
            num = -1
        return num
    
    def get_player_life_point(self,player_num):
        try:
            life_point = self.dungeon.phase_game.player_list()[player_num].life_point()
        except:
            life_point = -1
        return life_point

    def get_player_victor_point(self,player_num):
        try:
            victory_point = self.dungeon.phase_game.player_list()[player_num].victory_point()
        except:
            victory_point = -1
        return victory_point
    
    def get_player_name(self,player_num):
        try:
            player_name = self.dungeon.phase_game.player_list()[player_num].name()
        except:
            player_name = 'error_name'
        return player_name
        
    def get_current_turn_player(self):
        num = -1
        try:
            turn_player = self.dungeon.phase_turn.turn_player
            for i, player in enumerate(self.dungeon.phase_game.player_list()):
                if player == turn_player:
                    num = i
        except:
            num = -2
        return num
    
    def num_of_monster_in_deck(self):
        try:
            num = len(self.dungeon.phase_round.monster_in_deck)
        except:
            num = -1
        return num

    def num_of_monster_in_dungeon(self):
        try:
            num = len(self.dungeon.phase_round.monster_in_dungeon)
        except:
            num = -1
        return num
        
    def num_of_weapon_in_dungeon(self):
        try:
            num = len(self.dungeon.phase_round.weapon_in_dungeon)
        except:
            num = -1
        return num
        
        
    def top_monster_in_deck(self):
        try:
            monster_code = self.dungeon.phase_round.monster_in_deck[-1].code()
        except:
            monster_code = -1
        return monster_code
        
    def top_monster_in_dungeon(self):
        try:
            monster_code = self.dungeon.phase_round.monster_in_dungeon[-1].code()
        except:
            monster_code = -1
        return monster_code
        
    def hero_remaining_armor(self):
        try:
            armor = self.dungeon.phase_challenge.challenge_hero.armor()
        except:
            armor = -1
        return armor
        
        
    def get_draw_monster_name(self):
        try:
            monster = self.dungeon.phase_round.monster_in_deck[-1]
        except:
            monster = None
        return monster.name() if monster else 'no_monster'

    def get_battle_monster_name(self):
        try:
            monster = self.dungeon.phase_round.monster_in_dungeon[-1]
        except:
            monster = None
        return monster.name() if monster else 'no_monster'
        
        
    def has_player_passed(self, playerNumber):
        player = self.dungeon.phase_game.player_list()[playerNumber]
        if player in self.dungeon.phase_round.player_in_round:
            return False
        else:
            return True
        
    def is_players_turn(self, playerNumber):
        try:
            player = self.dungeon.phase_game.player_list()[player_num]
            if player == self.dungeon.phase_turn.turn_player:
                return True
        except:
            return False

    
    def has_weapon(self, weaponNumber):
        try:
            weapon = self.dungeon.phase_game.weapon_list()[weaponNumber]
        except:
            weapon = None
        if weapon in self.dungeon.phase_round.weapon_in_dungeon:
            return True
        else:
            return False
    
    
    def is_status_turn(self):
        try:
            code = self.dungeon.current_status_code
            if code == StatusType.turn_init:
                return True
            if code == StatusType.turn_start:
                return True
            if code == StatusType.turn_end:
                return True
            if code == StatusType.turn_execute:
                return True
        except:
            return False
        return False
    
    def show(self):
        print('hi', self.num_of_player_in_game())
        for i in range(self.num_of_player_in_game()):
            name = self.get_player_name(i)
            life = self.get_player_life_point(i)
            vp   = self.get_player_victor_point(i)
            msg = '[{}({},{})]'.format(name, life, vp)
            if self.get_current_turn_player() == i:
                msg = '*' + msg
            if not self.has_player_passed(i):
                msg += 'V'
            print(msg)
            
        deck_size = self.num_of_monster_in_deck()
        dungeon_size = self.num_of_monster_in_dungeon()
        weapon_size = self.num_of_weapon_in_dungeon()
        msg2 = '{} / {} [{}]'.format(deck_size, dungeon_size, weapon_size)
        print(msg2)
        
        draw_deck = self.top_monster_in_deck()
        msg3 = 'top deck : {}'.format(draw_deck)
        print(msg3)
        
        
        draw_dungeon = self.top_monster_in_dungeon()
        msg_dungeon = 'top dungeon : {}'.format(draw_dungeon)
        print(msg_dungeon)













    def show_all(self):
        status_code = self.dungeon.current_status_code
        print(status_code)
        
        if status_code == StatusType.game_start:
            self.show_phase_game()
        
        if status_code == StatusType.round_start:
            self.show_phase_round()
        
        
        if status_code == StatusType.turn_start:
            self.show_phase_turn()
        
        
        if status_code == StatusType.challenge_start:
            self.show_phase_challenge()
        
        
        if status_code == StatusType.battle_start:
            self.show_phase_battle()
            
    def show_debug(self):
        status_code = self.dungeon.current_status_code
        
        print(status_code)
        
        self.show_phase_game()
    
        self.show_phase_round()
    
        self.show_phase_turn()
    
        self.show_phase_challenge()
    
        self.show_phase_battle()
        
        
        
    def apply_format_to_items(self,format_applier, items):
        formated_items = list()
        for item in items:
            formated_items.append(format_applier(item))
        return formated_items
    
    def display_list_with_format(self, title, items, item_foramter):
        formated_title = '{} in {}'
        formated_items = self.apply_format_to_items(item_foramter, items)
        
        result  = formated_title.format(len(items), title)
        result += '\n'
        result += '\n'.join(formated_items)
        result += '\n'
        
        return result    
    
    
    def show_players(self,title,players):
        return self.display_list_with_format(title,players,self.player_format_applier)
    
    def player_format_applier(self,player):
        fmt = '(L:{},V:{}){}'
        return fmt.format(player.life_point(), player.victory_point(), player.name())

        
        
    def show_monsters(self,title,monsters):
        return self.display_list_with_format(title,monsters,self.monster_format_applier)
        
    def monster_format_applier(self,monster):
        fmt = '({}){}'
        return fmt.format(monster.damage(), monster.name())
        
        
        
    def show_weapons(self,title,weapons):
        return self.display_list_with_format(title,weapons,self.weapon_format_applier)
                
    def weapon_format_applier(self, weapon):
        type_armor_fmt = '{}({})'
        type_weapon_fmt = '{}'
        
        if weapon.armor() > 0:
            return type_armor_fmt.format(weapon.name(), weapon.armor())
        else:
            return type_weapon_fmt.format(weapon.name())

    
    
    
    
    def show_phase_game(self):
        game_status = [StatusType.game_init, StatusType.game_start, StatusType.game_next_round, StatusType.game_end]
        if self.dungeon.current_status_code not in game_status:
            return
        print('Dungeon Game')

        self.dungeon.phase_game.start()
        
        players_in_game = self.dungeon.phase_game.player_list()
        print(self.show_players('players_in_game', players_in_game))


    def show_phase_round(self):
        round_status = [StatusType.round_init, StatusType.round_start, StatusType.round_next_turn, StatusType.round_challenge, StatusType.round_end]
        if self.dungeon.current_status_code not in round_status:
            return
        print('Dungeon Round')

        player_in_round = self.dungeon.phase_round.player_in_round
        print(self.show_players('player_in_round', player_in_round))

        monster_in_deck = self.dungeon.phase_round.monster_in_deck
        print(self.show_monsters('monster_in_deck', monster_in_deck))
        
        monster_in_dungeon = self.dungeon.phase_round.monster_in_dungeon
        print(self.show_monsters('monster_in_dungeon',monster_in_dungeon))
        
        weapon_in_dungeon = self.dungeon.phase_round.weapon_in_dungeon
        print(self.show_weapons('weapon_in_dungeon', weapon_in_dungeon))
        
        last_challenger = self.dungeon.phase_round.last_challenger
        fmt_last_challenger = 'last_challenger : {}\n'.format(last_challenger)
        print(fmt_last_challenger)
        
        
    def show_phase_turn(self):
        turn_status = [StatusType.turn_init, StatusType.turn_start, StatusType.turn_execute, StatusType.turn_end]
        if self.dungeon.current_status_code not in turn_status:
            return
        print('Dungeon Turn')
        fmt = '{} : {}'
        
        player_in_round = self.dungeon.phase_turn.player_in_round
        print(self.show_players('player_in_round', player_in_round))

        monster_in_deck = self.dungeon.phase_turn.monster_in_deck
        print(self.show_monsters('monster_in_deck', monster_in_deck))
        
        monster_in_dungeon = self.dungeon.phase_turn.monster_in_dungeon
        print(self.show_monsters('monster_in_dungeon',monster_in_dungeon))
        
        weapon_in_dungeon = self.dungeon.phase_turn.weapon_in_dungeon
        print(self.show_weapons('weapon_in_dungeon', weapon_in_dungeon))
        
        
        turn_action = self.dungeon.phase_turn.turn_action
        print(fmt.format('turn_action', turn_action))
        
        turn_player = self.dungeon.phase_turn.turn_player
        print(fmt.format('turn_player', turn_player))
        
        turn_draw_monster = self.dungeon.phase_turn.turn_draw_monster
        print(fmt.format('turn_draw_monster', turn_draw_monster))
        
        turn_remove_weapon = self.dungeon.phase_turn.turn_remove_weapon
        print(fmt.format('turn_remove_weapon', turn_remove_weapon))
        
        print()
        
        
    def show_phase_challenge(self):
        challenge_status = [StatusType.challenge_init, StatusType.challenge_start, StatusType.challenge_next_battle, StatusType.challenge_end]
        if self.dungeon.current_status_code not in challenge_status:
            return
        print('Dungeon Challenge')
        fmt = '{} : {}'

        player_in_round = self.dungeon.phase_challenge.player_in_round
        print(self.show_players('player_in_round', player_in_round))
        
        monster_in_dungeon = self.dungeon.phase_challenge.monster_in_dungeon
        print(self.show_monsters('monster_in_dungeon',monster_in_dungeon))
        
        weapon_in_dungeon = self.dungeon.phase_challenge.weapon_in_dungeon
        print(self.show_weapons('weapon_in_dungeon', weapon_in_dungeon))
        
        challenge_player = self.dungeon.phase_challenge.challenge_player
        print(fmt.format('challenge_player', challenge_player))
        
        challenge_hero = self.dungeon.phase_challenge.challenge_hero
        print(fmt.format('challenge_hero_armor', challenge_hero.armor()))
        
        print()
        
    def show_phase_battle(self):
        battle_status = [StatusType.battle_init, StatusType.battle_start, StatusType.battle_execute, StatusType.battle_end]
        if self.dungeon.current_status_code not in battle_status:
            return
        print('Dungeon Battle')
        fmt = '{} : {}'

        monster_in_dungeon = self.dungeon.phase_battle.monster_in_dungeon
        print(self.show_monsters('monster_in_dungeon',monster_in_dungeon))
        
        weapon_in_dungeon = self.dungeon.phase_battle.weapon_in_dungeon
        print(self.show_weapons('weapon_in_dungeon', weapon_in_dungeon))
        
        challenge_player = self.dungeon.phase_battle.challenge_player
        print(fmt.format('challenge_player', challenge_player))
        
        challenge_hero = self.dungeon.phase_battle.challenge_hero
        print(fmt.format('challenge_hero_armor', challenge_hero.armor()))
        
        battle_monster = self.dungeon.phase_battle.battle_monster
        print(fmt.format('battle_monster', battle_monster.name() if battle_monster else 'no monster'))
        print(fmt.format('battle_monster_damage', battle_monster.damage() if battle_monster else 'no damage'))
        
        battle_win = self.dungeon.phase_battle.battle_win
        print(fmt.format('battle_win', battle_win))
                