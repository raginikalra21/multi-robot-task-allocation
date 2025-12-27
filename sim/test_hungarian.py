# sim/test_hungarian.py

from grid import GridWorld
from robot import Robot
from hungarian_allocator import hungarian_task_allocation
from metrics import compute_metrics
from logger import log_results

def main():
    obstacles = {(2,2), (2,3), (3,2)}
    grid = GridWorld(width=6, height=6, obstacles=obstacles)

    task_sets = {
        2: [(1, 5), (4, 5)],
        3: [(1, 5), (4, 5), (5, 5)],
        4: [(1, 5), (3, 5), (4, 5), (5, 5)]
    }

    for num_tasks, tasks in task_sets.items():
        robots = [
            Robot(robot_id=1, start_pos=(0, 0)),
            Robot(robot_id=2, start_pos=(5, 0))
        ]

        robots = hungarian_task_allocation(grid, robots, tasks)
        metrics = compute_metrics(robots)

        log_results(
            filename="results/hungarian_results.csv",
            algorithm="hungarian",
            num_robots=len(robots),
            num_tasks=num_tasks,
            metrics=metrics
        )

        print(f"Hungarian | Tasks: {num_tasks} | Metrics: {metrics}")

if __name__ == "__main__":
    main()
