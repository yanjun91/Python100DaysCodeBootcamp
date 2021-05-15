from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=100)

def button_clicked():
    # my_label.config(text="Button got clicked")
    my_label.config(text=input.get())


# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=20, pady=20)

# Use either of the way below to change label
my_label["text"] = "New Text"
my_label.config(text="New Text")

# Button
button = Button(text="Click Me", command=button_clicked)
# button.pack()
button.grid(column=1, row=1)

# Entry component
input = Entry(width=10)
# input.pack()
input.grid(column=3, row=2)

new_button = Button(text="Click me too!")
new_button.grid(column=2, row=0)

window.mainloop()
