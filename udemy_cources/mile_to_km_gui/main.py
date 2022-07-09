from tkinter import *


def convert_to_km():
    mile = int(miles_input.get())
    km = mile * 1.6
    km_output.delete(0, "end")
    km_output.insert(END, string=str(km))


screen = Tk()
screen.title("Mile to Km Converter")
# screen.minsize(width=800, height=600)
screen.config(padx=100, pady=100)
miles_label = Label(text="Miles")
equal_label = Label(text="is equal to")
km_label = Label(text="Km")

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
km_output = Entry(width=10)
km_output.insert(END, string="0")

calculate_bn = Button(text="Calculate", command=convert_to_km)

miles_input.grid(column=1, row=0, padx=10, pady=5)
miles_label.grid(column=2, row=0, padx=10, pady=5)
equal_label.grid(column=0, row=1, padx=10, pady=5)
km_output.grid(column=1, row=1, padx=10, pady=5)
km_label.grid(column=2, row=1, padx=10, pady=5)
calculate_bn.grid(column=1, row=2, padx=10, pady=5)

screen.mainloop()
