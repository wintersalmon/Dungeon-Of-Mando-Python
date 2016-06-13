# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# DungeonController
#
from mandom.status.status_type import StatusType

from mandom.dungeon import Dungeon
from mandom.dungeon_status_controller import DungeonStatusController
from mandom.monsters.monster_type import MonsterType

class DungeonController():
    def __init__(self, dungeon):
        self.dungeon = dungeon
        self.status_controller = DungeonStatusController(self.dungeon)
        self.current_status = None
        self.last_status_execute_success = False
        #self.event_recorder = list()
        
    def game_start(self):
        self.status_controller.begin()
        self.current_status = None
        self.last_status_execute_success = True
    
    def game_running(self):
        return self.status_controller.has_next()
    
    def update(self):
        if self.last_status_execute_success:
            prev_status = self.current_status.data().name if self.current_status else 'no_type'
            self.current_status = self.status_controller.next()
            changed_status = self.current_status.data().name if self.current_status else 'no_type'
            self.dungeon.change_status_code(self.current_status.data())
            event = 'from {} to {}'.format(prev_status, changed_status)
            self.dungeon.event_recorder.append(event)
        self.last_status_execute_success = self.current_status.execute(self.dungeon)
    
    def get_last_event(self):
        try:
            event = dungeon.event_recorder[-1]
        except:
            return 'error_no_event'
        return event
    
    def action_turn_pass(self):
        self.dungeon.phase_turn.turn_action = 0
        self.update()
        return True
        
    def action_turn_monster_to_dungeon(self):
        self.dungeon.phase_turn.turn_action = 1
        self.update()
        return True
        
    def action_turn_weapon_remove(self, weaponNumber):
        try:
            weapon = self.dungeon.phase_game.weapon_list()[weaponNumber]
        except:
            weapon = None
        if weapon:
            self.dungeon.phase_turn.turn_remove_weapon = weapon
            self.dungeon.phase_turn.turn_action = 2
            self.update()
            return True
        return False
        
    
    def get_event_count(self):
        try:
            return len(self.dungeon.event_recorder)
        except:
            return 0


    def get_event(self,i):
        try:
            return self.dungeon.event_recorder[i]
        except:
            return 'index_error'

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def update_command(self):
        if self.require_command_input_turn():
            self.command_input_turn()  
        elif self.require_command_input_challenge():
            self.command_input_challenge()
        
        
        
        
    def require_command_input_turn(self):
        if self.current_status.data() == StatusType.turn_execute:
            return True
        else:
            return False
    
    def command_input_turn(self):
        if self.command_ask_player_pass():
            return
        if self.command_ask_player_monster_add():
            return
        if self.command_ask_player_weapon_remove():
            return
        
        
        
    def require_command_input_challenge(self):
        if self.current_status.data() == StatusType.challenge_start:
            return True
        else:
            return False
        
    def command_input_challenge(self):
        if self.command_ask_player_hero_sword_target():
            return
        
        
        
        
        
        
        
        
        
    # def command(self):
    #     if self.current_status.data() == StatusType.turn_execute:
    #         if self.command_ask_player_pass():
    #             return True
    #         if self.command_ask_player_monster_add():
    #             return True
    #         if self.command_ask_player_weapon_remove():
    #             return True
    #     elif self.current_status.data() == StatusType.challenge_start:
    #         if self.command_ask_player_hero_sword_target():
    #             return True
    #     return False
                
            

    def command_ask_player_pass(self):
        player = self.dungeon.phase_turn.turn_player
        msg = '[{}] pass turn ?'.format(player)
        
        if self.command_ask_msg(msg, 'yY'):
            self.dungeon.phase_turn.turn_action = 0
            return True
        return False
        
    def command_ask_player_monster_add(self):
        player  = self.dungeon.phase_turn.turn_player
        monster = self.dungeon.phase_turn.turn_draw_monster
        msg = '[{}] Move {} to dungeon ?'.format(player, monster)
        
        if self.command_ask_msg(msg, 'yY'):
            self.dungeon.phase_turn.turn_action = 1
            return True
        return False
        
    def command_ask_player_weapon_remove(self):
        player  = self.dungeon.phase_turn.turn_player
        monster = self.dungeon.phase_turn.turn_draw_monster
        weapons = self.dungeon.phase_turn.weapon_in_dungeon
        weapons_str = [ str(weapon) for weapon in weapons ]

        msg = '[{}] select weapon to remove'.format(player)
        choice = self.command_ask_choice(msg, weapons_str)
        if choice in range(len(weapons)):
            self.dungeon.phase_turn.turn_action = 2
            self.dungeon.phase_turn.turn_remove_weapon = choice
            return True
        return False
        
    def command_ask_player_hero_sword_target(self):
        player = self.dungeon.phase_challenge.challenge_player
        monsters_str = [ str(m) for m in MonsterType ]
        
        msg = '[{}] select monster to slayer with hero sowrd'.format(player)
        choice = self.command_ask_choice(msg, monsters_str)
        try:
            if choice == 1:
                monster_code = MonsterType.goblin
            elif choice == 2:
                monster_code = MonsterType.skeletonWarrior
            elif choice == 3:
                monster_code = MonsterType.ork
            elif choice == 4:
                monster_code = MonsterType.vampire
            elif choice == 5:
                monster_code = MonsterType.reaper
            elif choice == 6:
                monster_code = MonsterType.satan
            elif choice == 7:
                monster_code = MonsterType.dragon
            
            self.dungeon.phase_challenge.declare_hero_sword(monster_code)
        except:
            print('ERROR')
            return False
        else:
            return True

        
    def command_ask_msg(self, msg, corret_response):
        response = input(msg)
        return response in corret_response
    
    def command_ask_choice(self, msg, items):
        response = input('{} ({}) : '.format(msg, ', '.join(items)))
        return int(response)
        
'''
noname          = ()
goblin          = ()
skeletonWarrior = ()
ork             = ()
vampire         = ()
golam           = ()
reaper          = ()
satan           = ()
dragon          = ()
'''
