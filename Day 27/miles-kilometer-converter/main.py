from tkinter import *


def convert():
    miles = float(miles_input.get())
    km = miles * 1.60934
    km_result_label.config(text=str(round(km)))


window = Tk()
window.minsize(width=200, height=100)
window.title("Mile to Km Converter")
window.config(padx=30, pady=30)

miles_input = Entry(width=10)
miles_input.insert(END, string="0")
miles_input.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

calc_button = Button(text="Calculate", command=convert)
calc_button.grid(column=1, row=2)

window.mainloop()