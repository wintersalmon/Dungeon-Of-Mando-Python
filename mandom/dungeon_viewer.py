# Salmonjoon
# DungeonOfMandom
# 2016.06.05
#
# DungeonViewer
#

from mandom.dungeon import Dungeon

class DungeonViewer():
    def __init__(self, dungeon):
        self.dungeon = dungeon
    
    # def update(self):
    #     print('update DungeonViewer')
    
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
        print('Dungeon Game')

        self.dungeon.phase_game.start()
        
        players_in_game = self.dungeon.phase_game.player_list()
        print(self.show_players('players_in_game', players_in_game))


    def show_phase_round(self):
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
        
        
        
        
    def show(self):
        self.show_phase_game()
        
        
        self.dungeon.phase_round.start()
        self.show_phase_round()
        
        
        self.dungeon.phase_turn.start()
        self.show_phase_turn()
        
        
        self.dungeon.phase_challenge.start()
        self.show_phase_challenge()
        
        
        self.dungeon.phase_battle.start()
        self.show_phase_battle()

        
        

        