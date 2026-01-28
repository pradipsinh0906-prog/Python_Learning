# # TASK 2: Employee Attendance System
# emp_id = [1,2,3,4]
# emp_names = ("Raj", "Simran", "Aman", "Pooja")
# present_ids = {1, 3}

# attendance = []

# for emp_id, emp_name in zip(emp_id, emp_names):
#     if emp_id in present_ids:
#         status = "Present"
#     else:
#         status = "Absent"
#     attendance.append({
#         "Employee ID": emp_id,
#         "Employee Name": emp_name,
#         "Status": status
#     })

# print(attendance)

# TASK 3: Product Price Merge
# products = ["Laptop", "Mobile", "Tablet"] 
# prices = (50000, 20000, 30000) 
# discounted_products = {"Mobile", "Tablet"}

# product_list = []

# for product, price in zip(products, prices):
#     if product in discounted_products:
#         discount_status = "Yes"
#     else:
#         discount_status = "No"
    
#     product_list.append({
#         "Product": product,
#         "Price": price,
#         "Discounted": discount_status
#     })

# print(product_list)

# TASK 4: Course Enrollment Tracker 

# student_ids = [11, 12, 13]
# courses = ("Python", "Java", "Django")
# enrolled = {11, 13}

# enrolled_list = []

# for student_id, course in zip(student_ids, courses):
#     if student_id in enrolled:
#         status = "Enrolled"
#     else:
#         status = "Not Enrolled"

#     enrolled_list.append({
#         "Student ID": student_id,
#         "Course": course,
#         "Status": status
#     })

# print(enrolled_list)

# TASK 5: Online Order Summary
# order_ids = [501, 502, 503]
# customers = ("Asha", "Vikram", "Rohan")
# delivered_orders = {501, 503}

# order_summary = []

# for order_id, customer in zip(order_ids, customers):
#     if order_id in delivered_orders:
#         status = "Delivered"
#     else:
#         status = "Pending"

#     order_summary.append({
#         "Order Id": order_id,
#         "Customer": customer,
#         "Status": status
#     })

# print(order_summary)

# TASK 6: Exam Result Generator
# roll_no = [21, 22, 23] 
# names = ("Kiran", "Meena", "Rahul") 
# marks = {21: 82, 22: 35, 23: 90}

# result_list = []

# for roll, name in zip(roll_no, names):
#     student_marks = marks.get(roll, 0)
#     if student_marks >= 40:
#         status = "Pass"
#     else:
#         status = "Fail"

#     result_list.append({
#         "Roll No": roll,
#         "Name": name,
#         "Marks": student_marks,
#         "Result": status
#     })

# print(result_list)

# TASK 7: Remove Duplicates & Join 

emails_list = ["a@gmail.com", "b@gmail.com", "a@gmail.com"] 
emails_tuple = ("c@gmail.com", "b@gmail.com")

all_emails = emails_list + list(emails_tuple)

unique_email = list(set(all_emails))

print(unique_email)

# TASK 8: Inventory Stock Checker

# items = ["Pen", "Book", "Pen", "Pencil"]
# stock = {"Pen": 10, "Book": 0, "Pencil": 5}

# unique_item = set(items)

# stock_status = {}

# for item in unique_item:
#     if stock.get(item , 0) > 0:
#         status = "In Stock"
#     else:
#         status = "Out of Stock"

#     stock_status[item] = status

# for item, status in stock_status.items():
#     print(f"{item}: {status}")

# TASK 9: City Temperature Report

# cities = ["Delhi", "Mumbai", "Chennai"]
# temps = (35, 32, 38)
# hot_cities = {"Delhi", "Chennai"}

# temp_report = []

# for city, temp in zip(cities, temps):
#     if city in hot_cities:
#         status = "Hot"
#     else:
#         status = "Normal"

#     temp_report.append({
#         "City": city,
#         "Temperature": temp,
#         "Status": status
#     })

# print(temp_report)

#  TASK 10: Library Book Tracker

book_ids = [101, 102, 103]
titles = ("Python Basics", "Java Mastery", "Django Pro")
issued_books = {102, 103}

library_report = []

for b_id, b_name in zip(book_ids, titles):
    if b_id in issued_books:
        status = "Issued"
    else:
        status = "Available"
    
    library_report.append({
        "Book Id": b_id,
        "Title": b_name,
        "Status": status
    })

print(library_report)