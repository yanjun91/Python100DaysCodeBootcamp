#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

HARD_LEVEL_TURNS = 10
EASY_LEVEL_TURNS = 5

def generate_number():
    return random.randint(1, 100)

def check_number(guess):
    if guess == random_number:
        print(f"You got it! The answer was {random_number}.")
        return True
    elif guess > random_number:
        print("Too high.")
        return False
    elif guess < random_number:
        print("Too low.")
        return False

def init_turns_remaining():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if(difficulty == "easy"):
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

random_number = generate_number()
game_over = False
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {random_number}")
turns_remaining = init_turns_remaining()

while not game_over:
    print(f"You have {turns_remaining} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    win = check_number(guess)
    if win:
        game_over = True
    elif turns_remaining == 1 and not win:
        game_over = True
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
        turns_remaining -= 1
        game_over = False
    