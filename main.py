from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('gray10')
screen.title('Retro Snake Game')
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(snake.move_speed)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        if scoreboard.score % 3 == 0:
            food.color('#C9C9C9')
            food.shapesize(stretch_len=0.5, stretch_wid=0.5)
        else:
            food.color('#76A86E')
            food.shapesize(stretch_len=0.6, stretch_wid=0.6)
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 275 or snake.head.ycor() < -285:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
