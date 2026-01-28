student = {}

student["name"] = input("Enter Student Name: ")
student["roll_no"] = int(input("Enter Student Enroll No.: "))

marks = []
subjects = ["English", "Maths", "Science"]

for sub in subjects:
    mark = int(input(f"Enter marks of {sub}: "))
    marks.append(mark)
    
student["marks"] = mark

total = 0

for sum_mark in marks:
    total += sum_mark
    
percentage = total / len(marks)

if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"
    
file = open("student_report.txt", "w")

file.write("Student Report\n")
file.write("-----------------\n")
file.write("Name: " + student["name"] + "\n")
file.write("Enroll No.: " + str(student["roll_no"]) + "\n")
file.write("Marks: " + str(student["marks"]) + "\n")
file.write("Total: " + str(total) + "\n")
file.write("Percentage: " + str(percentage) + "\n")
file.write("Result: " + str(result) + "\n")

file.close()

print("\nReport saved successfully!\n")

file = open("student_report.txt", "r")
# print("----- Student Report -----")
print(file.read())
file.close()