username = input("Enter your username: ")
password = input("Enter your password: ")

# fixed_username = "admin"
# fixed_password = "admin123"

if username == "admin" and password == "admin123":
    print("Login Successful!")

elif username != "admin" and password != "admin123":
    print("Invalid username and password.")

elif username != "admin":
    print("Invalid username.")

else:
    print("Invalid password.")