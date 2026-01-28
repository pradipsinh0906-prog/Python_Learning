num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")

choice = int(input("Select operation: "))

oprations = {
    1: num1 + num2,
    2: num1 - num2,
    3: num1 * num2,
    4: num1 / num2
}

print("Result: ", oprations.get(choice, "Invalid opration selected"))

# Second Method:- 

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# op = input("Select operation (+, -, *, /): ")

# if op == '+':
#     print("Result:", a + b)

# elif op == '-':
#     print("Result:", a - b)

# elif op == '*':
#     print("Result:", a * b)

# elif op == '/':
#     if b != 0:
#         print("Result:", a / b)
#     else:
#         print("Error: Cannot divide by zero")

# else:
#     print("Invalid operation selected")
