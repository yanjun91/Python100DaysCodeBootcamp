from art import logo, vs
from game_data import data
import random
from replit import clear

def generate_choices(choices):
    """Randomly generate two choices for the game."""
    if len(choices) == 0: # If the list is empty, then generate two choices
        return random.sample(data,2)
    else: # If list contains anything means it is on second round onwards. Hence, swap the choice position and generate a new choice B
        choices[0] = choices[1]
        choices[1] = random.choice(data)
        return choices

def check_result(choices, user_choice):
    """Compare results between two randomly generated accounts and check if user guessed correctly. Return boolean on the result to indicate if user is correct."""
    if choices[0]["follower_count"] > choices[1]["follower_count"] and user_choice == "a":
        return True
    elif choices[0]["follower_count"] < choices[1]["follower_count"] and user_choice == "b":
        return True
    else:
        return False

def format_output(choice):
    return f"{choice['name']}, {choice['description']}, from {choice['country']}."

# Main higher lower game function
def higher_lower_game():
    random_choices = []
    score = 0
    continue_game = True
    print(logo)
    while continue_game:
        random_choices = generate_choices(random_choices)
        while random_choices[0]['name'] == random_choices[1]['name']:
            # re-generate another account if both are the same
            random_choices = generate_choices(random_choices)
        print(f"Compare A: {format_output(random_choices[0])}")
        print(vs)
        print(f"Against B: {format_output(random_choices[1])}")

        # Gets user input to guess which account has more followers
        user_guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Compare the 2 randomly generated data and check against user input
        correct = check_result(random_choices, user_guess)
        clear()
        print(logo)
        if correct:
            # If guessed correctly, add score and generate another insta account to compare with B 
            score += 1
            random_choices = generate_choices(random_choices)
            print(f"You're right! Current score: {score}.")
            continue_game = True
        else:
            # If user guessed wrongly, show final score and end game
            print(f"Sorry, that's wrong. Final score: {score}")
            continue_game = False

higher_lower_game()
