# Salmonjoon
# DungeonOfMandom
# 2016.05.26
#
# dungeon
#

# from mandom.events.event import Event

# from mandom.player import Player

# from mandom.containers.recorder import Recorder

from mandom.phase.phase_game      import PhaseGame
from mandom.phase.phase_round     import PhaseRound
from mandom.phase.phase_turn      import PhaseTurn
from mandom.phase.phase_challenge import PhaseChallenge
from mandom.phase.phase_battle    import PhaseBattle

class Dungeon():
    def __init__(self):
        self.phase_game   = PhaseGame()
        self.phase_round  = PhaseRound(self.phase_game)
        self.phase_turn   = PhaseTurn(self.phase_round)
        self.phase_challenge = PhaseChallenge(self.phase_round)
        self.phase_battle = PhaseBattle(self.phase_challenge)
        
        self.current_status_code = None
        
        self.event_recorder = list()
        
    def change_status_code(self, new_status_code):
        self.current_status_code = new_status_code
        
