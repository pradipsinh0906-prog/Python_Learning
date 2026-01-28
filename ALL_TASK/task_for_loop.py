# Query for Task :- 8,9,10
# Answer 1:- 
# n = int(input("Enter a number: "))

# for i in range(n):
#     print("Hello World")

# Answer 2:-
# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     print(i)

# Answer 3:-
# n = int(input("Enter a number: "))

# for i in range(n,0, -1):
#     print(i)

# Answer 4:-
# n = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(f"{n} X {i} = {n*i}")

# Answer 5:-
# n = int(input("Enter a number: "))

# sum = 0 
# for i in range(1, n+1):
#     sum += i
# print(f"The sum of first {n} natural numbers is: {sum}")

# Answer 6:-
# n = int(input("Enter a number: "))

# fact = 1
# for i in range(1, n+1):
#     fact = fact * i
# print(f"The factorial of {n} is: {fact}")

# Answer 7:-
# n = int(input("Enter a number: "))

# even = 0
# odd = 0

# for i in range(1, n+1):
#     if i%2 == 0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"The sum of even numbers from 1 to {n} is: {even} , and the sum of odd numbers is: {odd}")

# Answer 8:- factors of a number - Divide thase to print thase factors
# 28 -> 1,2,4,7,14,28
# 12 -> 1,2,3,4,6,12
# n = int(input("Enter a number: "))

# for i in range(1, n+1):
#     if n % i == 0:
#         print(i)

# Answer 9:- perfect number - divide ane sum bane same thase atle number perfect number chhe
# n = int(input("Enter a number: "))

# total = 0

# for i in range(1, n):
#     if n % i == 0:
#         total += i

# if total == n:
#     print("Perfect Number")
# else:
#     print("Not a Perfect Number")

# Answer 10:- prime number - je divide na thai sake aavu 
# n = int(input("Enter a number: "))

# count = 0 

# for i in range(1, n + 1):
#     if n % i == 0:
#         count += 1
#         print(count)

# if count == 2:
#     print("Prime Number")
# else:
#     print("Not a Prime Number")

# Answer 11:-
# str = input("Enter a string: ")
# rev = ""

# for ch  in str:
#     rev = ch + rev

# print("Reversed String is:", rev)

# Answer 12:- #o/p:- madam, level, radar
# str = input("Enter a string: ")
# rev = ""

# for i in str:
#     rev = i + rev
#     print(rev)
# if str == rev:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")

# Answer 13:-
str = "P@#yn26at^&i5ve"

chars = 0
digits = 0
symbols = 0

for i in str:
    if i.isalpha():
        chars += 1
    elif i.isdigit():
        digits += 1
    else:
        symbols += 1

print("Characters:", chars)
print("Digits:", digits)
print("Symbols:", symbols)