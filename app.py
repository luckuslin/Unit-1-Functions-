import turtle
from turtle import *
t = Turtle()

t.shape('turtle')
def square():
 for i in range(4):
    t.forward(100)
    t.left(90)

def triangle():
   for i in range(3):
     t.forward(100)
     t.left(120)
  
def littlesomething ():
  t.speed(50)
  for i in range(60):
    t.forward(100)
    t.left(90)
    t.left(5)
  
     
littlesomething()


turtle.done()
