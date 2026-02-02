# 1. Write a program to print multiplication table of a given number using for loop.

# num = int(input("Enter the number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# 2. Write a program to greet all the person names stored in a list 'l' and which starts with S.

# l= ["Har", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print("Hello", name)

# 3. Attempt problem 1 using while loop.

# num = int(input("Enter the number: "))
# i = 1

# while i<=10:
#     print(num, "x", i, "=", num * i)
#     num += 1
    
# 4. Write a program to find whether a given number is prime or not.

# num = int(input("Enter the number: "))

# if num <= 1:
#     print("Not a Prime")
# else:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime Number")

# 5. Write a program to find the sum of first n natural numbers using while loop.

# n = int(input("Enter the Number: "))
# sum = 0
# i = 1

# while i <= n:
#     sum += i
#     i += 1
    
# print("Sum =", sum)

# 6. Write a program to calculate the factorial of a given number using for loop.

# num = int(input("Enter a number: "))

# fact = 1

# for i in range(1, num + 1):
#     fact += 1
    
# print("Factorial: ",fact)

# 7. Write a program to print the following star pattern.
#   *
#  *
# ***
   
print("  *")
print(" *")
print("***")
