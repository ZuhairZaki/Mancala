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
    print(curr_board)
    while not curr_board.is_terminal():
        if curr_board.player==0:
            val, ai_move = alpha_beta_decision(curr_board,-math.inf,math.inf,11,"heuristic6")
            print("Player 1 performing move ",ai_move,"\n\n")
            curr_board = curr_board.perform_move(ai_move)
        else:
            legal_moves = curr_board.get_legal_moves()
            while True:
                human_move = int(input("Choose a move: "))
                if human_move in legal_moves:
                    print("Player 2 performing move ",human_move,"\n\n")
                    curr_board = curr_board.perform_move(human_move)
                    break
                else:
                    print("Illegal Move\n\n")
        print(curr_board)
    print(curr_board)
    player1_score = curr_board.player_stores[0]
    player2_score = curr_board.player_stores[1]
    if player1_score>player2_score:
        print("Player 1 Wins!!!\n\n")
    elif player2_score>player1_score:
        print("Player 2 Wins!!!\n\n")
    else:
        print("Tie!!!\n\n")
elif choice==2:
    curr_board = BoardState()
    print(curr_board)
    while not curr_board.is_terminal():
        if curr_board.player==1:
            val, ai_move = alpha_beta_decision(curr_board,-math.inf,math.inf,11,"heuristic6")
            print("Player 2 performing move ",ai_move,"\n\n")
            curr_board = curr_board.perform_move(ai_move)
        else:
            legal_moves = curr_board.get_legal_moves()
            while True:
                human_move = int(input("Choose a move: "))
                if human_move in legal_moves:
                    print("Player 1 performing move ",human_move,"\n\n")
                    curr_board = curr_board.perform_move(human_move)
                    break
                else:
                    print("Illegal Move")
        print(curr_board)
    print(curr_board)
    player1_score = curr_board.player_stores[0]
    player2_score = curr_board.player_stores[1]
    if player1_score>player2_score:
        print("Player 1 Wins!!!\n\n")
    elif player2_score>player1_score:
        print("Player 2 Wins!!!\n\n")
    else:
        print("Tie!!!\n\n")
elif choice==3:
    curr_board = BoardState()
else:
    print("Invalid Mode")



