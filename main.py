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
    for seg in segmentsList:
        seg.forward(10)
        time.sleep(0.05)
screen.exitonclick()
