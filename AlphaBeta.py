from MancalaBoard import *
from Heuristics import *
import math

def alpha_beta_decision(board: BoardState,alpha,beta,depth,heu_func):
    if board.is_terminal() or depth==0:
        return heu_dict.get(heu_func)(board)

    if board.player==0:
        best_val = -math.inf
        best_move = -1
        valid_moves = board.get_legal_moves()
        for m in valid_moves:
            res_board = board.perform_move(m)
            val, = alpha_beta_decision(res_board,alpha,beta,depth-1,heu_func)
            if val>best_val:
                best_val = val
                best_move = m
            
            if best_val>=beta:
                return best_val, best_move

            alpha = max(alpha,best_val)
        return best_val, best_move
    else:
        best_val = math.inf
        best_move = -1
        valid_moves = board.get_legal_moves()
        for m in valid_moves:
            res_board = board.perform_move(m)
            val, = alpha_beta_decision(res_board,alpha,beta,depth-1,heu_func)
            if val<best_val:
                best_val = val
                best_move = m
            
            if best_val<=alpha:
                return best_val, best_move

            beta = min(beta,best_val)
        return best_val, best_move

    