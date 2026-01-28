# Demonstrate constructor (_init_).

# class Student:
#     def __init__(self):
#         print("Constructor Called")

# std = Student()

# Demonstrate instance variables & methods.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
        
#     def display(self):
#         print("Name: ",self.name)
#         print("Marks: ",self.marks)
        
#     def result(self):
#         if self.marks >= 40:
#             print("Result: Pass")
#         else:
#             print("Result: Fail")
        
# old_std_det = Student("Pradip", 85)
# new_std_det = Student("Vivek", 30)

# old_std_det.display()
# old_std_det.result()

# print()

# new_std_det.display()
# new_std_det.result()

# Demonstrate class variables.

# class Student:
#     school_name = "Jadeja's School"
    
#     def __init__(self, name):
#         self.name = name
        
#     def display(self):
#         print("Name: ",self.name)
#         print("School Name: ",self.school_name)
        
# s1 = Student("PradipSinh Jadeja")
# s2 = Student("Meetraj Chavda")

# s1.display()
# print()
# s2.display()

# Demonstrate single inheritance.

# class Person:
#     def __init__(self, name):
#         self.name = name
        
#     def show_name(self):
#         print("Name: ",self.name)

# class Student(Person):
#     def __init__(self, name, roll_no):
#         super().__init__(name)
#         self.roll_no = roll_no
    
#     def show_details(self):
#         print("Roll No.: ",self.roll_no)
        
# s1 = Student("Pradip", 101)

# s1.show_name()
# s1.show_details()

# Demonstrate multilevel inheritance.

# class Person:
#     def __init__(self, name):
#         self.name = name 
        
#     def show_name(self):
#         print("Name: ",self.name)

# class Employee(Person):
#     def __init__(self, name, emp_id):
#         super().__init__(name)
#         self.emp_id = emp_id
        
#     def show_emp(self):
#         print("Employee Id:",self.emp_id)
        
# class Manager(Employee):
#     def __init__(self, name, emp_id, department):
#         super().__init__(name, emp_id)
#         self.department = department
        
#     def show_manager(self):
#         print("Department:",self.department)
        
# m1 = Manager("Pradip", 101, "IT")

# m1.show_name()
# m1.show_emp()
# m1.show_manager()

# Demonstrate multiple inheritance.

# class Father:
#     def father_info(self):
#         print("Father Name: Sahdevsinh")
        
# class Mother:
#     def mother_info(self):
#         print("Mother Name: PrakshaBa")
        
# class Child(Father, Mother):
#     def child_info(self):
#         print("Child Name: Pradip")

# c1 = Child()

# c1.father_info()
# c1.mother_info()
# c1.child_info()

# Demonstrate method overriding.

# class Person:
#     def role(self):
#         print("I am a person")
        
# class Student(Person):
#     def role(self):
#         print("I am a Pradip")

# p = Person()
# s = Student()

# p.role()
# s.role()

# Demonstrate encapsulation (private variables).

# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.__balance = balance
        
#     def show_balance(self):
#         print("Balance:",self.__balance)

#     def deposit(self, amount):
#         self.__balance += amount
#         print("Amount Deposited")
        
# acc = BankAccount("Pradip", 5000)

# print("Name:",acc.name)

# acc.show_balance()
# acc.deposit(2000)
# acc.show_balance()

# Demonstrate getter & setter methods.

# class Student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.__marks = marks
    
#     def get_marks(self):
#         return self.__marks
    
#     def set_marks(self, marks):
#         if marks >= 0 and marks <= 100:
#             self.__marks = marks
#         else:
#             print("Invaild marks")
            
# s1 = Student("Pradip", 85)

# print("Marks:",s1.get_marks())

# s1.set_marks(95)
# print("Updated Marks:",s1.get_marks())

# s1.set_marks(150)

# Demonstrate polymorphism.

class Animal:
    def sound(self):
        print("Animal Make a sound")
        
class Dog(Animal):
    def sound(self):
        print("Dog Barks")
        
class Cat(Animal):
    def sound(self):
        print("Cat Meows")
        
animals = [Dog(), Cat(), Animal()]

for a in animals:
    a.sound()