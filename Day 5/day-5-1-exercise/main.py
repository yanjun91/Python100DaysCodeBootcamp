# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # convert each item in list to int data type
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
num_of_students = 0
total_height = 0
for student_height in student_heights:
  num_of_students += 1
  total_height += student_height

average = round(total_height / num_of_students)

print(average)


