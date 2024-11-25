from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(0, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    Password_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = web_entry.get()
    email = Email_entry.get()
    password = Password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any field empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # json.dump(new_data, data_file, indent=4)
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # updating jason file data
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            Password_entry.delete(0, END)


# ---------------------------- Find Password ------------------------------- #
def find_password():
    website = web_entry.get()
    try:
        with open("data.json")as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="website", message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message="No details found")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("My Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# Label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
Email_label = Label(text="Email/Username:")
Email_label.grid(column=0, row=2)
Password_label = Label(text="Password:")
Password_label.grid(column=0, row=3)

# entry
web_entry = Entry(width=38)
web_entry.grid(row=1, column=1, columnspan=1)
web_entry.focus()
Email_entry = Entry(width=38)
Email_entry.grid(row=2, column=1, columnspan=1)
Email_entry.insert(0, "akash@gmail.com")
Password_entry = Entry(width=38)
Password_entry.grid(column=1, row=3)

# Button
Search_button = Button(text="Search",width=14, command=find_password)
Search_button.grid(column=2, row=1)
Generate_button = Button(text="Generate Password", command=generate_password)
Generate_button.grid(column=2, row=3)
Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(column=1, row=4, columnspan=2, )

window.mainloop()
