from math import inf

class Board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0] #0 = empty, 1 = X, 2 = O
        self.turn = 1 #Tells which player is going, 1 for x, 2 for o
        self.winner = 0
    
    def check_state(self, state): #finds a winner in a format for the mimimax algorithm
        #check rows
        for i in range(3):
            if state[i*3] == state[i*3 + 1] == state[i*3 + 2] != 0:
                return True, 1 if state[i*3] == 2 else -1
        
        #check columns
        for i in range(3):
            if state[i] == state[i + 3] == state[i + 6] != 0:
                return True, 1 if state[i] == 2 else -1
        
        #check diagonals
        if state[0] == state[4] == state[8] != 0:
            return True, 1 if state[4] == 2 else -1
        if state[2] == state[4] == state[6] != 0:
            return True, 1 if state[4] == 2 else -1
        
        #check tie
        if 0 not in state:
            return True, 0
        
        return False, None
    
    def check_winner(self):
        #Check rows
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] != 0:
                self.winner = self.board[i*3]
                return True, (i*3, i*3 + 1, i*3 + 2), "H"
        
        #check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != 0:
                self.winner = self.board[i]
                return True, (i, i + 3, i + 6), "V"
        
        #check diagonals
        if self.board[0] == self.board[4] == self.board[8] != 0:
            self.winner = self.board[0]
            return True, (0, 4, 8), "D"
        if self.board[2] == self.board[4] == self.board[6] != 0:
            self.winner = self.board[2]
            return True, (2, 4, 6), "D"

        return False, (-1, -1, -1), "N"
    
    def find_empty(self, state):
        for i in range(9):
            if state[i] == 0:
                yield i
    
    def place(self, pos):
        if self.board[pos] == 0:
            self.board[pos] = self.turn
            self.turn = 3 - self.turn
    
    def minimax(self, state, depth, is_max): #computer will always be O (2)
        done, score = self.check_state(state)
        if done:
            return None, score
        if depth == 0:
            return None, score

        moves = list(self.find_empty(state))
        best_move = moves[0]

        if is_max:
            max_score = -inf
            for move in moves:
                new_state = state.copy()
                new_state[move] = 2
                new_score = self.minimax(new_state, depth-1, False)[1]
                if new_score > max_score:
                    max_score = new_score
                    best_move = move
            return best_move, max_score
        
        else:
            min_score = inf
            for move in moves:
                new_state = state.copy()
                new_state[move] = 1
                new_score = self.minimax(new_state, depth-1, True)[1]
                if new_score < min_score:
                    min_score = new_score
                    best_move = move
            return best_move, min_score