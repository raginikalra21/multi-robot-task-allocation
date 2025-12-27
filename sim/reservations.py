# sim/reservations.py

from collections import defaultdict

class ReservationTable:
    def __init__(self):
        self.vertex = defaultdict(set)  # (x, y) -> set(time)
        self.edge = set()  # ((x1,y1),(x2,y2),t)

    def reserve_path(self, path):
        for t in range(len(path)):
            self.vertex[path[t]].add(t)
            if t > 0:
                self.edge.add((path[t-1], path[t], t))

    def is_vertex_conflict(self, pos, t):
        return t in self.vertex[pos]

    def is_edge_conflict(self, prev, curr, t):
        return (curr, prev, t) in self.edge
