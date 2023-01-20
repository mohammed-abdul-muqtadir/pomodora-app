from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
tick_symbol = "✔"
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global REPS
    window.after_cancel(str(TIMER))
    REPS = 0
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    tick_label.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global REPS
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60
    REPS += 1
    if REPS == 1 or REPS == 3 or REPS == 5 or REPS == 7:
        count_down(work_sec)
        timer_label.config(text="WORK", fg=GREEN)
    elif REPS == 2 or REPS == 4 or REPS == 6:
        count_down(short_break)
        timer_label.config(text="Break", fg=PINK)
    elif REPS == 8:
        count_down(long_break)
        timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > -1:
        global TIMER
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        work_sessions = ""
        for i in range(floor(REPS / 2)):
            work_sessions += tick_symbol
        tick_label.config(text=f"{work_sessions}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=100, bg=YELLOW)

timer_label = Label(text="Timer", font=(FONT_NAME, 50, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

tick_label = Label(fg=GREEN, bg=YELLOW)
tick_label.grid(row=3, column=1)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 32, "bold"), fill="white")
canvas.grid(row=1, column=1)

window.mainloop()
