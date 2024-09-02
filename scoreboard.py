from turtle import Turtle

FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lvl = 1
        self.hideturtle()
        self.pencolor("white")
        self.penup()
        self.goto(-290, -290)

    # method to increase level count, when player object reaches top border
    def show_score(self):
        self.write(f"Level: {self.lvl}", move=False, align='left', font=FONT)

    def reset_position(self):
        self.lvl = 1
        self.goto(-290, -290)

    def increase_level(self):
        self.lvl += 1
        self.clear()
        self.show_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", move=False, align='center', font=("Courier", 26, "bold"))
