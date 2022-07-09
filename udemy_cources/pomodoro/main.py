from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
clock = ""


# ---------------------------- TIMER RESET ------------------------------- #
def reset():
    counter_label.config(text="")
    screen.after_cancel(clock)
    global reps
    reps = 0
    label.config(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW, foreground=GREEN)
    canvas.itemconfig(timer, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        time = LONG_BREAK_MIN * 60
        label.config(text="Break", fg=RED)
    elif reps % 2 != 0:
        time = WORK_MIN * 60
        label.config(text="Work", fg=GREEN)
    else:
        time = SHORT_BREAK_MIN * 60
        label.config(text="Break", fg=PINK)
    countdown(time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(minutes):
    global clock
    if minutes == "reset":
        return
    mm = minutes // 60
    ss = minutes % 60
    canvas.itemconfig(timer, text=f"{mm:02d}:{ss:02d}")
    if minutes > 0:
        clock = screen.after(1000, countdown, minutes - 1)
    else:
        if reps % 2 != 0:
            counter_label.config(text=counter_label.cget("text") + "✔")
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)
tomato_png = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_png)
timer = canvas.create_text(100, 135, text="00:00", font=(FONT_NAME, 48, "bold"), fill="white")

label = Label(text="Timer", font=(FONT_NAME, 42, "bold"), bg=YELLOW, foreground=GREEN)
label.grid(column=1, row=0)
start_btn = Button(text="Start", command=start_timer, width=8)
start_btn.grid(column=0, row=2)
reset_btn = Button(text="Reset", command=reset, width=8)
reset_btn.grid(column=2, row=2)
counter_label = Label(text="", bg=YELLOW, foreground=GREEN)
counter_label.grid(column=1, row=3)

screen.mainloop()
