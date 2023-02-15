import random
import time
from typing import Tuple

from ..othello.gamestate import GameState

PLUS_INF = float('inf')
MINUS_INF = float('-inf')


# Voce pode criar funcoes auxiliares neste arquivo
# e tambem modulos auxiliares neste pacote.
#
# Nao esqueca de renomear 'your_agent' com o nome
# do seu agente.


def make_move(state: GameState) -> Tuple[int, int]:
    """
    Returns an Othello move
    :param state: state to make the move
    :return: (int, int) tuple with x, y coordinates of the move (remember: 0 is the first row/column)
    """
    # o codigo abaixo apenas retorna um movimento aleatorio valido para
    # a primeira jogada com as pretas.
    # Remova-o e coloque a sua implementacao da poda alpha-beta
    #return random.choice([(2, 3), (4, 5), (5, 4), (3, 2)])
    
    return maxValue(state)

def maxValue(estado):
    if testeTerminal(estado):
        return utilidade(estado)
    v = MINUS_INF
    for jogada in jogadas:
        v = max(v, minValue(jogada))
    return v


def minValue(estado):
    if testeTerminal(estado):
        return utilidade(estado)
    v = PLUS_INF
    for jogada in jogadas:
        v = min(v, maxValue(jogada))
    return v


    