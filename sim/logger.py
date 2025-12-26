# sim/logger.py

import csv
import os

def log_results(filename, algorithm, num_robots, num_tasks, metrics):
    file_exists = os.path.isfile(filename)

    with open(filename, mode="a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow([
                "algorithm",
                "num_robots",
                "num_tasks",
                "total_distance",
                "makespan",
                "idle_time"
            ])

        writer.writerow([
            algorithm,
            num_robots,
            num_tasks,
            metrics["total_distance"],
            metrics["makespan"],
            metrics["idle_time"]
        ])
