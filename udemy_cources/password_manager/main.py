from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    password_list.extend([random.choice(letters) for _ in range(random.randint(8, 10))])
    password_list.extend([random.choice(symbols) for _ in range(random.randint(2, 4))])
    password_list.extend([random.choice(numbers) for _ in range(random.randint(2, 4))])

    random.shuffle(password_list)

    password = "".join(char for char in password_list)
    pyperclip.copy(password)
    entry_password.delete(0, END)
    entry_password.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = entry_website.get()
    user = entry_user.get()
    password = entry_password.get()
    new_data = {
        website: {
            "email": user,
            "password": password,
        }
    }

    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                          f"Email: {user}\nPassword: {password}\n"
                                                          f"Is it ok to save?")

    if len(website) == 0 or len(password) == 0:
        messagebox.showerror(message="Don`t leave fields open")
        return
    if is_ok:
        try:
            with open("data.json", mode="r") as f:
                data = json.load(f)
        except FileNotFoundError:
            with open("data.json", mode="w") as f:
                json.dump(new_data, f, indent=4)
        else:
            data.update(new_data)
            with open("data.json", mode="w") as f:
                json.dump(data, f, indent=4)
        finally:
            entry_website.delete(0, END)
            entry_user.delete(0, END)
            entry_user.insert(0, "default@email.com")
            entry_password.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = entry_website.get()
    try:
        with open("data.json", mode="r") as f:
            data = json.load(f)
            messagebox.showinfo(title=website,
                                message=f"email: {data[website]['email']} \npassword: {data[website]['password']}\n")
    except FileNotFoundError:
        messagebox.showerror(message="Password file does not exist.")
    except KeyError:
        messagebox.showerror(message="No such password")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Passwords Manager")
window.config(bg="white", padx=20, pady=20)

canvas = Canvas()
logo_image = PhotoImage(file="logo.png")
canvas.config(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

label_website = Label(text="Website:", bg="white")
label_website.grid(row=1, column=0, sticky="ew")
label_user = Label(text="Email/Username:", bg="white")
label_user.grid(row=2, column=0, sticky="ew")
label_password = Label(text="Password:", bg="white")
label_password.grid(row=3, column=0, sticky="ew")

entry_website = Entry()
entry_website.grid(row=1, column=1, sticky="ew")
entry_user = Entry()
entry_user.insert(0, "default@email.com")
entry_user.grid(row=2, column=1, columnspan=2, sticky="ew")
entry_password = Entry()
entry_password.grid(row=3, column=1, sticky="ew")

btn_search = Button(text="Search", bg="white", command=search)
btn_search.grid(row=1, column=2, sticky="ew")
btn_generate = Button(text="Generate Password", bg="white", command=generate_password)
btn_generate.grid(row=3, column=2, sticky="ew")
btn_add = Button(text="Add", bg="white", width=36, command=save)
btn_add.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
