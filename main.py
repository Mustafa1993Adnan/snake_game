from turtle import Screen, Turtle
import time

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
segments = [(0, 0), (-20, 0), (-40, 0)]
segmentsList = []
for position in segments:
    new_segment = Turtle('square')
    new_segment.penup()
    new_segment.color('red')
    new_segment.goto(position)
    segmentsList.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segmentsList) - 1, 0, -1):
        new_x = segmentsList[seg_num - 1].xcor()
        new_y = segmentsList[seg_num - 1].ycor()
        segmentsList[seg_num].goto(new_x, new_y)
    segmentsList[0].forward(20)
    segmentsList[0].left(90)

screen.exitonclick()
