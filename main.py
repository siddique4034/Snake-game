from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("grey")
screen.title("Kobra game")
screen.setup(width=650, height=650)
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True

while is_game_on:
  screen.update()
  time.sleep(0.5)

  snake.move()

  if snake.head.distance(food) < 15:
    food.refresh()
    snake.extend()
    score.score_increase()

  if snake.head.xcor() > 305 or snake.head.xcor() < -305 or snake.head.ycor() > 305 or snake.head.ycor() < -305:
    is_game_on = False
    score.game_over()

  for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
