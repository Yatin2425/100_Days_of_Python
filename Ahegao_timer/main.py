from tkinter import *
from PIL import ImageTk, Image
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GREY="#808080"
FONT_NAME = "Courier"
WORK_MIN = 40
SHORT_BREAK_MIN = 20
LONG_BREAK_MIN = 30
reps=0
my_timer=None 

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(my_timer)
    canvas.itemconfig(timer_text , text ="00:00")
    title_label.config(text = "Timer")
    check_marks.config(text = "")
    global reps
    reps = 0
    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_Timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    

    if reps % 8 == 0:
        countdown(long_break_sec)
        title_label.config(text = "Long break")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        title_label.config(text = "Short break")
    else:
        countdown(work_sec)
        title_label.config(text = "work for that V")
        
    
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    # if count_min == 0 and count_sec == 0:
    #     canvas.itemconfig(timer_image, image=break_img)
    if count_sec == 0:
        count_Sec="00"
    canvas.itemconfig(timer_text , text = f"{count_min}:{count_sec}" )
    if count>0:
        global my_timer
        my_timer = window.after(1000 , countdown , count - 1)
    else:
        start_Timer()
        mark = "  "
        for _ in range (math.floor(reps/2)):
            mark += "✔︎"
        check_marks.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50 , pady=50 )

title_label = Label(text="Timer" , font=(FONT_NAME ,25 ,"bold"), fg="grey")
title_label.grid(column=1,row=0)
canvas = Canvas(width = 200 , height = 224 )
img = ImageTk.PhotoImage(Image.open('timer.jpeg'))
break_img = ImageTk.PhotoImage(Image.open('Unknown.jpeg'))
timer_image=canvas.create_image(103 , 100 ,image=img)
timer_text = canvas.create_text(103 , 130 , text= "00:00" , fill = "white" , font = (FONT_NAME , 35 , "bold"))
canvas.grid(column=1,row=1)


start_button = Button(text="Start", fg=GREY , command=start_Timer)
start_button.grid(column=0,row=2)  
reset_button = Button(text="Reset", fg=GREY , command = reset_timer)
reset_button.grid(column=2,row=2)  

check_marks = Label(fg=GREY , font=(20))
check_marks.grid(column=1, row=3)


window.mainloop()

