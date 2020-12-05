from turtle import Screen
from snake import Snake
from score import Score
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Best Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.050)
    snake.move()

    if snake.head.distance(food) < 15:
        food.new_location()
        score.increase_score()
        snake.extend()

    if snake.head.xcor() > 280 or \
            snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or \
            snake.head.ycor() < -280:
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False

score.clear()
food.clear()
snake.clear_snake()
score.game_over()

screen.exitonclick()
