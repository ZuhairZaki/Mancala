from MancalaBoard import *
from Heuristics import *
from AlphaBeta import *
import math

print("Choose Mode:")
print("1. AI vs Human")
print("2. Human vs AI")
print("3. AI vs AI")

choice = int(input())

if choice==1:
    curr_board = BoardState()
    while not curr_board.is_terminal():
        print(curr_board)
        if curr_board.player==0:
            val, ai_move = alpha_beta_decision(curr_board,-math.inf,math.inf,11,"heuristic3")
            print("Player 1 performing move ",ai_move,"\n\n")
            curr_board = curr_board.perform_move(ai_move)
        else:
            human_move = int(input("Choose a move: "))
            print("Player 2 performing move ",human_move,"\n\n")
            curr_board = curr_board.perform_move(human_move)
elif choice==2:
    curr_board = BoardState()
    while not curr_board.is_terminal():
        print(curr_board)
        if curr_board.player==1:
            val, ai_move = alpha_beta_decision(curr_board,-math.inf,math.inf,11,"heuristic3")
            print("Player 2 performing move ",ai_move,"\n\n")
            curr_board = curr_board.perform_move(ai_move)
        else:
            human_move = int(input("Choose a move: "))
            print("Player 1 performing move ",human_move,"\n\n")
            curr_board = curr_board.perform_move(human_move)
elif choice==3:
    pass
else:
    print("Invalid Mode")



