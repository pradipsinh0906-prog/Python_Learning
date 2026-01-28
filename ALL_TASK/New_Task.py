# Q1 : Greater number among two numbers.

#  a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# if a > b :
#     print("a is greater than b")
# else:
#     print("b is greater than a")

# Q2 : Male or Female
# a = input("Enter your gender (M/F): ")

# if a == "M" or a == "m" or a == "Male" or a == "male":
#     print("Good Morning Sir")
# elif a == "F" or a == "f" or a == "Female" or a == "female":
#     print("Good Morning Ma'am")
# else:
#     print("Invalid Input")

# Q3 : Even or Odd
# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("This is an Even number")
# else:
#     print("This is an Odd number")

# Q4 : Age conditon

# age = int(input("Enter your age: "))

# if age >= 1 and age <= 17:
#     print("It's Children")
# elif age >= 18 and age <= 30:
#     print("It's Adult")
# elif age >= 31 and age <= 60:
#     print("It's Senior Citizen")
# elif age >= 61 and age <= 100:
#     print("It's Super Senior Citizen")
# else:
#     print("Invalid age")


# Q5 : winter temperature

temp = int(input("Enter the temperature in Celsius: "))

if temp < 0:
    print("It's Freezing weather")
elif temp >= 0 and temp < 10:
    print("It's Freezing Cold weather")
elif temp >= 10 and temp < 20:
    print("It's Freezing very Cold weather")
elif temp >= 20 and temp < 30:
    print("It's Normal weather")
elif temp >= 30 and temp < 40:
    print("It's Hot weather")
elif temp >= 40:
    print("It's Very Hot weather")
