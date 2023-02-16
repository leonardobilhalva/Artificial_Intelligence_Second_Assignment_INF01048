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
    """    
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
    '''heuristic evaluation function
    this function was based on the following article: https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf
    and also used the corner reach idea of this post: https://kartikkukreja.wordpress.com/2013/03/30/heuristic-function-for-reversiothello/ (based on the previous article too)'''
    
    weightParityHeuristic = 0
    weightMobilityHeuristic = 0
    weightCornerHeuristic = 0
    weightCornerReachHeuristic = 0
    
    maxCoins = state.board.num_pieces(state.player)
    minCoins = state.board.num_pieces(state.board.opponent(state.player))    
    parityHeuristic = 100 * (maxCoins - minCoins)/ (maxCoins + minCoins)
    
    maxMobility = len(state.board.legal_moves(state.player))
    minMobility = len(state.board.legal_moves(state.board.opponent(state.player)))        
    if(maxMobility + minMobility) != 0:
        mobilityHeuristic = 100 * (maxMobility - minMobility)/ (maxMobility + minMobility)
    else:
        mobilityHeuristic = 0

    
    maxCorner = 0
    minCorner = 0        
    maxCornerReach = 0
    minCornerReach = 0    
    corners = [0, 7, 56, 63]    
    for corner in corners:
        if state.board.__str__()[corner] == '.':
            if corner == 0:
                if state.board.tiles[0][1] == state.player:
                    maxCornerReach += 1
                elif state.board.tiles[0][1] == state.board.opponent(state.player):
                    minCornerReach += 1                
                else:
                    for y in range (2):
                        if state.board.tiles[1][y] == state.player:
                            maxCornerReach += 1
                        elif state.board.tiles[1][y] == state.board.opponent(state.player):
                            minCornerReach += 1                
            if corner == 7:
                if state.board.tiles[0][6] == state.player:
                    maxCornerReach += 1
                elif state.board.tiles[0][6] == state.board.opponent(state.player):
                    minCornerReach += 1                
                else:
                    for y in range (6,8):
                        if state.board.tiles[1][y] == state.player:
                            maxCornerReach += 1
                        elif state.board.tiles[1][y] == state.board.opponent(state.player):
                            minCornerReach += 1                
            if corner == 56:
                if state.board.tiles[7][1] == state.player:
                    maxCornerReach += 1
                elif state.board.tiles[7][1] == state.board.opponent(state.player):
                    minCornerReach += 1                
                else:
                    for y in range (2):
                        if state.board.tiles[6][y] == state.player:
                            maxCornerReach += 1
                        elif state.board.tiles[6][y] == state.board.opponent(state.player):
                            minCornerReach += 1                
            if corner == 63:
                if state.board.tiles[7][6] == state.player:
                    maxCornerReach += 1
                elif state.board.tiles[7][6] == state.board.opponent(state.player):
                    minCornerReach += 1                
                else:
                    for y in range (6,8):
                        if state.board.tiles[6][y] == state.player:
                            maxCornerReach += 1
                        elif state.board.tiles[6][y] == state.board.opponent(state.player):
                            minCornerReach += 1                
        elif state.board.__str__()[corner] == state.player:
            maxCorner += 1
        else:
            minCorner += 1   
                     
    if(maxCorner+ minCorner) != 0:
        cornerHeuristic = 100 * (maxCorner - minCorner)/ (maxCorner + minCorner)
    else:
        cornerHeuristic = 0
        
    cornerReachHeuristic = -25 * (maxCornerReach - minCornerReach)     
    
    
    return (weightParityHeuristic * parityHeuristic) + (weightMobilityHeuristic * mobilityHeuristic) + (weightCornerHeuristic * cornerHeuristic) + (weightCornerReachHeuristic * cornerReachHeuristic) 