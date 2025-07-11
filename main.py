from turtle import Screen
import time
from game.snake import Snake
from game.food import Food
from game.scoreboard import Scoreboard
from turtle import Turtle

def start_game():
    global snake, food, scoreboard, game_is_on

    screen.clear()
    screen.bgcolor("black")
    screen.title("🐍 Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    game_is_on = True
    game_loop()

def game_loop():
    global game_is_on
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()

        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        if (
            snake.head.xcor() > 280 or snake.head.xcor() < -280 or
            snake.head.ycor() > 280 or snake.head.ycor() < -280
        ):
            game_is_on = False
            end_game()

        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_is_on = False
                end_game()

def end_game():
    scoreboard.game_over()
    screen.onkey(restart_game, "space")  # Listen for SPACE to restart

def restart_game():
    screen.onkey(None, "space")  # Disable repeated trigger
    start_game()

# Initial setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Snake Game")
screen.tracer(0)

# Start the game first time
start_game()

screen.mainloop()
