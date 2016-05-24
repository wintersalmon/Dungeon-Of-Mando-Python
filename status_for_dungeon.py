# Salmonjoon
# DungeonOfMandom
# 2016.05.19
# status_for_dungeon


#from dungeon import Dungeon
from status import Status
from event  import Event
import random

START_STATUS_CODE = 'GameStartStatus'
END_STATUS_CODE   = 'GameEndStatus'
STATUS = dict()


class GameStartStatus(Status):
    def __init__(self):
        super().__init__('GameStartStatus')

    def update(self,data):
        data.set_status(self.code())
        data.init_game()
        event = Event('Game', 'Start', '')
        data.event_insert(event)

    def next_status(self,data):
        return 'NextRoundStatus'

class GameEndStatus(Status):
    def __init__(self):
        super().__init__('GameEndStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.end_game()
        winner = data.winner()
        
        event = Event('Game', 'End', winner)
        data.event_insert(event)
        
    def next_status(self,data):
        return None






class NextRoundStatus(Status):
    def __init__(self):
        super().__init__('NextRoundStatus')
        # self.__run_count = 0
        self.__has_next_round = False

    def update(self,data):
        data.set_status(self.code())
        
        result = data.HasNextRound()
        self.__has_next_round = result
            
        event = Event('Round', 'Next', result)
        data.event_insert(event)
        
    def next_status(self,data):
        if self.__has_next_round:
            return 'RoundStartStatus'
        else:
            return 'GameEndStatus'
        # self.__run_count += 1
        # if self.__run_count % 2 == 1:
        #     return 'RoundStartStatus'
        # else:
        #     return 'GameEndStatus'

class RoundStartStatus(Status):
    def __init__(self):
        super().__init__('RoundStartStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.init_round()
        player_order = data.player_remaining
        
        event = Event('Round', 'Start', player_order)
        data.event_insert(event)
                
    def next_status(self,data):
        return 'NextTurnStatus'

class RoundEndStatus(Status):
    def __init__(self):
        super().__init__('RoundEndStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.end_round()
        
        event = Event('Round', 'End', '')
        data.event_insert(event)
        
    def next_status(self,data):
        return 'NextRoundStatus'






class NextTurnStatus(Status):
    def __init__(self):
        super().__init__('NextTurnStatus')
        self.__has_next_turn = False
        # self.__run_count = 0

    def update(self,data):
        data.set_status(self.code())
        
        result = data.HasNextTurn()
        self.__has_next_turn = result
        
        event = Event('Turn', 'Next', result)
        data.event_insert(event)
        
    def next_status(self,data):
        if self.__has_next_turn:
            return 'TurnStartStatus'
        else:
            return 'ChallengeStartStatus'
        # self.__run_count += 1
        # if self.__run_count % 2 == 1:
        #     return 'TurnStartStatus'
        # else:
        #     return 'ChallengeStartStatus'

class TurnStartStatus(Status):
    def __init__(self):
        super().__init__('TurnStartStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.init_turn()
        turn_player = data.turn_player
        
        event = Event('Turn', 'Start', turn_player)
        data.event_insert(event)
        
    def next_status(self,data):
        return 'TurnExecuteStatus'

class TurnExecuteStatus(Status):
    def __init__(self):
        super().__init__('TurnExecuteStatus')

    def update(self,data):
        data.set_status(self.code())
        
        # TODO : Execute Turn
        data.execute_turn()
        result = data.turn_player_action
        
        event = Event('Turn', 'Execute', result)
        data.event_insert(event)
        
    def next_status(self,data):
        return 'TurnEndStatus'

class TurnEndStatus(Status):
    def __init__(self):
        super().__init__('TurnEndStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.end_turn()
        result = data.turn_player_action

        event = Event('Turn', 'End', result)
        data.event_insert(event)
        
    def next_status(self,data):
        return 'NextTurnStatus'






class  ChallengeStartStatus(Status):
    def __init__(self):
        super().__init__('ChallengeStartStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.init_challenge()
        challenger = data.challenge_player
        
        event = Event('Challenge', 'Start', challenger)
        data.event_insert(event)
        
    def next_status(self,data):
        return 'NextBattleStatus'

class  ChallengeEndStatus(Status):
    def __init__(self):
        super().__init__('ChallengeEndStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.end_challenge()
        challenger = data.challenge_player
        result = 'Won' if data.challenge_victory else 'Lost'
        msg = 'Challenger({}) {} '.format(challenger,result)
        
        event = Event('Challenge', 'End', msg)
        data.event_insert(event)
        
    def next_status(self,data):
        return 'RoundEndStatus'






class NextBattleStatus(Status):
    def __init__(self):
        super().__init__('ChallengeEndStatus')
        self.__has_next_battle = False
        # self.__run_count = 0

    def update(self,data):
        data.set_status(self.code())
        
        result = data.HasNextBattle()
        self.__has_next_battle = result
        
        event = Event('Battle', 'Next', result)
        data.event_insert(event)
        
    def next_status(self,data):
        if self.__has_next_battle:
             return 'ChallengeEndStatus'
        else:
            return 'BattleStartStatus'
        # self.__run_count += 1
        # if self.__run_count % 2 == 1:
        #     return 'ChallengeEndStatus'
        # else:
        #     return 'BattleStartStatus'

class BattleStartStatus(Status):
    def __init__(self):
        super().__init__('BattleStartStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.init_battle()
        
        event = Event('Battle', 'Start', '')
        data.event_insert(event)
        
    def next_status(self,data):
        return 'BattleExecuteStatus'

class BattleExecuteStatus(Status):
    def __init__(self):
        super().__init__('BattleExecuteStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.execute_battle()
        hp      = data.challenge_life_point
        monster = data.battle_monster
        result  = data.battle_victory
        msg = 'HP({}) Monster({}) Result({})'.format(hp,monster,result)
        
        event = Event('Battle', 'Execute', msg)
        data.event_insert(event)
        
    def next_status(self,data):
        return 'BattleEndStatus'

class BattleEndStatus(Status):
    def __init__(self):
        super().__init__('BattleEndStatus')

    def update(self,data):
        data.set_status(self.code())
        
        data.end_battle()
        
        event = Event('Battle', 'End', '')
        data.event_insert(event)
        
    def next_status(self,data):
        return 'NextBattleStatus'




STATUS['GameStartStatus'] = GameStartStatus()
STATUS['GameEndStatus']   = GameEndStatus()

STATUS['NextRoundStatus']  = NextRoundStatus()
STATUS['RoundStartStatus'] = RoundStartStatus()
STATUS['RoundEndStatus']   = RoundEndStatus()

STATUS['NextTurnStatus']    = NextTurnStatus()
STATUS['TurnStartStatus']   = TurnStartStatus()
STATUS['TurnExecuteStatus'] = TurnExecuteStatus()
STATUS['TurnEndStatus']     = TurnEndStatus()

STATUS['ChallengeStartStatus'] = ChallengeStartStatus()
STATUS['ChallengeEndStatus']   = ChallengeEndStatus()

STATUS['NextBattleStatus']    = NextBattleStatus()
STATUS['BattleStartStatus']   = BattleStartStatus()
STATUS['BattleExecuteStatus'] = BattleExecuteStatus()
STATUS['BattleEndStatus']     = BattleEndStatus()