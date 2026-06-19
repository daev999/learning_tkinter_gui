from tkinter import *
import random
import pandas

data = pandas.read_csv("data/french_words.csv")

random_index = random.randint(0, len(data) - 1)
current_card = data.iloc[random_index]

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- FLIP CARD ------------------------------- #
def flip_card():
    canvas.itemconfig(card_background, image=back_image)
    canvas.itemconfig(language_title,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])



# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

card_background = canvas.create_image(400, 263, image=front_image)
language_title = canvas.create_text(400, 150, text="French", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text=current_card["French"], font=("Arial", 60, "bold"))
canvas.grid(row=0, column=1)

window.after(3000, flip_card)


window.mainloop()

