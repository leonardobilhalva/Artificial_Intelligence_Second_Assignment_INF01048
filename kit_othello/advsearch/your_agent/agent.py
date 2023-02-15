import random
import time
from typing import Tuple

from ..othello.gamestate import GameState

PLUS_INF = float('inf')
MINUS_INF = float('-inf')
MAX_DEPTH = 5


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    if state.player != 'B' or state.player != 'W':
        raise ValueError("Player is neither black or white colored")
    
    _, nextMove = maxValue(state, 0, MINUS_INF, PLUS_INF)
    return nextMove

def maxValue(state, depth, alpha, beta):
    if shouldEval(state, depth):
        return heuristicEvaluation(state), (-1, -1)
    v = MINUS_INF
    
    
    for play in state.board.legal_moves():       
        
        v = max(v, minValue(play)) #
    return v






def minValue(state, depth, alpha, beta):
    if shouldEval(state, depth):
        return heuristicEvaluation(state), (-1, -1)
    v = PLUS_INF
    
    
    for play in state.board.legal_moves():
        v = min(v, maxValue(play))
    return v



def shouldEval(state: GameState, depth):
    '''check if 'state' should be evaluated by heuristic'''
    return depth > MAX_DEPTH  or state.board.is_terminal_state() or (not state.board.has_legal_move(state.player) and depth == 0)

def heuristicEvaluation(state: GameState):    
    return random.randint(-10, 10)
