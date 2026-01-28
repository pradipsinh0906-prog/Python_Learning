import math


name = input("Enter your name: ")

sub1 = int(input("Enter marks for Subject 1: "))
sub2 = int(input("Enter marks for Subject 2: "))
sub3 = int(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
percentage = total / 3

print("\nStudent Name: ", name)
print("Total Marks: ", total)
print("Percentage: ", math.trunc(percentage)) #int, round, math trunc

if sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
    print("Result: Pass")

    if percentage >= 90:
        print("Grade: A+")
    elif percentage >= 75:
        print("Grade: A")
    elif percentage >= 60:
        print("Grade: B")
    elif percentage >= 50:
        print("Grade: C")
    elif percentage >= 35:
        print("Grade: D")

else:
    print("Result: Fail")
    print("Grade: F")

