# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusType
#

from mandom.containers.auto_number_enum import AutoNumberEnum

class StatusType(AutoNumberEnum):
    none = ()
    
    game = ()
    game_start = ()
    game_end   = ()
    
    round = ()
    next_round = ()
    round_start = ()
    round_end = ()
    
    turn = ()
    next_turn = ()
    turn_start = ()
    turn_execute = ()
    turn_end = ()
    
    challenge = ()
    challenge_start = ()
    challenge_end = ()
    
    battle = ()
    next_battle = ()
    battle_start = ()
    battle_execute = ()
    battle_end = ()