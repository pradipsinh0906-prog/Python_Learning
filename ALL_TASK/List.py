# 1. Create a list of 10 numbers and print only even numbers

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for num in numbers:
#     if num % 2 == 0:
#         print(num)

# 2. Find the sum and average of list elements 

# num = [10, 20, 30, 40, 50]

# total = sum(num)
# average = total / len(num)

# print("Sum:", total)
# print("Average: ", average)

# 3. Find the largest and smallest element in a list 

# numbers = [34, 12, 5, 67, 23, 99, 2]

# print("Largest number: ", max(numbers))
# print("Smallest number: ", min(numbers))

# 4. Reverse a list without using reverse()
# num = [1, 2, 3, 4, 5]

# reversed_list = num[::-1]

# print("Reversed List: ", reversed_list)

# 5. Count how many times a value appears in a list 

# num = [1, 2, 3, 2, 4, 2, 5, 2, 2, 4, 4, 5, 1, 5]
# value = int(input("Enter a value to count: "))

# count = num.count(value)

# print("Count : ", count)

# 6. Remove duplicate elements from a list 
# num = [1, 2, 3, 2, 4, 5, 1, 3, 4, 5, 6, 7, 8, 6]

# unique = list(set(num))

# print("List after removing duplicates: ", unique)

# 7. Merge two lists and sort them 
# list1 = [5, 2, 9, 1]
# list2 = [8, 3, 7, 4]

# merge_list = list1 + list2
# merge_list.sort()

# print("Merged and sorted list: ", merge_list)

# 8. Find common elements between two lists 
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 1, 8]

# common = set(list1) & set(list2)

# print("Common elements: ", list(common))

# 9. Replace all negative numbers with 0 
# num = [10, -5, 3, -1, 0, -7, 8]

# for i in range(len(num)):
#     if num[i] < 0:
#         num[i] = 0
# print("List after replacing negatives with 0: ", num)

# 10. Convert a list of strings into uppercase
str = ["python", "java", "c++", "ruby"]

uppercase_list = []

for name in str:
    uppercase_list.append(name.upper())

print("Uppercase List: ", uppercase_list)