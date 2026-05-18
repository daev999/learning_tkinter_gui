from tkinter import *

def action():
    miles_to_convert = float(miles_box.get())
    converted_km = round(miles_to_convert * 1.609, 2)
    converted_num.config(text = converted_km)
    return converted_km


#Creating a new window and configurations
window = Tk()
window.title("miles_to_km_converter")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)

#Labels
is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

converted_num = Label(text="0")
converted_num.grid(column=1, row=1)

miles = Label(text="miles")
miles.grid(column=2, row=0)

km = Label(text="km")
km.grid(column=2, row=1)

#Entries
miles_box = Entry(width=10)
miles_box.grid(column=1, row=0)

#Buttons
calculate_button = Button(text="calculate", command=action)
calculate_button.grid(column=1, row=2)




window.mainloop()