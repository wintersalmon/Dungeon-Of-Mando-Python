# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# player

import monster
import weapon

class Player:
    def __init__(self,name):
        self.__name = name
        self.__victory_point = 0
        self.__life_point = 2
        self.__removed_weapons  = []
        self.__removed_monsters = []
        
    def __str__(self):
        return self.__name
    
    def name(self):
        return self.__name

    def victory_point(self):
        return self.__victory_point

    def life_point(self):
        return self.__life_point

    def gain_victory_point(self):
        self.__victory_point += 1
        return self.__victory_point

    def lose_life_point(self):
        self.__life_point -= 1
        if self.__life_point < 0:
            self.__life_point = 0
        return self.__life_point
    
    def reset_round(self):
        self.__removed_weapons.clear()
        self.__removed_monsters.clear()

    def add_removed_weapon(self,weapon):
        self.__removed_weapons.append(weapon)
        
    def add_removed_monster(self,monster):
        self.__removed_monsters.append(monster)

    def make_display_msg(self,content):
        msg = '[{0}] {1} ? '.format(self, content)
        return msg

    def make_display_option_msg(self,title,options):
        msg = self.make_display_msg(title)
        if isinstance(options,str):
            msg += '('
            msg += options
            msg += ')'
        elif isinstance(options,list):
            for idx in range(0,len(options)):
                msg += '[{0}]{1} '.format(idx,options[idx])
        msg += ' : '
        return msg

    def ask_pass(self):
        options = ['yes', 'no']
        response = input(self.make_display_option_msg('Pass Turn', options))

        try:
            response_number = int(response)
        except:
            print(self.make_display_msg('ERROR', 'Input Not Integer'))
            response_number = 0
        
        if 0 <= response_number < len(options):
            if response_number == 0:
                return True
        return False

    def ask_stack_monster_to_dungeon(self,monster):
        options = ['Yes', 'No']
        msg = 'Add Monster({}) To Dungeon'.format(monster)
        response = input(self.make_display_option_msg(msg, options))

        try:
            response_number = int(response)
        except:
            print(self.make_display_msg('ERROR', 'Input Not Integer'))
            response_number = 0
        
        if 0 <= response_number < len(options):
            if response_number == 0:
                return True
        return False

    def ask_weapon_to_remove(self,weapon_list):
        response = input(self.make_display_option_msg('Select a Weapon To Remove',weapon_list))
        try:
            response_number = int(response)
        except:
            print(self.make_display_msg('ERROR', 'User Input Not Integer'))
            response_number = 0
        return response_number

        # response = input(self.make_display_option_msg('Select a Weapon To Remove',weapon_list))
        # try:
        #     response_number = int(response)
        # except:
        #     print(self.make_display_msg('ERROR', 'User Input Not Integer'))
        #     response_number = 0

        # if 0 <= response_number < len(weapon_list):
        #     return weapon_list[response_number]
        # else:
        #     return None
        
    def ask_hero_sword_target_monster_name(self):
        response = input(self.make_display_option_msg('Select a Monster to target with HeroSword', monsters.ACTUAL_MONSTER_NAME_LIST))

        try:
            response_number = int(response)
        except:
            print(self.make_display_msg('ERROR', 'User Input Not Integer'))
            response_number = 0

        if 0 <= response_number < len(monsters.ACTUAL_MONSTER_NAME_LIST):
            return monsters.ACTUAL_MONSTER_NAME_LIST[response_number]
        else:
            return None
    
    def show_current_draw_monster(self,monster):
        print(self.make_display_option_msg(monster.name(), 'No Options'))
