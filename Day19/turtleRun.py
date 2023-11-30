import turtle
import random

def setup_turtle(color, x, y):
    t = turtle.Turtle()
    t.shape("turtle")
    t.color(color)
    t.speed(0)
    t.penup()
    t.goto(x, y)
    return t

def race():
    colors = ["red", "blue", "green", "orange", "purple", "brown"]
    turtles = []

    # Set up turtles
    for i in range(6):
        turtles.append(setup_turtle(colors[i], -250, 100 - i * 40))

    # User bet
    user_bet = turtle.textinput("Turtle Race", "Enter the color you bet on:").lower()

    # Race
    winner = None
    for _ in range(100):
        for t in turtles:
            speed = random.randint(1, 10)
            t.speed(speed)
            t.forward(random.randint(1, 5))

            if t.xcor() > 230:
                winner = t.color()[0]
                break

    # Announce winner
    turtle.goto(0, 0)
    turtle.write(f"The winner is the {winner} turtle!", align="center", font=("Arial", 16, "normal"))

    # Check user bet
    if user_bet == winner:
        turtle.write("Congratulations! You won!", align="center", font=("Arial", 16, "normal"))
    else:
        turtle.write("Sorry, you lost. Better luck next time!", align="center", font=("Arial", 16, "normal"))

    turtle.done()

# Run the race
race()
