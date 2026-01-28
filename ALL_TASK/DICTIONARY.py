# 1. Create a dictionary of student names and marks 

# students = {
#     "Pradip": 85,
#     "Meetraj": 90,
#     "Vivek": 78,
#     "Ankit": 92,
# }

# print("Student Marks Dictionary:", students)

# 2. Access value using key 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78, "Ankit": 92}

# student_name = input("Enter student name to get marks: ")

# if student_name in students:
#     print("Marks of", student_name, ":", students.get(student_name))
# else:
#     print("Student not found")

# 3. Add a new key-value pair 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78, "Ankit": 92}

# students["Rina"] = 88

# print("Updated Student Marks Dictionary:", students)

# 4. Update value of an existing key 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78}

# students["Vivek"] = 80

# print("Updated Marks of Vivek:", students)

# 5. Delete a key from dictionary 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78, "Ankit": 92}

# del students["Ankit"]

# print("Dictionary after deleting Ankit:", students)

# 6. Print all keys and values 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78}

# for name, marks in students.items():
#     print(name, ":", marks)

# 7. Check whether a key exists 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78}

# student_name = input("Enter student name to check: ")

# if student_name in students:
#     print(student_name, "exists in the dictionary")
# else:
#     print(student_name, "does not exist in the dictionary")

# 8. Count frequency of characters in a string 

# str = input("Enter a string: ")

# freq = {}

# for char in str:
#     freq[char] = freq.get(char, 0) + 1

# print("Character Frequency:", freq)

# 9. Find student with highest marks 

# students = {"Pradip": 85, "Meetraj": 90, "Vivek": 78, "Ankit": 92}

# top_student = max(students, key=students.get)

# print("Top student:", top_student, "with marks:", students[top_student])

# 10. Merge two dictionaries

dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

merged_dict = dict1 | dict2

print("Merged Dictionary:", merged_dict)