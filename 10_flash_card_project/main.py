from tkinter import *
import random
import pandas

data = pandas.read_csv("data/french_words.csv")

current_card = data.iloc[random.randint(0, len(data) - 1)]

flip_timer = None

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARD CONFIGURATION ------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(language_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])

def next_card():
    global current_card, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    current_card = data.iloc[random.randint(0, len(data) - 1)]

    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(language_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(3000, flip_card)

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_image)
language_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["French"], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0, bd=0)
right_button = Button(image=right_image, command=next_card, highlightthickness=0, bd=0)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)

next_card()

window.mainloop()

