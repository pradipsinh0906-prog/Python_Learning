# Task 13:- Program 1:- Write dictionary data into a file (key–value format)

# student = {
#     "Pradip": 95,
#     "Vivek": 80,
#     "Meetraj": 90
# }

# file = open("student.txt", "w")

# for key, value in student.items():
#     file.write(key + ":" + str(value) + "\n")
    
# file.close()

# print("Dictionary data written to file")

# Program 2: Read dictionary data from a file and recreate the dictionary

file = open("student.txt", "r")

student = {}

for line in file:
    key, value = line.strip().split(":")
    student[key] = int(value)
    
file.close()

print("Dictionary recreated from file:",student)