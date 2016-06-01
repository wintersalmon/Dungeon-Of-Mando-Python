# Salmonjoon
# DungeonOfMandom
# 2016.05.28
#
# StatusManager
#

from mandom.status.status_type import StatusType

from mandom.status.status_game_start import StatusGameStart
from mandom.status.status_game_end import StatusGameEnd

from mandom.status.status_next_round import StatusNextRound 
from mandom.status.status_round_start import StatusRoundStart 
from mandom.status.status_round_end import StatusRoundEnd

from mandom.status.status_next_turn import StatusNextTurn
from mandom.status.status_turn_start import StatusTurnStart 
from mandom.status.status_turn_execute import StatusTurnExecute
from mandom.status.status_turn_end import StatusTurnEnd

from mandom.status.status_challenge_start import StatusChallengeStart
from mandom.status.status_challenge_end import StatusChallengeEnd

from mandom.status.status_next_battle import StatusNextBattle
from mandom.status.status_battle_start import StatusBattleStart
from mandom.status.status_battle_execute import StatusBattleExecute
from mandom.status.status_battle_end import StatusBattleEnd

class StatusManager():
    def __init__(self, dungeon):
        self.__dungeon = dungeon
        self.__status_handlers = dict()
        self.__cur_status_code = StatusType.none
        self.__starting_status_code = StatusType.game_start
        self.__final_status_code = StatusType.game_end
        
        self.__register(StatusGameStart())
        self.__register(StatusGameStart())
        
        self.__register(StatusNextRound())
        self.__register(StatusRoundStart())
        self.__register(StatusRoundEnd())
        
        self.__register(StatusNextTurn())
        self.__register(StatusTurnStart())
        self.__register(StatusTurnExecute())
        self.__register(StatusTurnEnd())
        
        self.__register(StatusChallengeStart())
        self.__register(StatusChallengeEnd())
        
        self.__register(StatusNextBattle())
        self.__register(StatusBattleStart())
        self.__register(StatusBattleExecute())
        self.__register(StatusBattleEnd())
        

    def __register(self, status):
        code = status.start_status()
        self.__status_handlers[code] = status
        
    def start(self):
        self.__cur_status_code = self.__starting_status_code
    
    def is_end(self):
        return self.__cur_status_code == self.__final_status_code
    
    def next(self):
        if self.__cur_status_code == StatusType.none:
            return False
        
        cur_status = self.__status_handlers[self.__cur_status_code]
        next_status = cur_status.update(self.__dungeon)
        self.__cur_status_code = next_status
        return True
        
    