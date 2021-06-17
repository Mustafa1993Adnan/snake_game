from turtle import Turtle

STARING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segmentsList = []
        self.create_snake()
        self.snakeHead = self.segmentsList[0]

    def create_snake(self):
        for position in STARING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('white')
            new_segment.goto(position)
            self.segmentsList.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segmentsList) - 1, 0, -1):
            new_x = self.segmentsList[seg_num - 1].xcor()
            new_y = self.segmentsList[seg_num - 1].ycor()
            self.segmentsList[seg_num].goto(new_x, new_y)
        self.snakeHead.forward(MOVE_DISTANCE)

    def up(self):
        if self.snakeHead.heading() != DOWN:
            self.snakeHead.setheading(UP)

    def down(self):
        if self.snakeHead.heading() != UP:
            self.snakeHead.setheading(DOWN)

    def left(self):
        if self.snakeHead.heading() != RIGHT:
            self.snakeHead.setheading(LEFT)

    def right(self):
        if self.snakeHead.heading() != LEFT:
            self.snakeHead.setheading(RIGHT)
