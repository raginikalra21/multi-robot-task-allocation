# sim/auction_allocator.py

from a_star import a_star_search

def auction_task_allocation(grid, robots, tasks):
    """
    Auction-based task allocation.
    Each robot bids for a task based on (distance + current workload).
    Lowest bid wins the task.
    """

    for task in tasks:
        best_robot = None
        lowest_bid = float("inf")
        best_distance = 0

        for robot in robots:
            path = a_star_search(grid, robot.position, task)
            if path is None:
                continue

            distance = len(path) - 1
            bid = distance + robot.total_distance  # bid function

            if bid < lowest_bid:
                lowest_bid = bid
                best_robot = robot
                best_distance = distance

        if best_robot:
            best_robot.assign_task(task, best_distance)

    return robots
