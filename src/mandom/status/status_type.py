# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusType
#

from mandom.containers.auto_number_enum import AutoNumberEnum


class StatusType(AutoNumberEnum):
    none = ()

    game_init = ()
    game_start = ()
    game_next_round = ()
    game_end = ()

    round_init = ()
    round_start = ()
    round_next_turn = ()
    round_challenge = ()
    round_end = ()

    turn_init = ()
    turn_start = ()
    turn_execute = ()
    turn_end = ()

    challenge_init = ()
    challenge_start = ()
    challenge_next_battle = ()
    challenge_end = ()

    battle_init = ()
    battle_start = ()
    battle_execute = ()
    battle_end = ()
