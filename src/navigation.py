def move_agent(path, grid_obj, win):
    import pygame

    gap = 600 // grid_obj.rows

    for node in path:
        x, y = node
        pygame.draw.rect(win, (0,255,0), (x*gap, y*gap, gap, gap))
        pygame.display.update()
        pygame.time.delay(100)