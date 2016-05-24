# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# Dungeon

from monster import GoblinMonster, SkeletonWarriorMonster, OrkMonster, VampireMonster, GolamMonster, ReaperMonster, SatanMonster, DragonMonster
from weapon  import TorchWeapon, HolyGrailWeapon, SpearWeapon, ArmorWeapon, ShieldWeapon, HeroSwordWeapon
from player  import Player
from event_recorder import EventRecorder

class Dungeon(EventRecorder):
    def __init__(self):
        super().__init__()
        
        # default members
        self.player_list  = list()
        self.monster_list = list()
        self.weapon_list  = list()
        
        # members used in game
        self.current_status = 'none'
        self.winner_id    = None
        
        # members used in round
        self.player_remaining  = list()
        self.player_removed    = list()
        self.monster_remaining = list()
        self.monster_removed   = list()
        self.weapon_remaining  = list()
        self.weapon_removed    = list()

        # members used in turn
        self.turn_player_action   = 0
        self.turn_player_option   = 0
        self.turn_player          = list()
        self.turn_draw_monster    = list()
        self.turn_selected_weapon = list()

        # members used in challenge
        self.challenge_player     = None
        self.challenge_life_point = 0
        self.challenge_monsters   = list()
        self.challenge_weapons    = list()
        self.challenge_victory    = None

        # members used in battle
        self.battle_monster = list()
        self.battle_victory = list()

        # init monster_list
        self.monster_list.append(GoblinMonster())
        self.monster_list.append(GoblinMonster())
        self.monster_list.append(SkeletonWarriorMonster())
        self.monster_list.append(SkeletonWarriorMonster())
        self.monster_list.append(OrkMonster())
        self.monster_list.append(OrkMonster())
        self.monster_list.append(VampireMonster())
        self.monster_list.append(VampireMonster())
        self.monster_list.append(GolamMonster())
        self.monster_list.append(GolamMonster())
        self.monster_list.append(ReaperMonster())
        self.monster_list.append(SatanMonster())
        self.monster_list.append(DragonMonster())
        
        # init weapon_list
        self.weapon_list.append(TorchWeapon())
        self.weapon_list.append(HolyGrailWeapon())
        self.weapon_list.append(SpearWeapon())
        self.weapon_list.append(ArmorWeapon())
        self.weapon_list.append(ShieldWeapon())
        self.weapon_list.append(HeroSwordWeapon())


    def connect_player(self,connected_player):
        if isinstance(connected_player,Player):
            self.player_list.append(connected_player)
            return True
        return False

    def disconnect_player(self, target_player):
        if target_player in self.player_list:
            self.player_list.remove(target_player)
            return True
        return False


    def set_status(self, new_status):
        self.current_status = new_status
        
    def get_status(self):
        return self.current_status
    
    def winner(self):
        if self.winner_id:
            return self.player_list[self.winner_id]
        return None
        

    def init_game(self):
        # self.current_status = 'none'
        del self.monster_remaining[:]
        del self.monster_removed[:]
        del self.weapon_remaining[:]
        del self.weapon_removed[:]
        del self.player_remaining[:]
        del self.player_removed[:]
        
        self.monster_remaining = [ m for m in range(len(self.monster_list)) ]
        self.weapon_remaining  = [ w for w in range(len(self.weapon_list)) ]
        self.player_remaining  = [ p for p in range(len(self.player_list)) ]

    def init_round(self):
        del self.player_remaining[:]
        del self.player_removed[:]
        self.player_remaining = [ id for id, player in enumerate(self.player_list) if player.life_point() > 0 ]
        
        
    def init_turn(self):
        self.turn_player_action   = 0
        self.turn_player          = self.player_remaining[0]
        self.turn_draw_monster    = self.monster_remaining[-1]
        self.turn_selected_weapon = None
    
    def init_challenge(self):
        self.challenge_player     = self.player_remaining[0]
        self.challenge_victory    = False
        self.challenge_life_point = 3
        del self.challenge_monsters[:]
        del self.challenge_weapons[:]
        
        for id in self.weapon_remaining:
            self.challenge_life_point += self.weapon_list[id].armor()
        self.challenge_monsters = [ m for m in range(len(self.monster_list)) ]
        self.challenge_weapons  = [ w for w in range(len(self.weapon_list)) ]
        
    def init_battle(self):
        self.battle_monster = self.challenge_monsters.pop(-1)
        self.battle_victory = False

    # Check if there is only one winner (victory point 2)
    # Check if there is only one surviver (life point more then zero)
    def HasNextRound(self):        
        winner_count = 0
        surviver_count = 0
        for player in self.player_list:
            if player.victory_point() == 2:
                winner_count += 1
            if player.life_point() > 0:
                surviver_count += 1
        
        if winner_count == 1:
            return False
        if surviver_count == 1:
            return False
        return True
    
    # Check if there is more then one player left in round
    def HasNextTurn(self):
        if len(self.player_remaining) > 1:
            return True
        return False
    
    # Check if there is monster left in challenge
    # Check if hero has HP left
    def HasNextBattle(self):
        if len(self.challenge_monsters) > 0 and self.challenge_life_point > 0:
            return True
        return False
        
    # Find winner or surviver
    def end_game(self):
        winner   = None
        surviver = None
        for player in self.player_list:
            if player.victory_point() == 2:
                winner = player
            if player.life_point() > 0:
                surviver = player
        
        if winner:
            return winer
        if surviver:
            return surviver
        return None
        
    def end_round(self):
        pass
        
    def end_turn(self):
        if self.turn_player_action == 0: # Passed
            self.player_remaining.remove(self.turn_player)
            return
        else:
            if self.turn_player_action == 1: # Stack Monster
                self.monster_removed.append(self.turn_draw_monster)
                
            if self.turn_player_action == 2: # Remove Weapon
                self.weapon_removed.append(self.turn_selected_weapon)

            self.player_remaining.pop(self.turn_player)
            self.player_remaining.append(self.turn_player)
        
        # if self.player_list[self.turn_player].passed():
        #     self.player_remaining.remove(self.turn_player)
        # else:
        #     self.player_remaining.pop(self.turn_player)
        #     self.player_remaining.append(self.turn_player)
    
    # If challenge Won (life > 0 and monster == 0)
    #   challenger gain victory point
    # If challenge Lost
    #   challenger lost life point
    def end_challenge(self):
        if self.challenge_life_point > 0 and len(self.challenge_monsters) == 0:
            self.player_list[self.challenge_player].gain_victory_point()
        else:
            self.player_list[self.challenge_player].lose_life_point()
        
    # If battle lost
    #   give damage to hero
    def end_battle(self):
        if self.battle_victory:
            return
        damage  = self.monster_list[self.battle_monster].damage()
        hp      = self.challenge_life_point
                
        self.challenge_life_point = hp - damage if (hp - damage) > 0 else 0
    
    
    def execute_turn(self):
        cur_player  = self.player_list[self.turn_player]
        
        if cur_player.ask_pass():
            self.turn_player_action = 0
            return
            
        if cur_player.ask_stack_monster_to_dungeon(self.turn_draw_monster):
            self.turn_player_action = 1
            return
        
        weapon_num = cur_player.ask_weapon_to_remove(self.weapon_remaining)
        if weapon_num >= 0:
            self.turn_player_action   = 2
            self.turn_selected_weapon = weapon_num
            return
        
    def execute_battle(self):
        victory = False
        
        monster = self.monster_list[self.battle_monster]
        for w_id in self.challenge_weapons:
            if self.weapon_list[w_id].can_slayer_monster(monster):
                victory = True
                break
                
        self.battle_victory = victory
        

