# sim/collision_planner.py

from reservations import ReservationTable
from a_star_time import a_star_time

def plan_paths_collision_aware(grid, robots, tasks):
    reservations = ReservationTable()
    paths = {}

    for robot, task in zip(robots, tasks):
        path = a_star_time(grid, robot.position, task, reservations)
        if path is None:
            raise RuntimeError("No collision-free path found")

        reservations.reserve_path(path)
        paths[len(paths)] = path

        robot.position = path[-1]
        robot.total_distance += len(path) - 1

    return paths
