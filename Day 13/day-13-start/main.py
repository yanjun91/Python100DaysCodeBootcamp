############DEBUGGING#####################

# # Describe Problem
# def my_function():
#   for i in range(1, 20): # BUG: range does not include the stop param number, in this case, it loops from 1 to 19 only
#     if i == 20:
#       print("You got it")
# my_function()

# # Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # BUG: randomly gets number from 1 to 6 inclusive. List only has index of 0,1,2,3,4,5
# print(dice_imgs[dice_num])

# # Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994: # BUG: 1994 will not fulfill in both if and elif condition
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # Fix the Errors
# age = input("How old are you?")
# if age > 18:# BUG: age input is in string type but we are comparing to number here
# print("You can drive at age {age}.") # BUG: not indented and don't have f-string to format the variable age in print

# #Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # BUG: should use only one equal sign to assign to variable
# total_words = pages * word_per_page
# print(total_words)

#Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item) # BUG: Indent this to multiply 2 for each item in list instead of appending the last item that is multiply by 2 into b_list
#   print(b_list)

# mutate([1,2,3,5,8,13])