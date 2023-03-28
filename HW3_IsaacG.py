"""
Isaac Guerrero
CS 100 Section 015
HW03, September 17, 2021
"""
import turtle
import math
aScreen = turtle.Screen()
shelly = turtle.Turtle()



shelly.forward(100)
shelly.right(120)
shelly.forward(100)
shelly.right(120)
shelly.forward(100)
shelly.right(120)

shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)
shelly.forward(100)
shelly.right(90)

shelly.forward(80)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)
shelly.right(72)
shelly.forward(100)

#Rinnegan from Naruto as my concentric circles
shelly.color("#E6E6FA")
shelly.begin_fill()
shelly.circle(200)
shelly.end_fill()
shelly.color("black")

shelly.up()
shelly.left(90)
shelly.forward(150)
shelly.right(90)
shelly.down()
shelly.circle(50)
shelly.up()
shelly.left(90)
shelly.forward(25)
shelly.right(90)
shelly.down()
shelly.begin_fill()
shelly.circle(25)
shelly.end_fill()
shelly.up()
shelly.right(90)
shelly.forward(25)
shelly.left(90)
shelly.down()
shelly.up()
shelly.right(90)
shelly.forward(50)
shelly.left(90)
shelly.down()
shelly.circle(100)
shelly.up()
shelly.right(90)
shelly.forward(50)
shelly.left(90)
shelly.down()
shelly.circle(150)
shelly.up()
shelly.right(90)
shelly.forward(50)
shelly.left(90)
shelly.down()
shelly.circle(200)


print(math.gcd(63, 49))

print(math.perm(100))

print(math.log2(1000000))
