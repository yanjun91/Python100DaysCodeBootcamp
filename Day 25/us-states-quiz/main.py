import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Import 50 states csv file
all_states = pandas.read_csv("50_states.csv")
states_list = all_states.state.to_list()
# Initializes values
correct_guesses = []
continue_game = True

while continue_game:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    # If user types exit, then add states missing from guesses into a csv files and exit the game
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # Write correct guess to map image if the guessed state is in the list and it has not guessed correctly before
    if answer_state in states_list and answer_state not in correct_guesses:
        answered_row = all_states[all_states["state"] == answer_state]
        new_state = turtle.Turtle()
        new_state.hideturtle()
        new_state.penup()
        new_state.goto(x=int(answered_row.x), y=int(answered_row.y))
        new_state.write(answer_state, align="left", font=("Courier", 8, "bold"))
        correct_guesses.append(answer_state)  # or answered_row.state.item()

    if len(correct_guesses) == 50:
        continue_game = False

print(set(states_list).difference(correct_guesses))

screen.exitonclick()
