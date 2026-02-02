# 1. Write a program using functions to find greatest of three numbers.

# def greatest(a,b,c):
#     return max(a,b,c)

# print(greatest(10, 15, 50))

# 2. Write a python program using function to convert Celsius to Fahrenheit.

# def Celsius_Fahrenheit(c):
#     return (c * 9/5) + 32

# print(Celsius_Fahrenheit(37))

# 3. How do you prevent a python print() function to print a new line at the end.

# print("Hello", end=" ")
# print("World")

# 4. Write a recursive function to calculate the sum of first n natural numbers.

# def sum_n(n):
#     if n == 0:
#         return 0
#     return n + sum_n(n - 1)

# print(sum_n(5))

# 5. Write a python function to print first n lines of the following pattern:
# *
# **
# *
# - for n = 3

# def patten(n):
#     for i in range(1, n):
#         print("*" * i)
#     for i in range(n-2, 0, -1):
#         print("*" * i)
        
# patten(3)

# 6. Write a python function which converts inches to cms.

# def inches_cms(inch):
#     return inch * 2.54

# print(inches_cms(10))

# 7. Write a python function to remove a given word from a list ad strip it at the same time.

# def remove_word(lst, word):
#     new_list = []
#     for item in lst:
#         item  = item.strip()
#         if item.strip() != word:
#             new_list.append(item)
#     return new_list

# l = [" apple ", " mango ", " banana "]
# print(remove_word(l, "mango"))

# 8. Write a python function to print multiplication table of a given number

def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)
        
table(5)