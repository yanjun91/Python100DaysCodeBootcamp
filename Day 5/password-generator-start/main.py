#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your easy_password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
easy_password = ""
for letter_num in range(0, nr_letters):
  rand_letters_index = random.randint(0, len(letters) - 1) # can use random.choice(letters) instead for shorter code
  easy_password += letters[rand_letters_index]

for symbol_num in range(0, nr_symbols):
  rand_symbols_index = random.randint(0, len(symbols) - 1)
  easy_password += symbols[rand_symbols_index]

for number_num in range(0, nr_numbers):
  rand_numbers_index = random.randint(0, len(numbers) - 1)
  easy_password += numbers[rand_numbers_index]

print(easy_password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = []
for letter_num in range(0, nr_letters):
  rand_letters_index = random.randint(0, len(letters) - 1)
  hard_password.append(letters[rand_letters_index])

for symbol_num in range(0, nr_symbols):
  rand_symbols_index = random.randint(0, len(symbols) - 1)
  hard_password.append(symbols[rand_symbols_index])

for number_num in range(0, nr_numbers):
  rand_numbers_index = random.randint(0, len(numbers) - 1)
  hard_password.append(numbers[rand_numbers_index])

random.shuffle(hard_password)
final_password = ""
for character in hard_password:
  final_password += character
print(final_password)
