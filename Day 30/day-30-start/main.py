# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent-key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# TypeError
# text = "abc"
# print(text + 5)

# try:
#     file = open("a_file.txt")
# except:  # catch all exception but only catch the first exception that happened
#     print("There was an error")
#     open("a_file.txt", "w") # Create the file if not exist
#     file.write("Something")


# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["afafa"])
# except FileNotFoundError:  # catch all exception but only catch the first exception that happened
#     file = open("a_file.txt", "w")  # Create the file if not exist
#     file.write("Something")
#     print("File not found")
# except KeyError as error_msg:
#     print(f"Key not found: {error_msg}")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters")

bmi = weight / height ** 2
print(bmi)
