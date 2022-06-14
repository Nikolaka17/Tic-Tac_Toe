class Board:
    def __init__(self):
        self.board = [0, 0, 0, 0, 0, 0, 0, 0, 0] #0 = empty, 1 = X, 2 = O
        self.turn = 1 #Tells which player is going, 1 for x, 2 for o
        self.winner = 0
    
    def check_winner(self):
        #Check rows
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] != 0:
                self.winner = self.board[i*3]
                return True, (i*3, i*3 + 1, i*3 + 2)
        
        #check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != 0:
                self.winner = self.board[i]
                return True, (i, i + 3, i + 6)
        
        #check diagonals
        if self.board[0] == self.board[4] == self.board[8] != 0:
            self.winner = self.board[0]
            return True, (0, 4, 8)
        if self.board[2] == self.board[4] == self.board[6] != 0:
            self.winner = self.board[2]
            return True, (2, 4, 6)

        return False, (-1, -1, -1)
    
    def find_empty(self):
        for i in range(9):
            if self.board[i] == 0:
                yield i
    
    def place(self, pos):
        if self.board[pos] == 0:
            self.board[pos] = self.turn
            self.turn = 3 - self.turn
            status = self.check_winner()
            if status[0]:
                return True, status[1]