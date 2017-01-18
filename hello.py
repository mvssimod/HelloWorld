# connect the Turtle and random libraries (aka "modules")
import turtle, random

# let's make a turtle
tina = turtle.Turtle()
tina.speed(1000)

# list of colors
colors = ["pink", "blue", "yellow", "green", "silver", "red", "turquoise", "orange", "purple"]


# random color picker
def color_tina():
    pick = random.randint(0, len(colors) - 1)
    tina.color(colors[pick])


def triangle(size):
    color_tina()
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.right(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)
    tina.left(120)
    tina.forward(size)

    tina.pendown()


tina.goto(-150, 150)
tina.pendown
for x in range(10, 100, 5):
    triangle(x)

tina.pendown()
tina.goto(150, 150)
tina.pendown
for x in range(10, 100, 5):
    triangle(x)

tina.pendown()
tina.goto(-150, -150)
tina.pendown
for x in range(10, 100, 5):
    triangle(x)

tina.pendown()
tina.goto(150, -150)
tina.pendown
for x in range(10, 100, 5):
    triangle(x)

tina.pendown()
tina.goto(-150, 150)
tina.pendown
for x in range(10, 100, 5):
    triangle(x)


# draw octagon
def octagon(size):
    color_tina()
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)
    tina.right(60)
    tina.forward(size)


# repeating octagons
def octagons(size, num):
    for x in range(1, num):
        octagon(size * x)


# let's make some methods, like plays in a playbook
def square(some_turtle):
    # stop writing
    some_turtle.penup()
    # go to the middle
    some_turtle.goto(0, 0)
    # start writing
    some_turtle.pendown()
    # go up
    some_turtle.goto(0, 50)
    # go right
    some_turtle.goto(50, 50)
    # go down
    some_turtle.goto(50, 0)
    # go back to the start
    some_turtle.goto(0, 0)


# draw a series of circles, size = size of first circle
def super_circles(size):
    for x in range(1, 11):
        color_tina()
        tina.circle(size * x)


# let's draw a circle in the middle
tina.goto(0, 0)
tina.circle(25)
tina.goto(0, 0)
tina.circle(-25)
super_circles(5)

tina.goto(0, 0)
tina.circle(-25)
tina.goto(0, 0)
tina.circle(25)
super_circles(5)

# let's make tina draw that square
# she'll fill in the spot of "some_turtle"
square(tina)

# let's draw a circle in the middle
tina.goto(25, 0)
tina.circle(25)

# call my fancy new functions
super_circles(5)
triangle(60)

triangle(55)
super_circles(5)

tina.penup()
triangle(60)
tina.goto(100, 100)
tina.pendown()
for x in range(10, 100, 5):
    triangle(x)

tina.penup()
tina.goto(-100, -100)
tina.pendown()
for x in range(-10, -100, -5):
    triangle(x)

# Conditional Statement
answer = input("What next?")
print("You just said this: " + answer)

if True:
    print("Great job!")