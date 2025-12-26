# sim/metrics.py

def compute_metrics(robots):
    distances = [robot.total_distance for robot in robots]

    total_distance = sum(distances)
    makespan = max(distances) if distances else 0
    idle_time = makespan * len(robots) - total_distance

    return {
        "total_distance": total_distance,
        "makespan": makespan,
        "idle_time": idle_time
    }
