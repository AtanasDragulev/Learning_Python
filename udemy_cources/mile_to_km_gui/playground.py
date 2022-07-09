from tkinter import *

screen = Tk()
screen.minsize(width=500, height=300)
label = Label(text="Label")
label.config(padx=50, pady=50)
button = Button(text="Button1")
new_button = Button(text="New Button")
entry = Entry()
label.grid(column=0, row=0)
button.grid(column=1, row=1)
new_button.grid(column=2, row=0)
entry.grid(column=3, row=2)
screen.mainloop()
