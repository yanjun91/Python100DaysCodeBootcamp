from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Arial", 40, "italic")
TRANSLATE_FONT = ("Arial", 60, "bold")
words_list = {}
current_card = {}

# Open the words to learn file when available
try:
    words_df = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    ori_words_df = pandas.read_csv("./data/french_words.csv")
    words_list = ori_words_df.to_dict(orient="records")
else:
    words_list = words_df.to_dict(orient="records")


# Remove the words learnt and save to a new csv file for study next time
def word_learnt():
    words_list.remove(current_card)
    df = pandas.DataFrame(words_list)
    df.to_csv("./data/words_to_learn.csv", index=False)
    get_random_french_word()


def get_random_french_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)  # cancels the sleep timer until we stop clicking on button
    current_card = random.choice(words_list)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(card_background, image=flash_card_front)
    flip_timer = window.after(3000, func=flip_card)  # Re-add the sleep timer if we didn't click button again


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=flash_card_back)


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Flash Card
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
flash_card_front = PhotoImage(file="images/card_front.png")
card_background = canvas.create_image(400, 263, image=flash_card_front)
card_title = canvas.create_text(400, 150, text="", fill="black", font=LANGUAGE_FONT)
card_word = canvas.create_text(400, 263, text="", fill="black", font=TRANSLATE_FONT)
canvas.grid(row=0, column=0, columnspan=2)

flash_card_back = PhotoImage(file="images/card_back.png")

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=get_random_french_word)
wrong_button.grid(row=1, column=0, pady=50)

tick_image = PhotoImage(file="images/right.png")
right_button = Button(image=tick_image, highlightthickness=0, command=word_learnt)
right_button.grid(row=1, column=1, pady=50)

get_random_french_word()  # Initialize card content

window.mainloop()
