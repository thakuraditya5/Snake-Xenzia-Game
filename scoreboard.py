from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score =0
        self.penup()
        self.color("white")
        self.goto(x=0,y=250)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)


    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"GAME OVER. Score: {self.score}", align=ALIGNMENT, font=FONT)
