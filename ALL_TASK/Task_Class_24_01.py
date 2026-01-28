# Create a class Student with attributes: id, name.
# Create object and print student details.

# class Student:
#     def __init__(self, id, name):
#         self.id = id
#         self.name = name

#     def display(self):
#         print("Student Id:",self.id)
#         print("Student Name:",self.name) 

# sid = int(input("Enter Student Id: "))
# sname = input("Enter Student Name: ")

# Student1 = Student(sid, sname)

# Student1.display()

# Create a class Calculator with add, subtract, multiply, divide methods.

# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def subtract(self, a, b):
#         return a - b
#     def multiply(self, a, b):
#         return a * b
#     def divide(self, a, b):
#         return a / b
    
# calc = Calculator()

# a = int(input("Enter first Number: "))
# b = int(input("Enter second Number: "))

# print("Add:",calc.add(a, b))
# print("Subtract:",calc.subtract(a, b))
# print("Multiply:",calc.multiply(a, b))
# print("Divide:",calc.divide(a, b))

# Create a class Rectangle with area & perimeter methods.

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
    
#     def area(self):
#         return self.length * self.width
    
# l = float(input("Enter length: "))
# w = float(input("Enter Width: "))

# rect = Rectangle(l, w)

# print("Area of Rectangle:",rect.area())

# Create a class Employee with display method.

# class Employee:
#     def __init__(self, emp_id, name, salary):
#         self.emp_id = emp_id
#         self.name = name
#         self.salary = salary
        
#     def display(self):
#         print("Employee ID:",self.emp_id)
#         print("Employee Name:",self.name)
#         print("Employee Salary:",self.salary)
        
# eid = int(input("Enter Employee ID: "))
# ename = input("Employee Name: ")
# salary = float(input("Enter Employee Salary: "))

# emp_det = Employee(eid, ename, salary)

# emp_det.display()

# Create a class Car and print car details.

# class Car:
#     def __init__(self, car_id, brand, model, price):
#         self.car_id = car_id
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def display(self):
#         print("Car ID: ",self.car_id)
#         print("Brand: ",self.brand)
#         print("Model: ",self.model)
#         print("Price: ",self.price)

# cid = int(input("Enter Car ID: "))
# brand = input("Enter Car Brand: ")
# model = input("Enter Car Model: ")
# price = float(input("Enter Car Price: "))

# car_det = Car(cid, brand, model, price)

# car_det.display()

# Create a class BankAccount with deposit & withdraw.

# class BankAccount:
#     def __init__(self, acc_no, name, balance=0):
#         self.acc_no = acc_no
#         self.name = name
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print("Deposit Amount:", amount)
#         print("Current Balance:",self.balance)
        
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient Balance")
#         else:
#             self.balance -= amount
#             print("Withdrawn Amount:", amount)
#             print("Current Balance:", self.balance)
            
#     def display(self):
#         print("Account No.:",self.acc_no)
#         print("Account Holder:",self.name)
#         print("Balance:",self.balance)
        
# acc_no = input("Enter Account Number: ")
# name = input("Enter Account Holder Name: ")
# balance = float(input("Enter Initial Balance: "))

# account = BankAccount(acc_no, name, balance)

# account.display()

# dep_amt = float(input("Emter Deposit Amount: "))
# account.deposit(dep_amt)

# with_amt = float(input("Enter Withdraw Amount: "))
# account.withdraw(with_amt)

# Create a class Book and display book info.

# class Book:
#     def __init__(self, book_id, title, author, price):
#         self.book_id = book_id
#         self.title = title
#         self.author = author
#         self.price = price
        
#     def display(self):
#         print("Book ID: ",self.book_id)
#         print("Title: ",self.title)
#         print("Author: ",self.author)
#         print("Price: ",self.price)
        
# bid = int(input("Enter Book Id: "))
# title = input("Enter Book Title: ")
# author = input("Enter Author Name: ")
# price = float(input("Enter Book Price: "))

# book_det = Book(bid, title, author, price)

# book_det.display()

# Create a class Mobile and print mobile details.

# class Mobile:
#     def __init__(self, mobile_id, brand, model, price):
#         self.mobile_id = mobile_id
#         self.brand = brand
#         self.model = model
#         self.price = price
    
#     def display(self):
#         print("Mobile ID: ",self.mobile_id)
#         print("Brand: ",self.brand)
#         print("Model: ",self.model)
#         print("Price: ",self.price)
        
# mid = int(input("Enter Mobile ID: "))
# brand = input("Enter Mobile Brand: ")
# model = input("Enter Mobile Model: ")
# price = float(input("Enter Mobile Price: "))

# new_mobile = Mobile(mid, brand, model, price)
        
# new_mobile.display()

# Create a class Laptop and show specifications.

class Laptop:
    def __init__(self, laptop_id, brand, processor, ram , storage, price):
        self.laptop_id = laptop_id
        self.brand = brand
        self.processor = processor
        self.ram = ram
        self.storage = storage
        self.price = price
        
    def display(self):
        print("Laptop ID: ",self.laptop_id)
        print("Brand: ",self.brand)
        print("Processor: ",self.processor)
        print("RAM: ",self.ram)
        print("Storage: ",self.storage)
        print("Price: ",self.price)
        
lid = int(input("Enter Laptop ID: "))
brand = input("Enter Brand: ")
processor = input("Enter Processor: ")
ram = input("Enter RAM (e.g. 8GB): ")
storage = input("Enter Storage (e.g. 512GB SSD): ")
price = float(input("Enter Price: "))

new_laptop = Laptop(lid, brand, processor, ram, storage, price)

new_laptop.display()