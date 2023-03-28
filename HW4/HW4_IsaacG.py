"""
Isaac Guerrero
CS 100 
Section 015
HW 04
September 26, 2021
"""
import turtle
import math
# 1
a = 3
b = 4
c = 5

print("#1")
if a < b:
    print("ok")
if c < b:
    print("ok")
if a+b == c:
    print("ok")
if math.sqrt(a) + math.sqrt(b) == math.sqrt(c):
    print("ok")

print("#2")
if a < b:
    print("OK")
else:
    print("NOT OK")

if c < b:
    print("OK")
else:
    print("NOT OK")

if a + b == c:
    print("OK")
else:
    print("NOT OK")

if a**2 + b**2 == c**2:
    print("OK")
else:
    print("NOT OK")


print("#3")
color = input("What color? ")
line_width = int(input("What line width? "))
line_length = int(input("What line length? "))
shape = input("Line, triangle or square? ")

t = turtle.Turtle()
t.pensize(line_width)
t.color(color)

if shape == "line":
    t.forward(line_length)
elif shape == "triangle":
    for i in range(3):
        t.forward(line_length)
        t.left(120)
elif shape == "square":
    for i in range(4):
        t.forward(line_length)
        t.left(90)
else:
    print("Invalid shape specified")

turtle.done()
