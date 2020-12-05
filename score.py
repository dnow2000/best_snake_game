from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.update_score()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        pass
