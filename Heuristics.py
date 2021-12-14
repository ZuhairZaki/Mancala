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

heu_dict = { 
    "heuristic1": heuristic1,
    "heuristic2": heurisric2,
    "heuristic3": heuristic3
}