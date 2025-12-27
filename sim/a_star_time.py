# sim/a_star_time.py

import heapq

def a_star_time(grid, start, goal, reservations):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    open_set = []
    heapq.heappush(open_set, (0, start, 0))
    came_from = {}
    g_score = {(start, 0): 0}

    while open_set:
        _, current, t = heapq.heappop(open_set)

        if current == goal:
            path = [current]
            while (current, t) in came_from:
                current, t = came_from[(current, t)]
                path.append(current)
            return list(reversed(path))

        for neighbor in grid.neighbors(current):
            next_t = t + 1

            if reservations.is_vertex_conflict(neighbor, next_t):
                continue
            if reservations.is_edge_conflict(current, neighbor, next_t):
                continue

            state = (neighbor, next_t)
            tentative_g = g_score[(current, t)] + 1

            if state not in g_score or tentative_g < g_score[state]:
                g_score[state] = tentative_g
                f = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f, neighbor, next_t))
                came_from[state] = (current, t)

    return None
