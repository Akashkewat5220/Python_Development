from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


#Password Generator Project
def generate_password():
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message = "Please don't leave any field empty")
    else:
        ok=messagebox.askokcancel(title=website, message=f"These are the detail entered: \nEmail: {email}"
                               f"\n Password: {password} \n Is it ok to save?")

        if ok:
            data_file = open("data.txt", "a")
            data_file.write(f"{website} | {email} | {password}\n")
            web_entry.delete(0, END)
            Password_entry.delete(0, END)


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
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()
Email_entry = Entry(width=35)
Email_entry.grid(column=1, row=2,  columnspan=2)
Email_entry.insert(0, "akash@gmail.com")
Password_entry = Entry(width=21)
Password_entry.grid(column=1, row=3)


# Button
Generate_button = Button(text="Generate Password", command=generate_password)
Generate_button.grid(column=2, row=3)
Add_button = Button(text="Add", width=36, command=save)
Add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()


