# Salmonjoon
# DungeonOfMandom
# 2016.06.13
#
# Mandom
#

from mandom.phase.phase_battle import PhaseBattle
from mandom.phase.phase_challenge import PhaseChallenge
from mandom.phase.phase_game import PhaseGame
from mandom.phase.phase_round import PhaseRound
from mandom.phase.phase_turn import PhaseTurn


class Mandom(object):
    def __init__(self):
        self.phase_game = PhaseGame()
        self.phase_round = PhaseRound(self.phase_game)
        self.phase_turn = PhaseTurn(self.phase_round)
        self.phase_challenge = PhaseChallenge(self.phase_round)
        self.phase_battle = PhaseBattle(self.phase_challenge)
