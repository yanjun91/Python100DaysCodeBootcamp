file = open("my_file.txt")
contents = file.read()
print(contents)
file.close()  # Remember to close file to free up memory

# using this way to open file do not need to explicitly call close()
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)

# Open in write mode. Existing contents will be replaced. If file not exist, a new file will be created
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Open in append mode. Text will be append at the end of file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
