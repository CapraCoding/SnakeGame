from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.turtle_list = []
        self.create_snake()
        self.head = self.turtle_list[0]


    def create_snake(self):
        for positions in starting_positions:
            self.get_bigger(positions)

        return self.turtle_list

    def move(self):
        for seg_num in range(len(self.turtle_list) - 1, 0, -1):
            new_x = self.turtle_list[seg_num - 1].xcor()
            new_y = self.turtle_list[seg_num - 1].ycor()
            self.turtle_list[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.get_bigger(self.turtle_list[-1].position())

    def get_bigger(self,position):
        turtle = Turtle(shape='square')
        turtle.color('white')
        turtle.penup()
        turtle.goto(position)
        self.turtle_list.append(turtle)

    def reset(self):
        for segment in self.turtle_list:
            segment.goto(1000,1000)
        self.turtle_list.clear()
        self.create_snake()
        self.head = self.turtle_list[0]
