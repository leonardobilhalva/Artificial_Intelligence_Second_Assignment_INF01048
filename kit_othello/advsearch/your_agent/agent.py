import random
import time
from typing import Tuple

from ..othello.gamestate import GameState

PLUS_INF = float('inf')
MINUS_INF = float('-inf')
MAX_DEPTH = 3
MIN_DEPTH = 0
NONE_POS = (-1, -1)


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    # """
    # if state.player != 'B' or state.player != 'W':
    #     raise ValueError("Player is neither black or white colored")
    
    _, nextMove = maxValue(state, MIN_DEPTH, MINUS_INF, PLUS_INF)
    return nextMove

def maxValue(state: GameState, depth: int, alpha, beta):
    if shouldEval(state, depth):
        return heuristicEvaluation(state), NONE_POS
    
    v = MINUS_INF 
    move = NONE_POS    
    possibleMoves = state.board.legal_moves(state.player)
    
    if len(possibleMoves) == 0:
        possibleMoves.add(NONE_POS)
    
    for moveAux in possibleMoves:        
        auxBoard = state.board.copy()
        auxBoard.process_move(moveAux, state.player)      
        vAux, _ = minValue(GameState(auxBoard, state.board.opponent(state.player)), depth+1, alpha, beta)
        if vAux > v:
            v = vAux
            move = moveAux                    
        alpha = max(alpha, v)
        if alpha >= beta:
            break   
                 
    return v, move


def minValue(state: GameState, depth: int, alpha, beta):
    if shouldEval(state, depth):
        return heuristicEvaluation(state), NONE_POS
    v = PLUS_INF    
    move = NONE_POS    
    possibleMoves = state.board.legal_moves(state.player)
    
    if len(possibleMoves) == 0:
        possibleMoves.add(NONE_POS)
    
    for moveAux in possibleMoves:        
        auxBoard = state.board.copy()
        auxBoard.process_move(moveAux, state.player)        
        vAux, _ = maxValue(GameState(auxBoard, state.board.opponent(state.player)), depth+1, alpha, beta)
        if vAux > v:
            v = vAux
            move = moveAux                    
        beta = min(beta, v)
        if beta <= alpha:
            break   
                 
    return v, move



def shouldEval(state: GameState, depth: int):
    '''check if 'state' should be evaluated by heuristic'''
    return depth > MAX_DEPTH  or state.board.is_terminal_state() or (not state.board.has_legal_move(state.player) and depth == 0)

def heuristicEvaluation(state: GameState):    
    '''heuristic dummy evaluation function'''
    return random.randint(-10, 10)