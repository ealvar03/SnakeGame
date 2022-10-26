from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

if __name__ == '__main__':
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake Game in Python")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    score = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect a collision with the food using distance method from turtle
        if snake.segments[0].distance(food) < 15:
            food.refresh_food_point()
            snake.extend()
            score.add_score()

        # Detect a collision with the wall
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280\
                or snake.segments[0].ycor() < -280:
            game_is_on = False
            score.game_is_over()

        # Detect collision with the tail
        for segment in snake.segments[1:]:
            if snake.segments[0].distance(segment) < 10:
                game_is_on = False
                score.game_is_over()

    screen.exitonclick()
