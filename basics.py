class BankAccount:
    def __init__(self,name,phone,address):
        self.AccountHolderName = name
        self.AccountHolderPhone = phone
        self.AccountHolderAddress = address
        self.CurrentBalance = 0

    def display_balance(self):
        return f"Your balance is {self.CurrentBalance}"
    
    def deposit(self,amount):
        self.CurrentBalance += amount
        return f"Amount deposited Successfully. Your new balance is {self.CurrentBalance}"
    
    def withdraw(self,amount):
        if amount > self.CurrentBalance:
            print("Insufficient funds")
        else:
            self.CurrentBalance -= amount
        return f"Amount withdrawn Successfully. Your new balance is {self.CurrentBalance}"

account1 = BankAccount("John Doe","1234567890","123 Main St")

print(account1.AccountHolderName)
print(account1.AccountHolderAddress)
print(account1.AccountHolderPhone)
print(account1.CurrentBalance)
print(account1.display_balance())
print(account1.deposit(100))
print(account1.withdraw(50))        