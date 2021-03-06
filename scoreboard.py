from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 10, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Your Score = {self.score} - High Score = {self.high_score}", align=ALIGN, font=FONT)
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

        self.score=0
        self.clear()
        self.update_scoreboard()
    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game over your score is {self.score} ", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
