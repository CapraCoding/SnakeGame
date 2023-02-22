from turtle import Turtle
from snake import Snake
ALIGNMENT = 'center'
FONT = 24
STYLE_TEXT = 'normal'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.highscore = None
        self.score = 0
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.color('white')
        self.get_highscore()
        self.update_score()

    def get_highscore(self):
        with open('highscore.txt', 'r+') as highscore_file:
            self.highscore = highscore_file.read()

    def update_highscore(self):
        with open('highscore.txt', 'w') as highscore_file:
            highscore_file.write(str(self.highscore))
    def reset(self):
        self.score = 0
        self.update_score()

    #def game_over(self):
    #    self.goto(0,0)
    #    self.write(f'Game Over', align='center', font=(ALIGNMENT, FONT, STYLE_TEXT))
    #    return False

    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}   HighScore = {self.highscore}', align='center', font=(ALIGNMENT, FONT, STYLE_TEXT))

    def new_score(self, snake):
        self.score += 1
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.update_highscore()
        self.update_score()
        snake.extend()
