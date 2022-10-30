from turtle import Turtle


class Scoreboard(Turtle):
    """
    This class inherits from the super class Turtle and it will allow us to track the score and show a message of
    "Game Over" on screen when game is over.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()
        self.update_current_score()

    def update_current_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Roboto", 15, "normal"))

    def add_score(self):
        self.score += 1
        self.update_current_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_current_score()


