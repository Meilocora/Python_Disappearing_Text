from tkinter import *
from tkinter.scrolledtext import ScrolledText
import math
# ---------------------------- CONSTANTS ------------------------------- #
FONT_NAME = "Courier"
COUNT = 5
timer = None

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def stop_timer():
    global timer
    window.after_cancel(timer)


def count_down(COUNT):
    count_min = math.floor(COUNT / 60)
    count_sec = COUNT % 60
    count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if COUNT > 0:
        global timer
        timer = window.after(1000, count_down, COUNT - 1)
    else:
        clear_inputs()
        stop_timer()


def clear_inputs():
    # user_text.delete(0, END)
    user_text.delete(1.0, END)


def callback(event):
    stop_timer()
    count_down(COUNT)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Disappearing Text Writing App")
window.config(padx=30, pady=30)

main_label = Label(text="Disappearing Text Writing App", font=(FONT_NAME, 35, "bold"), pady=20)
main_label.grid(row=0, column=1)

canvas = Canvas(width=800, height=100)
timer_label = canvas.create_text(400, 20, text="Timer", font=(FONT_NAME, 24, "bold"))
timer_text = canvas.create_text(400, 55, text="00:00", font=(FONT_NAME, 24, "bold"))
canvas.grid(column=0, row=1, columnspan=3)

var = StringVar()
user_text = ScrolledText(window, font=(FONT_NAME, 16, "normal"))
user_text.bind('<KeyRelease>', callback)
user_text.grid(column=0, row=6, columnspan=3)

user_text.focus()
count_down(COUNT)
window.mainloop()
