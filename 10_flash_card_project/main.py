from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

# ---------------------------- UI SETUP ------------------------------- #

# Window
window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50)

# Canvas
canvas = Canvas(width=800, height=526)
front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")
canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=1)

window.mainloop()

