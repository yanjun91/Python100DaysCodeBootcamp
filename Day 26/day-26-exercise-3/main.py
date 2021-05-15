with open("file1.txt") as file1:
    file1_list = file1.readlines()

file1_list = [int(n.strip()) for n in file1_list]

with open("file2.txt") as file1:
    file2_list = file1.readlines()

file2_list = [int(n.strip()) for n in file2_list]

result = [file1_number for file1_number in file1_list if file1_number in file2_list]

# Write your code above 👆

print(result)
