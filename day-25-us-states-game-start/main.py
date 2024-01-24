import turtle as t
import pandas as pd

correct_count = 0 

screen = t.Screen()
screen.title("States game")
image = "blank_states_img.gif"
screen.addshape(image)

t.shape(image)

data=pd.read_csv("50_states.csv")

state_name = set(data["state"])
guessed_state = set()

while correct_count <50:
    answer_state = screen.textinput(title=f"{correct_count}/50 Guess the state", prompt="What another state name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in state_name :
        
        if answer_state not in guessed_state:
                    print(answer_state)
                    correct_count += 1
                    state_data= data[data.state == answer_state]
                    tim= t.Turtle()
                    tim.hideturtle()
                    tim.penup()
                    tim.color("black")
                    tim.goto(int(state_data.x) , int(state_data.y))
                    tim.write(answer_state.title())
                    print(state_data)
                    guessed_state.add("answer_state.title()")

  


 
