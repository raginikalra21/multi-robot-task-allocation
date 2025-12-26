# sim/grid.py

class GridWorld:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.obstacles = obstacles if obstacles else set()

    def in_bounds(self, node):
        x, y = node
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, node):
        return node not in self.obstacles

    def neighbors(self, node):
        x, y = node
        candidates = [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1)
        ]
        results = filter(self.in_bounds, candidates)
        results = filter(self.passable, results)
        return list(results)
