import pygame as pg

class Movement:
    def __init__(self, keys, player, obstacles) -> None:
        self.keys = keys
        self.player = player
        self. obstacles = obstacles


    def handle_movement(self):
        # player
        self.player.handle_movement(self.keys)
        # obstacles
        for obstacle in self.obstacles:
            obstacle.handle_movement()
            obstacle.check_self_destruct()