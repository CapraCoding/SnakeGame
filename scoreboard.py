from turtle import Turtle
ALIGNMENT = 'center'
FONT = 24
STYLE_TEXT = 'normal'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,350)
        self.hideturtle()
        self.color('white')
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align='center', font=(ALIGNMENT, FONT, STYLE_TEXT))
        return False
    def update_score(self):
        self.clear()
        self.write(f'Score = {self.score}', align='center', font=(ALIGNMENT, FONT, STYLE_TEXT))

    def new_score(self, snake):
        self.score += 1
        self.update_score()
        snake.extend()
