import pygame as pg

class Player():
    WIDTH, HEIGHT = 25, 25

    def __init__(self, x, y, color, dt) -> None:
        self.x = x
        self.y = y
        self.vel = 0
        self.COLOR = color
        self.JUMP_HEIGHT = 400
        self.GRAVITY = 1200
        self.destructed = False
        self.dt = dt

    def draw(self, win):
        if not self.destructed:
            self.player_rect = pg.Rect(self.x, self.y, self.WIDTH, self.HEIGHT)
            pg.draw.rect(win, self.COLOR, self.player_rect)


    jump_pressed = False
    def handle_movement(self, keys):
        if not self.destructed:
            # apply gravity
            self.vel += self.GRAVITY * self.dt
            # check for jump
            if keys[pg.K_SPACE] and not self.jump_pressed:
                self.vel = -self.JUMP_HEIGHT
                self.jump_pressed = True
            elif not keys[pg.K_SPACE]:
                self.jump_pressed = False
            # apply vel to pos
            self.y += self.vel * self.dt
        else:
            self.return_death_state()


    def return_death_state(self):
        return self.destructed