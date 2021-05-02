# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Hello")
    print("How are you?")
    print("Goodbye")

greet()

# Function that allows input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("YJ")

# Function with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Call function using Positional Argument
greet_with("Yan Jun", "Penang")

# Call function using Keyword Argument
greet_with(name="Yan Jun", location="Penang")