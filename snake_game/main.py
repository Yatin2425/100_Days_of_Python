from turtle import Screen, Turtle
import time


screen = Screen()
screen.setup(width= 600 ,height=600)
screen.bgcolor("black")
screen.title('My Snake Game')
screen.tracer(0)

starting_positions=[(0,0),(-20,0),(-40,0)]
segements=[]

for position in starting_positions:
    new_segement=Turtle("square")
    new_segement.color("white")
    new_segement.penup()
    new_segement.goto(position)
    segements.append(new_segement)

    
game_is_on=True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segements:
        seg.forward(20)
    
        
    




















screen.exitonclick()




