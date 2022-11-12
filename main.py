BACKGROUND_COLOR = "#B1DDC6"
import pandas
from tkinter import *
import random



data = pandas.read_csv("./data/french_words.csv")
to_learn = data.to_dict(orient="records")


def next_card():
    global current_card
    global flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_face, image=card_front)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(word, text=f"{current_card['French']}", fill="black")
    flip_timer = screen.after(3000, flip_card)

def flip_card():
    canvas.itemconfig(card_face, image=card_back)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=f"{current_card['English']}", fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("words_to_learn.csv")
    next_card()

screen = Tk()
screen.title("Flashcards!")
screen.minsize(height=800, width=800)
screen.config(padx=25, pady=25, bg=BACKGROUND_COLOR)

flip_timer = screen.after(3000, flip_card)

card_front = PhotoImage(file="./images/card_front.png")
card_back = PhotoImage(file="./images/card_back.png")
right = PhotoImage(file="./images/right.png")
wrong = PhotoImage(file="./images/wrong.png")


canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_face = canvas.create_image(400, 263, image=card_front)
canvas.grid(columnspan=2, column=0, row=0)
title = canvas.create_text(400, 150, text="Language", font=("Arial", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))

known = Button(image=right, highlightthickness=0, command=is_known)
known.grid(column=0, row=1, pady=50)

unknown = Button(image=wrong, highlightthickness=0, command=next_card)
unknown.grid(column=1, row=1, pady=50)

next_card()

screen.mainloop()