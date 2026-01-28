# Task 12:- Program 1:- Store squared values of list elements into a file

# numbers = [2, 4, 6, 8, 10]

# file = open("Square.txt", "w")

# for num in numbers:
#     file.write(str(num ** 2) + "\n")
    
# file.close()

# print("Squared values written to file successfully.")

# Program 2:- Read list data from a file and store it back into a list

file = open("data.txt", "r")

my_list = []

for line in file:
    my_list.append(int(line.strip()))
    
file.close()

print("List from file:",my_list)