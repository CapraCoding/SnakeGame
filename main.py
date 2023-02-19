import time
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)
food = Food()
score = Score()
snake = Snake()
game_is_on = True
screen.listen()

screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')
screen.onkey(fun=exit, key='Escape')

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if (snake.head.xcor() >= 500 or snake.head.xcor() <= -500) or (snake.head.ycor() > 400 or snake.head.xcor() <-400):
        game_is_on = score.game_over()

    if snake.head.distance(food) < 20:
        food.refresh()
        score.new_score(snake)
    for segment in snake.turtle_list[1:]:
        if snake.head.distance(segment.position()) < 10:
            game_is_on = score.game_over()



screen.exitonclick()
