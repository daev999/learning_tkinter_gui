from tkinter import *
import random
import pandas

# Does words_to_learn.csv exist?
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")

to_learn = data.to_dict(orient="records")

current_card = random.choice(to_learn)

flip_timer = None

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- CARD CONFIGURATION ------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(language_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])

def next_card():
    global current_card, flip_timer, to_learn

    if flip_timer:
        window.after_cancel(flip_timer)

    current_card = random.choice(to_learn)

    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(language_title, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    flip_timer = window.after(3000, flip_card)

def is_known():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)
    next_card()

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_image)
language_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["French"], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1)

right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")

wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0, bd=0)
right_button = Button(image=right_image, command=is_known, highlightthickness=0, bd=0)

wrong_button.grid(row=1, column=0)
right_button.grid(row=1, column=2)

next_card()

window.mainloop()

