from turtle import Turtle, Screen


screen = Screen()
player_name = screen.textinput(title="Player name", prompt="Enter your name: ")
FONT = ("Courier", 20, 'normal')

class Score(Turtle):
   
   def __init__(self):

     super().__init__()
     self.score = 0
     self.penup()
     self.color("blue")
     self.hideturtle()
     self.goto(0, 310)
     self.score_update()

   def score_update(self):
     self.write(f"Player name: {player_name}\nSCORE: {self.score}", False, align="center")

   def game_over(self):
     self.goto(0, 0)
     self.write(f"GAME OVER\n{player_name}'s score: {self.score}", False, align="center", font=FONT)

   def score_increase(self):
     self.clear()
     self.score += 1
     self.score_update()
