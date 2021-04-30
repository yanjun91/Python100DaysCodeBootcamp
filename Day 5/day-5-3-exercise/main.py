#Write your code below this row 👇

# method 1
even_total = 0
for number in range(2, 101, 2):
  even_total += number

print(even_total)

# method 2
even_total2 = 0
for number in range(1, 101):
  if number % 2 == 0:
    even_total2 += number

print(even_total2)