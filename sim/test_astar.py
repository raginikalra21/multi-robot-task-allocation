# sim/test_astar.py

from grid import GridWorld
from a_star import a_star_search

def main():
    obstacles = {
        (1, 1), (1, 2), (1, 3),
        (3, 3), (4, 3)
    }

    grid = GridWorld(width=6, height=6, obstacles=obstacles)

    start = (0, 0)
    goal = (5, 5)

    path = a_star_search(grid, start, goal)

    print("Path found:")
    print(path)

if __name__ == "__main__":
    main()
