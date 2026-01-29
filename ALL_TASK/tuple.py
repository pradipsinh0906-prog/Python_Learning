# 1. Create a tuple and print its length 

# my_tuple = (10, 20, 30, 40, 50)

# print("Length:",len(my_tuple))

# 2. Access first and last element of a tuple 
# my_tuple = (5, 15, 25, 35, 45)

# print("First element:", my_tuple[0])
# print("Last element:", my_tuple[-1])

# 3. Convert a tuple into a list and modify it 
# my_tuple = (1, 2, 3, 4, 5)
# my_list = list(my_tuple)

# my_list.append(6)

# print("Modified List:", my_list)

# 4. Find maximum and minimum value in a tuple 
# my_tuple = (12, 45, 7, 23, 89, 3)

# print("Maximum value:", max(my_tuple))
# print("Minimum value:", min(my_tuple))

# 5. Count occurrences of an element in a tuple 

# my_tuple = (1, 2, 3, 2, 4, 2, 5, 2)

# print("Count of 2:", my_tuple.count(2))

# 6. Check whether an element exists in a tuple 

# num = int(input("Enter a number to check: "))

# my_tuple = (10, 20, 30, 40, 50)

# if num in my_tuple:
#     print("Element exists in the tuple")
# else:
#     print("Element does not exist in the tuple")

# 7. Reverse a tuple 

# my_tuple = (1, 2, 3, 4, 5)

# reversed_tuple = my_tuple[::-1]

# print("Reversed Tuple:", reversed_tuple)

# 8. Convert a list into a tuple 

# my_list = [10, 20, 30, 40, 50]

# my_tuple = tuple(my_list)

# print("Converted Tuple:", my_tuple)

# 9. Unpack tuple elements into variables 

# my_tuple = (100, 200, 300)

# a, b, c = my_tuple

# print("a:", a)
# print("b:", b)
# print("c:", c)

# 10. Create a tuple of squares of numbers

my_tuple = ()

for i in range(1, 6):
    my_tuple += (i*i,)

print("Tuple of squares:", my_tuple)