### TEST ###

def Test():
    dungeon = Dungeon()
    
    # create game
    print('create game')
    p1 = Player('salmon')
    p2 = Player('kein')
    dungeon.connect_player(p1)
    dungeon.connect_player(p2)

    # test game
    print('init game')
    dungeon.init_game()
    print_with_prefix('Status', dungeon.get_status())
    print_with_prefix('Players', dungeon.player_list )
    print_with_prefix('Monsters', dungeon.monster_list)
    print_with_prefix('Weapons', dungeon.weapon_list)
    
    # test round
    print('init round')
    dungeon.init_round()
    print_with_prefix('player_remaining', dungeon.player_remaining)
    print_with_prefix('player_removed', dungeon.player_removed)
    
    # test turn
    print('init turn')
    dungeon.init_turn()
    print_with_prefix('turn_player', dungeon.turn_player)
    print_with_prefix('turn_draw_monster', dungeon.turn_draw_monster)
    print_with_prefix('turn_selected_weapon', dungeon.turn_selected_weapon)
    
    
    # test challenge
    print('init challenge')
    dungeon.init_challenge()
    print_with_prefix('challenge_player', dungeon.challenge_player)
    print_with_prefix('challenge_life_point', dungeon.challenge_life_point)
    print_with_prefix('challenge_monsters', dungeon.challenge_monsters)
    print_with_prefix('challenge_weapons', dungeon.challenge_weapons)
    print_with_prefix('challenge_victory', dungeon.challenge_victory)
    
    
    # test battle
    print('init battle')
    dungeon.init_battle()
    print_with_prefix('battle_monster', dungeon.battle_monster)
    print_with_prefix('battle_victory', dungeon.battle_victory)
    
    
    


    
    
def print_with_prefix(prefix,items):
    content = get_content_str(items)
    print('{} : {}'.format(prefix, content))

def get_content_str(items):
    if isinstance(items,list):
        size    = len(items)
        content = ''
        for item in items:
            content += get_content_str(item) + ' '
        return '({})[{}]'.format(size, content)
    else:
        return str(items)

#Test()
