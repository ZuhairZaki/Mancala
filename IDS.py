from MancalaBoard import *
from Heuristics import *
from AlphaBeta import *


def iterative_deepening_decision(board: BoardState,max_depth,heu_func):
    for d in range(1,max_depth+1):
        bestValue,bestMove = alpha_beta_decision(board,-math.inf,math.inf,d,heu_func)
    return bestValue, bestMove