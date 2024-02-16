from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/functions_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/builtin_functions.csv")
    to_learn = data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global flip_timer, current_card
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(image, image=card_front)
    canvas.itemconfig(card_title, text="Function", fill="black")
    canvas.itemconfig(card_word, text=current_card["Function"], fill="black", font=("Arial", 60, "bold"))
    flip_timer = window.after(3000, func=flip_card)


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/functions_to_learn.csv", index=False)
    next_card()


def flip_card():
    canvas.itemconfig(card_title, text="Meaning", fill="white")
    canvas.itemconfig(card_word, text=current_card["Meaning"], fill="white", font=("Arial", 15, "bold"))
    canvas.itemconfig(image, image=card_back)


# --------------------------------------UI-SETUP-------------------------------------------#
window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, pady=50, padx=50)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(height=564, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
image = canvas.create_image(400,  263, image=card_front)
card_title = canvas.create_text(400, 150, text='', font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text='', font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right = PhotoImage(file="images/right.png")
right_button = Button(image=right, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

wrong = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()

window.mainloop()
