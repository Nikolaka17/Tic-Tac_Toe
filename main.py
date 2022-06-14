import pygame
from sys import exit

class Window:
    def __init__(self, width, height):
        #pygame setup
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()

        #general setup
        self.width = width
        self.height = height
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            pygame.display.update()
            self.clock.tick(60)

if __name__ == "__main__":
    window = Window(800, 600)
    window.run()