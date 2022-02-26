import pygame as pg

class StartScreen:
    def __init__(self, game_started, wwidth, wheight, font, color) -> None:
        self.game_started = game_started
        self.wwidth = wwidth
        self.wheight = wheight
        self.font = font
        self.color = color
        self.title_size = 96
        self.hint_size = 24

    def draw(self, win):
        # title text
        title_font = pg.font.Font(self.font, self.title_size)
        title_text = title_font.render('flep :)', 1, self.color)
        win.blit(title_text, (((self.wwidth//2)-(title_text.get_width()//2)), (self.wheight//2)-(title_text.get_height())))

        # hint text
        hint_font = pg.font.Font(self.font, self.hint_size)
        hint_text = hint_font.render('press SPACE to flep', 1, self.color)
        win.blit(hint_text, ((self.wwidth//2)-(hint_text.get_width()//2), (self.wheight//1.5)-(hint_text.get_height()//4)))


    def wait_for_keypress(self, keys):
        if keys[pg.K_SPACE]:
            self.game_started = True
    
    def return_start_state(self):
        return self.game_started