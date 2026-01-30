import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square():
 for i in range(4):
    t.forward(100)
    t.left(90) 

""" def triangle():
   for i in range(3):
     t.forward(100)
     t.left(120)
   """
def littlesomething (irange):
  t.speed(100)
  length=50
  for i in range(60):
    t.forward(100)
    t.left(90)
    t.left(5)

""" def squares(irange):
  length=50
  for i in range(irange):
    t.forward(100)
    t.left(90)
    t.left(5)
    t.forward(5)
    length += 25 """
def addSquares(iRange):
    length = 25
    for i in range(iRange):
        square(length, 90)
        length += 25
addSquares(5)


    






turtle.done()
