from turtle import Turtle

STARING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segmentsList = []
        self.create_snake()

    def create_snake(self):
        for position in STARING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.penup()
            new_segment.color('red')
            new_segment.goto(position)
            self.segmentsList.append(new_segment)

    def move(self):
        for seg_num in range(len(self.segmentsList) - 1, 0, -1):
            new_x = self.segmentsList[seg_num - 1].xcor()
            new_y = self.segmentsList[seg_num - 1].ycor()
            self.segmentsList[seg_num].goto(new_x, new_y)
        self.segmentsList[0].forward(MOVE_DISTANCE)

    def up(self):
        self.segmentsList[0].setheading(90)

    def down(self):
        self.segmentsList[0].setheading(270)

    def left(self):
        self.segmentsList[0].setheading(180)

    def right(self):
        self.segmentsList[0].setheading(0)
