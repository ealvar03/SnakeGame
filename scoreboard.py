from turtle import Turtle


class Scoreboard(Turtle):
    """
    This class inherits from the super class Turtle and it will allow us to track the score and show a message of
    "Game Over" on screen when game is over.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.update_current_score()

    def update_current_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Roboto", 15, "normal"))

    def add_score(self):
        self.score += 1
        self.clear()
        self.update_current_score()

    def game_is_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Roboto", 15, "normal"))

