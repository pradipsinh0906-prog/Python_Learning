# Task 11:-  Program 1:- Read numbers from a file and calculate their sum
# file = open("Number.txt", "r")

# total = 0

# for line in file:
#     total += int(line.strip())
    
# file.close()

# print("Sum Of Numbers: ",total)

# Program 2:- Read numbers from a file and count even and odd numbers

file = open("Number.txt", "r")

even_count = 0
odd_count = 0

for line in file:
    num = int(line.strip())
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
file.close()

print("Even Numbers Count:",even_count)
print("Odd Numbers Count:",odd_count)