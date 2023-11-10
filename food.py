from turtle import Turtle
import random

class Food(Turtle):
   def __init__(self):
     super().__init__()

     self.shape("turtle")
     self.color("brown")
     self.penup()
     self.shapesize(stretch_len=0.75, stretch_wid=0.75)
     self.refresh()

   def refresh(self):
     self.new_x = random.randint(-640 ,640)
     self.new_y = random.randint(-640, 640)
     self.goto(self.new_x, self.new_y)

