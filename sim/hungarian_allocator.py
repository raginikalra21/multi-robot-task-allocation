# sim/hungarian_allocator.py

import numpy as np
from scipy.optimize import linear_sum_assignment
from a_star import a_star_search

def hungarian_task_allocation(grid, robots, tasks):
    """
    Optimal task allocation using Hungarian Algorithm.
    Each robot is assigned at most one task.
    """

    num_robots = len(robots)
    num_tasks = len(tasks)

    size = max(num_robots, num_tasks)
    cost_matrix = np.full((size, size), fill_value=1000)

    for i, robot in enumerate(robots):
        for j, task in enumerate(tasks):
            path = a_star_search(grid, robot.position, task)
            if path:
                cost_matrix[i][j] = len(path) - 1

    row_ind, col_ind = linear_sum_assignment(cost_matrix)

    for r, c in zip(row_ind, col_ind):
        if r < num_robots and c < num_tasks:
            robots[r].assign_task(tasks[c], cost_matrix[r][c])

    return robots
