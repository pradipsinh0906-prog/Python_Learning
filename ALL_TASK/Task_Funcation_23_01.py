# Function to check palindrome string.

# def is_palidrome(s):
#     start = 0
#     end = len(s) - 1
    
#     while start < end:
#         if s[start] != s[end]:
#             return False
#         start += 1
#         end -= 1
#     return True

# print("Palidrome is not:",is_palidrome("pradip"))
# print("Palidrome is:",is_palidrome("level"))

# Function to count vowels in a string.

# def count_vowels(s):
#     vowels = "aeiouAEIOU"
#     count = 0
    
#     for char in s:
#         if char in vowels:
#             count += 1
#     return count

# print(count_vowels("pradip"))
# print(count_vowels("Education"))
# print(count_vowels("meetraj"))

# Function to generate Fibonacci series up to n.

# def fibonacci(n):
#     a, b = 0, 1
#     series = []

#     while a <= n:
#         series.append(a)
#         a, b = b, a + b

#     return series

# print(fibonacci(20))

# Function to check prime number.

# def is_prime(n):
#     if n <= 1:
#         return False
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# print("Prime Number:",is_prime(7))
# print("Prime Number Not:",is_prime(10))

# Function to find sum of digits of a number.

# def sum_digits(n):
#     total = 0
#     while n > 0:
#         digit = n % 10
#         total += digit
#         n //= 10
#     return total

# print(sum_digits(123))
# print(sum_digits(405))

# Function to count words in a sentence.

# def count_words(sentence):
#     words = sentence.split()
#     return len(words)

# print(count_words("Python is easy to learn"))
# print(count_words("Hello, My Name is Pradipsinh Jadeja"))

# Function to remove duplicates from list using function.

# def remove_duplicate(lst):
#     unique_list = []
#     for item in lst:
#         if item not in unique_list:
#             unique_list.append(item)
#     return unique_list

# print(remove_duplicate([1,2,3,4,1,2,3,4,5,6,7,8]))  

# Function to sort list without using sort().

# def sort_list(lst):
#     n = len(lst)
#     for i in range(n):
#         for j in range(i + 1, n):
#             if lst[i] > lst[j]:
#                 lst[i], lst[j] = lst[j], lst[i]
#     return lst

# print(sort_list([5,2,8,1,3]))

# Function to convert Celsius to Fahrenheit. formula = celsius (ex.:-25) 25*9/5 + 32 = 77

# def Celsius_Fahrenheit(c):
#     return (c * 9/5) + 32

# print(Celsius_Fahrenheit(25))

# Function to return unique elements from tuple

def unique_tuple(t):
    unique = []
    for item in t:
        if item not in unique:
            unique.append(item)
    return tuple(unique)

print(unique_tuple((1,2,3,4,1,2,3,4,5,6,7,8)))
    