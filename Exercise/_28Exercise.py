# Draw regular 7- and 9-sided polygons, and their star equivalents 
from turtle import *

t3 = Turtle()
t3.color('pink')

for i in range(7):
    t3.forward(100)
    t3.left(51.42)


t4 = Turtle()
t4.color('skyblue')

for i in  range(9):
    t4.forward(100)
    t4.right(40)

