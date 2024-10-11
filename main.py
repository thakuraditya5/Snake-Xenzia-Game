from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
food= Food()
scoreboard = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

game_is_on = True

# Register the key event listeners outside the loop
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect contact with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        scoreboard.update_scoreboard()
        food.refresh()
        snake.extend()



    #detect collision with the wall
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        game_is_on=False
        scoreboard.game_over()


    #detect collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
