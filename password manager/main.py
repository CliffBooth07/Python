from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def password_gen():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letter = [random.choice(letters) for _ in range(nr_letters)]
    symbol = [random.choice(symbols) for _ in range(nr_symbols)]
    number = [random.choice(numbers) for _ in range(nr_numbers)]
    password_list = letter + symbol + number

    random.shuffle(password_list)
    password = "".join(password_list)
    placeholder3.insert(0, password)
    pyperclip.copy(password)
    messagebox.showinfo(title="PM", message="Password Copy to your Clipboard")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    site = placeholder1.get()
    mail = placeholder2.get()
    password = placeholder3.get()
    new_data = {
        site: {
            "email": mail,
            "password": password
        }
    }
    if len(site) == 0 or len(password) == 0 or len(password) == 0:
        messagebox.showerror(title="PM", message="Give relevant input")
    else:
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)

    placeholder1.delete(0, "end")
    placeholder3.delete(0, "end")


#----------------------------- SEARCH ----------------------------------#

def search():
    web = placeholder1.get()
    # print(web)
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            print(data)
    except FileNotFoundError:
        messagebox.showerror(title="PM", message="No data file found")
    else:
        if web in data:
            messagebox.showinfo(title=web,
                                message=f"Email: {data[web]['email']}\nPassword: {data[web]['password']}")
        else:
            messagebox.showerror(title="PM", message=f"No detail for the {web} exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

label1 = Label(text="Website:")
label1.grid(row=1, column=0)
label2 = Label(text="Email/Username:")
label2.grid(row=2, column=0)
label3 = Label(text="Password:")
label3.grid(row=3, column=0)

placeholder1 = Entry(width=33)
placeholder1.grid(row=1, column=1)
placeholder1.focus()
placeholder2 = Entry(width=52)
placeholder2.grid(row=2, column=1, columnspan=2)
placeholder2.insert(0, "yourmail@.mail.com")
placeholder3 = Entry(width=33)
placeholder3.grid(row=3, column=1)

button1 = Button(text="Generate Password", command=password_gen)
button1.grid(row=3, column=2)
button2 = Button(text="Add", width=44, command=save)
button2.grid(row=4, column=1, columnspan=2)
button3 = Button(text="Search", width=15, command=search)
button3.grid(row=1, column=2)

window.mainloop()
