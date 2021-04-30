fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
  print(fruit)
  print(fruit + " Pie")
print(fruits)

print("---")

for number in range(1, 11): # this range will loop until 10 == [1, 10)
  print(number)

print("---")

for number in range(1, 11, 3): # 3rd parameter is the step where we define how much to add on each loop
  print(number)