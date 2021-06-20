from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collision with food
    if snake.snakeHead.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.snakeHead.xcor() > 290 or snake.snakeHead.xcor() < -290 or snake.snakeHead.ycor() > 290 \
            or snake.snakeHead.ycor() < -290:
        scoreboard.game_over()
        game_is_on = False
    # detect collision with tail
    for segment in snake.segmentsList:
        if segment == snake.snakeHead:
            pass
        elif snake.snakeHead.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
screen.exitonclick()
