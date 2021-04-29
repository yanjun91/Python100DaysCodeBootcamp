import random

random_integer = random.randint(1, 10)
print(random_integer)

# 0.0000... - 0.99999...
random_float = random.random() # this produces random float number between 0 to 1(non-inclusive) [0, 1)
print(random_float)

# random float number between 1 to 5 (non-inclusive) 
# 0.0000... - 4.99999...
random_float_0_5 = random_float * 5 
print(random_float_0_5)