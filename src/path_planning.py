import heapq

def heuristic(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def astar(grid, start, end):
    rows = len(grid)
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == end:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        x, y = current
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < rows and grid[nx][ny] == 0:
                temp_g = g_score[current] + 1

                if (nx, ny) not in g_score or temp_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = temp_g
                    f = temp_g + heuristic((nx, ny), end)
                    heapq.heappush(open_set, (f, (nx, ny)))
                    came_from[(nx, ny)] = current

    return []