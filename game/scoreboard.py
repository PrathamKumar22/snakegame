from turtle import Turtle, Screen

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()
        self.screen = Screen()
        self.restart_text = Turtle()
        self.restart_text.hideturtle()
        self.restart_text.color("white")
        self.restart_text.penup()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER\nPress SPACE to Restart", align="center", font=("Arial", 14, "bold"))


    def show_restart(self):
        self.restart_text.goto(0, -40)
        self.restart_text.write("Click anywhere to RESTART", align="center", font=("Arial", 18, "normal"))
        self.screen.onclick(self.restart_game)

    def restart_game(self, x, y):
        self.screen.bye()  # Close the current turtle window
        import os
        os.system("python main.py")  # Restart the game by running main.py again
