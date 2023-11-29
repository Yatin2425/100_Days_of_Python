#just a boring code
import turtle

# Set up the turtle
t = turtle.Turtle()
t.speed("fastest")
t.color("red")
t.fillcolor("red")

# Move to starting position
t.penup()
t.goto(0, -200)
t.pendown()

# Draw heart shape
t.begin_fill()
t.left(140)
t.forward(224)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.left(120)
for _ in range(200):
    t.right(1)
    t.forward(2)
t.forward(224)
t.end_fill()

# Hide the turtle
t.hideturtle()

# Keep the window open
turtle.done()
