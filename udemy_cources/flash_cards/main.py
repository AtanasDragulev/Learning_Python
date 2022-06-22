from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_word = {}

try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/en-bg.csv")
words = data.to_dict(orient="records")
print(words)


def new_word():
    global current_word
    if len(words) > 0:
        random_word = random.choice(words)
        current_word = random_word
        front(random_word["en"], random_word["bg"])
    else:
        canvas.itemconfigure(word, text="No more words", fill="black")


def remove_word():
    if current_word in words:
        words.pop(words.index(current_word))
        new_data = pandas.DataFrame(words)
        new_data.to_csv("./data/words_to_learn.csv", encoding="utf-8", index=False)

    new_word()


def cycle_back(bg):
    canvas.itemconfigure(f_img, state="hidden")
    canvas.itemconfigure(b_img, state="normal")
    canvas.itemconfigure(title, text="Български", fill="white")
    canvas.itemconfigure(word, text=bg, fill="white")


def front(en, bg):
    window.after(3000, cycle_back, bg)
    canvas.itemconfigure(b_img, state="hidden")
    canvas.itemconfigure(f_img, state="normal")
    canvas.itemconfigure(title, text="English", fill="black")
    canvas.itemconfigure(word, text=en, fill="black")


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=20, pady=30)
canvas = Canvas()
canvas.config(bg=BACKGROUND_COLOR, width=800, height=520, highlightthickness=0)

front_img = PhotoImage(file="./images/card_front.png")
back_img = PhotoImage(file="./images/card_back.png")
f_img = canvas.create_image(410, 270, image=front_img)
b_img = canvas.create_image(410, 270, image=back_img)
canvas.itemconfigure(b_img, state="hidden")
canvas.itemconfigure(f_img, state="normal")
title = canvas.create_text(400, 150, text="Title", font=("Arial", 36, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

btn_y_img = PhotoImage(file="./images/right.png")
btn_no_img = PhotoImage(file="./images/wrong.png")

btn_no = Button(image=btn_no_img, highlightthickness=0, command=new_word)
btn_no.grid(row=1, column=0)
btn_yes = Button(image=btn_y_img, highlightthickness=0, command=remove_word)
btn_yes.grid(row=1, column=1)

new_word()

window.mainloop()
