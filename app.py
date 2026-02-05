import turtle
from turtle import *
t = Turtle()

t.shape('turtle')

def square(irange):
 for i in range(4):
    t.forward(100)
    t.left(90) 

def triangle():
   for i in range(3):
     t.forward(100)
     t.left(120)
  
def littlesomething(irange):
  length=5
  for i in range(60):
    square(length * 5)
    length += 5

littlesomething(5)
