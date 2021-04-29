import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
# 0 > 2
# 1 > 0
# 2 > 1

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
computer_choice = random.randint(0, 2)

# Method 1
if user_choice > 2 or user_choice < 0:
  print("You've typed a wrong choice. You lose")
else:
  print(game_images[user_choice])
  print(f"Computer choose:\n{game_images[computer_choice]}")
  if user_choice == computer_choice:
    print("Draw")
  else:
    if user_choice == 0:
      if computer_choice == 2:
        print("You win")
      else:
        print("You lose")
    elif user_choice == 1:
      if computer_choice == 0:
        print("You win")
      else:
        print("You lose")
    else:
      if computer_choice == 1:
        print("You win")
      else:
        print("You lose")

# Method 2
if user_choice > 2 or user_choice < 0:
  print("You've typed a wrong choice. You lose")
else:
  print(game_images[user_choice])
  print(f"Computer choose:\n{game_images[computer_choice]}")
  if user_choice == computer_choice:
    print("Draw")
  else:
    if (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
      print("You win")
    else:
      print("You lose")

# Instructor method
if user_choice >= 3 or user_choice < 0: 
    print("You typed an invalid number, you lose!") 
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])


    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")
