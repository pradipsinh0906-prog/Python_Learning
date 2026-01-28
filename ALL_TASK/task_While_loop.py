# Task 1:
# n = int(input("Enter a number: "))

# while n > 0:
#     digit = n % 10
#     print(digit)
#     n = n // 10

# Task 2:
# n = int(input("Enter a number: "))

# rev = 0

# while n > 0:
#     digit = n % 10
#     # print(digit)
#     rev = rev * 10 + digit
#     print(rev)
#     n = n // 10

# print("Reversed Number is:", rev)

# Task 3:
# n = int(input("Enter a number: "))
# temp = n
# rev = 0

# while n > 0:
#     digit = n % 10
#     rev = rev * 10 + digit
#     n = n // 10

# if temp == rev:
#     print("Palindrome Number")
# else:
#     print("Not a Palindrome Number")

# task 4:
# import random

# number = random.randint(1, 10)
# guess = 0

# while guess != number:
#     guess = int(input("Guess the number (1-10): "))

#     if guess < number:
#         print("Too Low!")
#     elif guess > number:
#         print("Too High!")
#     else:
#         print("🎉 Congratulations! You guessed it right.")
