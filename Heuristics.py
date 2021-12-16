from typing import Sized
from MancalaBoard import *

def beans_difference(board: BoardState):
    return (board.player_stores[0]-board.player_stores[1])

def beans_hoarded(board: BoardState):
    player1_beans = 0
    player2_beans = 0
    for i in range(board.pockets):
        player1_beans += board.player_side[0][i]
        player2_beans += board.player_side[1][i]
    
    return (player1_beans-player2_beans)

def repeat_turns(max_side):
    max_chain = 0
    side_copy = max_side[:]
    no_pockets = len(side_copy)
    for i in range(no_pockets):
        inc = (side_copy[i])//(2*no_pockets+1)
        res = (side_copy[i])%(2*no_pockets+1)
        if res==no_pockets-i:
            side_copy[i] = 0
            for j in range(no_pockets):
                if j<=i:
                    side_copy[j] += inc
                else:
                    side_copy[j] += inc+1
            max_chain = max(max_chain,repeat_turns(side_copy)+1)
    return max_chain

def maximize_capture(max_side,min_side):
    max_cap = 0
    side_copy1 = max_side[:]
    side_copy2 = min_side[:]
    no_pockets = len(side_copy1)
    for i in range(no_pockets):
        beans_amount = side_copy1[i]
        if beans_amount!=0:
            j = i+beans_amount
            if j<no_pockets:
                if side_copy1[j]==0:
                    max_cap = max(max_cap,side_copy2[no_pockets-j-1]+1)
            else:
                j -= (2*no_pockets+1)
                if j>=0 and j<=i:
                    if j==i or side_copy1[j]==0:
                        max_cap = max(max_cap,side_copy2[no_pockets-j-1]+2)
    return max_cap
 
def heuristic1(board: BoardState):
    w = 1
    return w*beans_difference(board)

def heurisric2(board: BoardState):
    w1 = 1
    w2 = 0.5
    return w1*beans_difference(board) + w2*beans_hoarded(board)

def heuristic3(board: BoardState):
    w1 = 1
    w2 = 0.5
    w3 = 0.5
    return w1*beans_difference(board) + w2*beans_hoarded(board) + w3*repeat_turns(board.player_side[0])

def heuristic4(board: BoardState):
    w1 = 1
    w2 = 0.5
    w3 = 0.7
    w4 = -0.3
    return w1*beans_difference(board) + w2*beans_hoarded(board) + w3*repeat_turns(board.player_side[0]) \
    + w4*repeat_turns(board.player_side[1])

def heuristic5(board: BoardState):
    w1 = 1
    w2 = 0.5
    w3 = 0.7
    w4 = -0.3
    w5 = 0.7
    return w1*beans_difference(board) + w2*beans_hoarded(board) + w3*repeat_turns(board.player_side[0]) \
    + w4*repeat_turns(board.player_side[1]) + w5*maximize_capture(board.player_side[0],board.player_side[1]) 

def heuristic6(board: BoardState):
    w1 = 1
    w2 = 0.5
    w3 = 0.7
    w4 = -0.3
    w5 = 0.7
    w6 = -0.3
    return w1*beans_difference(board) + w2*beans_hoarded(board) + w3*repeat_turns(board.player_side[0]) \
    + w4*repeat_turns(board.player_side[1]) + w5*maximize_capture(board.player_side[0],board.player_side[1]) \
    + w6*maximize_capture(board.player_side[1],board.player_side[0])

heu_dict = { 
    "heuristic1": heuristic1,
    "heuristic2": heurisric2,
    "heuristic3": heuristic3,
    "heuristic4": heuristic4,
    "heuristic5": heuristic5,
    "heuristic6": heuristic6
}