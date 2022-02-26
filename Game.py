import pygame as pg
pg.init()
import time

from handling.DeltaTime import DeltaTime
from screens.StartScreen import StartScreen
from screens.DeathScreen import DeathScreen
from objects.Player import Player
from objects.Obstacle import Obstacle, randomize_pos
from handling.Movement import Movement
from handling.Collisions import Collisions

WWIDTH = 360
WHEIGHT = 640

WIN = pg.display.set_mode((WWIDTH, WHEIGHT))
pg.display.set_caption('flep :)')

FONT = './fonts/Poppins-Regular.ttf'
SCORE_FONT = pg.font.Font(FONT, 320)

WHITE = (255, 255, 255)
GREY = (195, 195, 195)
BLACK = (0, 0, 0)

CREATEOBSTACLE = pg.USEREVENT + 1
pg.time.set_timer(CREATEOBSTACLE, 1500)

class Game:
    def __init__(self) -> None:
        self.prev_time = time.time()
        self.dt = None
        self.run = False
        self.game_started = False
        self.obstacles = []
        self.score = 0

    def run_game(self):
        self.run = True
        self.main()

    def instanciate_obstacle(self):
        self.obstacles.append(Obstacle(WWIDTH, WHEIGHT, BLACK, GREY, randomize_pos(), self.dt))

    def lose(self):
        self.player.destructed = True
        for obstacle in self.obstacles:
            if not obstacle.destructed:
                obstacle.destructed = True
        

    def draw(self, win):
        # background
        win.fill(GREY)

        if self.game_started:
            if not self.player.return_death_state():
                # obstacle score rect first so its invisble
                for obstacle in self.obstacles:
                    obstacle.draw_score_rect(WIN)

                # score
                score_text = SCORE_FONT.render(str(self.collisions.return_score()), 1, WHITE)
                win.blit(score_text, (((WWIDTH//2)-(score_text.get_width()//2)), (WHEIGHT//2)-(score_text.get_height()//2)))

                # obstacles
                for obstacle in self.obstacles:
                    obstacle.draw(WIN)

                # player
                self.player.draw(WIN)
            else:
                self.death_screen.draw(WIN)
        
        else:
            self.start_screen.draw(WIN)

        pg.display.update()


    def main(self):
        if not self.game_started:
            self.start_screen = StartScreen(self.game_started, WWIDTH, WHEIGHT, FONT, BLACK)
        self.death_screen = DeathScreen(WWIDTH, WHEIGHT, FONT, BLACK)

        self.player = Player((WWIDTH//5)-(Player.WIDTH//2), (WHEIGHT//2)-(Player.HEIGHT//2), BLACK , self.dt)
        self.deltatime = DeltaTime(self.dt, self.prev_time, self.player, self.obstacles)
        self.collisions = Collisions(self.obstacles, self.player, self.lose, self.score, WHEIGHT)

        while self.run:
            self.deltatime.handle_dt()
            self.deltatime.set_dt()

            self.draw(WIN)

            self.keys = pg.key.get_pressed()

            if not self.player.return_death_state():
                if self.game_started:
                    Movement(self.keys, self.player, self.obstacles).handle_movement()

                    self.collisions.handle_collisions()

                if not self.game_started:
                    self.start_screen.wait_for_keypress(self.keys)
                    if self.start_screen.return_start_state():
                        self.game_started = self.start_screen.return_start_state()
            else:
                self.death_screen.wait_for_keypress(self.keys)
                if self.death_screen.return_restart_state():
                    self.player.destructed = False
                    for obstacle in self.obstacles:
                        obstacle.destructed = True
                    self.death_screen.restart = False
                    self.collisions.score = 0
                    self.player.x = (WWIDTH//5)-(Player.WIDTH//2)
                    self.player.y = (WHEIGHT//2)-(Player.HEIGHT//2)
            

            # closing window
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.run = False
                    break
                if self.game_started:
                    if event.type == CREATEOBSTACLE:
                        self.instanciate_obstacle()
            

if __name__ == '__main__':
    Game().run_game()