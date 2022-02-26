class Collisions:
    def __init__(self, obstacles, player, lose, score, WHEIGHT) -> None:
        self.obstacles = obstacles
        self.player = player
        self.lose = lose
        self.score = score
        self.WHEIGHT = WHEIGHT

    def handle_collisions(self):
        for obstacle in self.obstacles:
            if not obstacle.destructed:
                for i, obstacle_rect in enumerate(obstacle.return_rects()):
                    if (self.player.player_rect.colliderect(obstacle_rect) and (i == 0 or i == 1)) or self.player.y > self.WHEIGHT or self.player.y < 0 - self.player.HEIGHT:
                        self.lose()
                    if self.player.player_rect.colliderect(obstacle_rect) and i == 2:
                        if not obstacle.score_collected:
                            self.score += 1
                            obstacle.score_collected = True
                            print(self.score)

    def return_score(self):
        return self.score