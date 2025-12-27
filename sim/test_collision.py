# sim/test_collision.py

from grid import GridWorld
from robot import Robot
from collision_planner import plan_paths_collision_aware

def main():
    grid = GridWorld(6, 6, {(2,2), (2,3), (3,2)})

    robots = [
        Robot(1, (0,0)),
        Robot(2, (0,1))
    ]

    tasks = [(5,5), (5,4)]

    paths = plan_paths_collision_aware(grid, robots, tasks)

    for rid, path in paths.items():
        print(f"Robot {rid}: {path}")

if __name__ == "__main__":
    main()
