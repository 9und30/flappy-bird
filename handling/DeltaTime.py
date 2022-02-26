import time

class DeltaTime:
    def __init__(self, dt, prev_time, player, obstacles) -> None:
        self.dt = dt
        self.prev_time = prev_time
        self.player = player
        self.obstacles = obstacles


    def handle_dt(self):
        self.dt = time.time() - self.prev_time
        self.prev_time = time.time()

    def set_dt(self):
        self.player.dt = self.dt
        for obstacle in self.obstacles:
            obstacle.dt = self.dt