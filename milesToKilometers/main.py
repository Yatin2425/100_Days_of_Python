from tkinter import *


def poundsTOkg():
    pounds = float(pounds_input.get())
    kg = int(pounds/2.2)
    result_label.config(text=f"{kg}")


window = Tk()
window.title("Pounds to kg converter. ")
window.config(padx=20, pady=20)

pounds_input = Entry(width=5)
pounds_input.grid(column=1, row=0)

pounds_label = Label(text="Pounds")
pounds_label.grid(column=2, row=0)


is_equal = Label(text="is equal to")
is_equal.grid(column=0, row=1)

result_label = Label(text="result")
result_label.grid(column=1, row=1)

kg_label = Label(text="kg")
kg_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=poundsTOkg)
calculate_button.grid(column=1, row=2)

window.mainloop()
