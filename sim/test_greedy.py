# sim/test_greedy.py

from grid import GridWorld
from robot import Robot
from task_allocator import greedy_task_allocation
from metrics import compute_metrics
from logger import log_results

def main():
    obstacles = {(2,2), (2,3), (3,2)}
    grid = GridWorld(width=6, height=6, obstacles=obstacles)

    robots = [
        Robot(robot_id=1, start_pos=(0, 0)),
        Robot(robot_id=2, start_pos=(5, 0))
    ]

    tasks = [(1, 5), (4, 5), (5, 5)]

    robots = greedy_task_allocation(grid, robots, tasks)

    metrics = compute_metrics(robots)

    print("Metrics:", metrics)

    log_results(
        filename="results/greedy_results.csv",
        algorithm="load_aware_greedy",
        num_robots=len(robots),
        num_tasks=len(tasks),
        metrics=metrics
    )

if __name__ == "__main__":
    main()
