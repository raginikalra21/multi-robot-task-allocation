# sim/task_allocator.py

from a_star import a_star_search

def greedy_task_allocation(grid, robots, tasks):
    """
    Load-aware greedy task allocation.
    Chooses robot with minimum (distance + current workload).
    """
    for task in tasks:
        best_robot = None
        best_score = float("inf")
        best_distance = 0

        for robot in robots:
            path = a_star_search(grid, robot.position, task)
            if path is None:
                continue

            distance = len(path) - 1
            score = distance + robot.total_distance  # load-aware

            if score < best_score:
                best_score = score
                best_robot = robot
                best_distance = distance

        if best_robot:
            best_robot.assign_task(task, best_distance)

    return robots
