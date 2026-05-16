from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("miles_to_km_converter")
window.minsize(width=300, height=200)

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




window.mainloop()