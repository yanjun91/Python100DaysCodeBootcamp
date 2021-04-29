# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_name = (name1 + name2).lower()

t_count = combined_name.count("t")
r_count = combined_name.count("r")
u_count = combined_name.count("u")
e_count = combined_name.count("e")

true_count = str(t_count + r_count + u_count + e_count)

l_count = combined_name.count("l")
o_count = combined_name.count("o")
v_count = combined_name.count("v")
e_count = combined_name.count("e")

love_count = str(l_count + o_count + v_count + e_count)

score = int(true_count + love_count)

if score < 10 or score > 90:
  print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")