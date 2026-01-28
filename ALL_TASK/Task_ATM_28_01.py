class ATM:
    def __init__(self):
        self.balance = 50000
        self.pin = "2365"
        
    def check_pin(self):
        entered_pin = input("Enter your ATM PIN: ")
        if entered_pin == self.pin:
            return True
        else:
            print("PIN is Wrong!")
            
    def check_balance(self):
        print(f"Current Balance: {self.balance:,}")
        
    def deposit(self):
        amount = int(input("Enter amount to deposit : ₹"))
        if amount > 0:
            self.balance += amount
            print("Amount Deposited Successfully.")
            self.check_balance()
        else:
            print("Invaild Amount!")
    
    def withdraw(self):
        amount = int(input("Enter amount to withdraw : ₹"))
        if amount <= 0:
            print("Invaild Amount")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Please Collect Your Cash")
            self.check_balance()
    
    def start_atm(self):
        if not self.check_pin():
            return
        
        while True:
            print("\n ATM MENU")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            
            choice = input("Enter you choice (1-4): ")
            
            if choice == "1":
                self.check_balance()
            elif choice == "2":
                self.deposit()
            elif choice == "3":
                self.withdraw()
            elif choice == "4":
                print("Thank You for using ATM")
                break
            else:
                print("Invaild Choice")
            
atm = ATM()
atm.start_atm()