# Write a program to calculate the total marks of each student stored in a dictionary.

# students = {
#     "Pradip" : [70, 80, 90],
#     "Vivek" : [80, 85, 75],
#     "Meetraj" : [90, 95, 85],
#     "Ishwar" : [91, 95, 96]
# }

# for name, marks in students.items():
#     total = sum(marks)
#     print(f"{name} Total Marks: {total}")
    
    
# Write a program to find the student with the highest marks using a dictionary.

# students = {
#     "Pradip" : 98,
#     "Vivek" : 85,
#     "Meetraj" : 95,
#     "Ishwar" :  96
# }

# top_student = ""
# high_mark = 0

# for name, marks in students.items():
#     if marks > high_mark:
#         high_mark = marks
#         top_student = name

# print(f"Topper Name: {top_student} \nHighest Mark: {high_mark}")

# Write a program to read data from a file and display it line by line.

# file = open("pradip.txt", "r")

# for line in file:
#     print(line.strip())
    
# file. close()

# Write a program to count the number of lines in a file.

# file = open("pradip.txt", "r")

# line_count = 0

# for line in file:
#     line_count += 1
    
# print("Number Of Lines: ",line_count)

# file.close()

# Write a program to write numbers from 1 to 20 into a file.

# file = open("Number.txt", "w")

# for i in range(1, 21):
#     file.write(str(i) + "\n")
    
# print("Number Written by Succesfully.")

# file.close()

# Write a program to write list elements into a file using a loop.

items = ["Iphone", "Vivo", "Oppo", "Mi", "Samsaung", "Realme", "OnePlus"]

file = open("Product.txt", "w")

for item in items:
    file.write(item + "\n")

print("Product List add in File.")

file.close()