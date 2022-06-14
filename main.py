import pygame
from sys import exit
from board import Board

class Window:
    def __init__(self, size):
        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((size, size))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()

        #general setup
        self.size = size
        self.board = Board()
        self.won = (False, (-1, -1, -1), "N")
    
    def draw_winner(self, line, type):
        num_to_coord = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (0, 1), 4: (1, 1), 5: (2, 1), 6: (0, 2), 7: (1, 2), 8: (2, 2)}
        start = num_to_coord[line[0]]
        end = num_to_coord[line[-1]]
        if type == "D":
            if line[0] == 0 and line[2] == 8:
                pygame.draw.line(self.screen, (0,255,0), (0,0), (self.size, self.size), width=10)
            elif line[0] == 2 and line[2] == 6:
                pygame.draw.line(self.screen, (0,255,0), (self.size,0), (0, self.size), width=10)
        elif type == "H":
            pygame.draw.line(self.screen, (0, 255, 0), (0, (start[1]*self.size/3) + self.size/6), (self.size, (start[1]*self.size/3) + self.size/6), width=10)
        elif type == "V":
            pygame.draw.line(self.screen, (0, 255, 0), ((start[0]*self.size/3) + self.size/6, 0), ((start[0]*self.size/3) + self.size/6, self.size), width=10)
    
    def draw_x(self, pos):
        num_to_coord = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (0, 1), 4: (1, 1), 5: (2, 1), 6: (0, 2), 7: (1, 2), 8: (2, 2)} #translates from matrix to array
        coord = num_to_coord[pos]
        pygame.draw.line(self.screen, (255, 0, 0), (coord[0]*self.size/3 + 8, coord[1]*self.size/3 + 8), ((coord[0]*self.size/3) + self.size/3 -8, (coord[1]*self.size/3) + self.size/3 -8), width=10)
        pygame.draw.line(self.screen, (255, 0, 0), ((coord[0]*self.size/3) + self.size/3 - 8, (coord[1]*self.size/3) + 8), (coord[0]*self.size/3 + 8, (coord[1]*self.size/3) + self.size/3 - 8), width = 10)

    def draw_o(self, pos):
        num_to_coord = {0: (0, 0), 1: (1, 0), 2: (2, 0), 3: (0, 1), 4: (1, 1), 5: (2, 1), 6: (0, 2), 7: (1, 2), 8: (2, 2)}
        coord = num_to_coord[pos]
        pygame.draw.circle(self.screen, (0, 0, 255), (coord[0]*self.size/3 + self.size/6, coord[1]*self.size/3 + self.size/6), self.size/6 - 8)
    
    def draw_grid(self):
        for i in range(1, 4):
            pygame.draw.line(self.screen, (255, 255, 255), (0, i*self.size/3), (self.size, i*self.size/3))
            pygame.draw.line(self.screen, (255, 255, 255), (i*self.size/3, 0), (i*self.size/3, self.size))
        for i in range(9):
            if self.board.board[i] == 1:
                self.draw_x(i)
            elif self.board.board[i] == 2:
                self.draw_o(i)
        if self.won[0]:
            self.draw_winner(self.won[1], self.won[2])
       
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key in (pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9):
                        self.win = self.board.place(event.key - 49)
            
            self.draw_grid()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    window = Window(900)
    window.run()