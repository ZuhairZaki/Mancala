from copy import *

class BoardState:
    def __init__(self,n=6,player=0):
        self.pockets = n
        self.player = player
        self.player_stores = [0,0]
        self.player_side = [[4]*self.pockets,[4]*self.pockets]

    def __repr__(self):
        s = "Player 2\n\n"
        s += "Store: "+str(self.player_stores[1])+"\n\n"
        s += "-------------------------------------------\n\n"

        for i in range(self.pockets):
            s += str(self.player_side[1][self.pockets-i-1])+"\t"

        s += "\n\n"
        s += "-------------------------------------------\n\n"

        for i in range(self.pockets):
            s += str(self.player_side[0][i])+"\t"
        
        s += "\n\n"
        s += "-------------------------------------------\n\n"
        s += "Store: "+str(self.player_stores[0])+"\n\n"
        s += "Player 1\n\n"

        return s

    def get_legal_moves(self):
        actions = []
        pockets = self.player_side[self.player]
        for i in range(len(pockets)):
            if pockets[i]!=0:
                actions.append(i)
        return actions

    def is_terminal(self):
        terminal = False

        sum = 0
        for p in self.player_side[0]:
            sum += p
        if sum==0:
            terminal = True

        if not terminal:
            sum = 0
            for p in self.player_side[1]:
                sum += p
            if sum==0:
                terminal = True

        if terminal:
            for i in range(self.pockets):
                self.player_stores[0] += self.player_side[0][i]
                self.player_side[0][i] = 0
                self.player_stores[1] += self.player_side[1][i]
                self.player_side[1][i] = 0

        return terminal

    def perform_move(self,action):
        next_board = deepcopy(self)

        pockets = next_board.player_side[self.player]
        beans = pockets[action]
        pockets[action] = 0

        pocket_no = action+1
        curr_side = self.player
        next_player = 1-self.player
        while beans>0:
            next_player = 1-self.player
            while pocket_no<len(pockets) and beans>0:
                pockets[pocket_no] += 1
                beans -= 1
                pocket_no += 1
            
            if beans==0:
                break

            if curr_side==self.player:
                next_board.player_stores[self.player] += 1
                beans -= 1
                next_player = self.player

            curr_side = 1-curr_side
            pockets = next_board.player_side[curr_side]
            pocket_no = 0

        
        if curr_side==self.player and pockets[pocket_no-1]==1:
            opp_beans = next_board.player_side[1-self.player][next_board.pockets-pocket_no]
            next_board.player_stores[self.player] += opp_beans+1
            pockets[pocket_no-1]=0
            next_board.player_side[1-self.player][next_board.pockets-pocket_no] = 0

        next_board.player = next_player

        return next_board