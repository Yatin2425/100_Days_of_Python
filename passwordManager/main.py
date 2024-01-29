from tkinter import *
import random
import json
from tkinter import messagebox

#functions
file_path = "/Users/yatintyagi/Desktop/passwords/passwords.JSON"
def save():
    email=Email_entry.get()
    website=website_entry.get()
    passs=Password_entry.get()
    new_data = {
        website: {
            "email": email , 
            "password": passs
        }
    }
    
    try:
        with open(file_path, "r") as f:
            data = json.load(f)
    except FileNotFoundError:
        with open(file_path, "w") as f:
            json.dump(new_data, f, indent=4)
    else:
        data.update(new_data)
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        
    Email_entry.delete(0, 'end')
    website_entry.delete(0, 'end')
    Password_entry.delete(0, 'end')
    
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    a=10
    b=5
    c=5 
    password=''
    password_list = []

    for char in range(1, a + 1):
        password_list.append(random.choice(letters))

    for char in range(1, b + 1):
        password_list += random.choice(symbols)

    for char in range(1, c + 1):
        password_list += random.choice(numbers)


    random.shuffle(password_list)


    password = ""
    for char in password_list:
        password += char
    Password_entry.insert(0,password)

def searchPwd():
    website = website_entry.get()
    with open(file_path,"r") as f:
        data=json.load(f)
        if website in data:
            email = data[website]["email"]
            passs = data[website]["password"]
            messagebox.showinfo(title = website , message = f"Email = {email} \n Password = {passs}")
        
    
        


    


window = Tk()
window.title("Password manager")
window.config(padx=50, pady=50)
img = PhotoImage(file="lock.png")
canvas = Canvas(height=400 , width=400 )
canvas.create_image(200 , 200 , image=img)
canvas.grid(column=1, row=0)

#labels
website_label = Label(text="Website")
website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username")
Email_label.grid(column=0, row=2)
Password = Label(text="Password")
Password.grid(column=0, row=3)

#buttons
Generate = Button(text="Generate password" , width= 25 , command=generate)
Generate.grid(column=2, row=3)
add = Button(text="Add" ,width=36 , command= save)
add.grid(column=1, row=4 ,columnspan= 2)
search_button = Button(text="Search" , width=25 , command= searchPwd)
search_button.grid(column=2 , row=1)

#text Field
website_entry = Entry(width=35)
website_entry.grid(column=1 , row=1)
website_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(column=1 , row=2)
Email_entry.insert(0 , "yatintyagi2425@gmail.com")
Password_entry = Entry(width=21)
Password_entry.grid(column=1 , row=3)


    
















window.mainloop()