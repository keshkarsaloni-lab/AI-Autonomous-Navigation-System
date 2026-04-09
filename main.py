import pygame
from simulation.environment import Grid
from src.path_planning import astar
from src.navigation import move_agent

pygame.init()
WIN = pygame.display.set_mode((600,600))
pygame.display.set_caption("Autonomous Navigation")

grid = Grid()
grid.add_obstacles()

start = None
end = None

run = True
while run:
    WIN.fill((255,255,255))
    grid.draw(WIN)

    if start:
        gap = 600 // grid.rows
        pygame.draw.rect(WIN, (0,255,0), (start[0]*gap, start[1]*gap, gap, gap))

    if end:
        gap = 600 // grid.rows
        pygame.draw.rect(WIN, (255,0,0), (end[0]*gap, end[1]*gap, gap, gap))

    pygame.display.update()

    if start and end:
     path = astar(grid.grid, start, end)
     move_agent(path, grid, WIN)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            x, y = pos

            gap = 600 // grid.rows
            row = x // gap
            col = y // gap

            if not start:
                start = (row, col)
                print("Start:", start)

            elif not end and (row, col) != start:
                end = (row, col)
                print("End:", end)

            if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RETURN:
                    

              pygame.quit()