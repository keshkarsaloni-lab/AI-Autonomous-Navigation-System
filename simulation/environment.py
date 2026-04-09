import pygame
import random

WIDTH, HEIGHT = 600, 600
ROWS = 20

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Grid:
    def __init__(self):
        self.rows = ROWS
        self.grid = [[0 for _ in range(ROWS)] for _ in range(ROWS)]

    def add_obstacles(self, count=40):
        for _ in range(count):
            x = random.randint(0, ROWS-1)
            y = random.randint(0, ROWS-1)
            self.grid[x][y] = 1

    def draw(self, win):
        gap = WIDTH // self.rows
        for i in range(self.rows):
            for j in range(self.rows):
                color = WHITE
                if self.grid[i][j] == 1:
                    color = BLACK
                pygame.draw.rect(win, color, (i*gap, j*gap, gap, gap))

        for i in range(self.rows):
            pygame.draw.line(win, BLACK, (0, i*gap), (WIDTH, i*gap))
            pygame.draw.line(win, BLACK, (i*gap, 0), (i*gap, HEIGHT))