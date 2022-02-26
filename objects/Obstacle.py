import pygame as pg
import random

def randomize_pos():
    obstacle_offset = random.randint(-100, 100)
    return obstacle_offset

class Obstacle:
    def __init__(self, wwidth, wheight, color, transparent, offset, dt) -> None:
        self.WWIDTH = wwidth
        self.WHEIGHT = wheight
        self.WIDTH = 35
        self.HEIGHT = self.WHEIGHT // 1.5
        self.COLOR = color
        self.TRANSPARENT = transparent
        self.offset = offset
        self.x = self.WWIDTH + self.WIDTH
        self.PIPE_SPACE = 110
        self.SPEED = 145
        self.destructed = False
        self.score_collected = False
        self.dt = dt

    def draw(self, win):
        if not self.destructed:
            self.pipe_rect_1 = pg.Rect((self.x, (-(self.PIPE_SPACE)+self.offset), self.WIDTH, self.HEIGHT))
            self.pipe_rect_2 = pg.Rect((self.x, ((self.WHEIGHT//2)+(self.PIPE_SPACE)+self.offset), self.WIDTH, self.HEIGHT))
            pg.draw.rect(win, self.COLOR, self.pipe_rect_1)
            pg.draw.rect(win, self.COLOR, self.pipe_rect_2)
    
    def draw_score_rect(self, win):
        if not self.destructed:
            self.score_rect = pg.Rect((self.x+(self.WIDTH//2), ((-(self.PIPE_SPACE)+self.offset)+self.HEIGHT), 1, self.PIPE_SPACE))
            pg.draw.rect(win, self.TRANSPARENT, self.score_rect)
    

    def handle_movement(self):
        if not self.destructed:
            self.x += -self.SPEED * self.dt

    def check_self_destruct(self):
        if self.x <= 0 - self.WIDTH:
            self.destructed = True

    def return_rects(self):
        return [self.pipe_rect_1, self.pipe_rect_2, self.score_rect]