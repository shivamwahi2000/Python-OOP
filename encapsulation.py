class BankAccount:
    def __init__(self,name,phone,address):
        self.__AccountHolderName = name
        self.__AccountHolderPhone = phone
        self.__AccountHolderAddress = address
        self.__CurrentBalance = 0
        self.__withdrawalLimit = 200000

    def displayBalance(self):
        return f"Your balance is {self.__CurrentBalance}"
    
    def deposit(self,amount):
        self.__CurrentBalance += amount
        return f"Amount deposited Successfully. Your new balance is {self.__CurrentBalance}"
    
    def withdraw(self,amount):
        if amount > self.__CurrentBalance:
            print("Insufficient funds")
        else:
            self.__CurrentBalance -= amount
        return f"Amount withdrawn Successfully. Your new balance is {self.__CurrentBalance}"
    
    def getAccountDetails(self):
        return f"Account Holder Name: {self.__AccountHolderName}\nAccount Holder Phone: {self.__AccountHolderPhone}\nAccount Holder Address: {self.__AccountHolderAddress}"

    def getWithdrawalLimit(self):
        print(f"Your withdrawal limit is {self.__withdrawalLimit}")
        return self.setWithdrawalLimit()

    def setWithdrawalLimit(self):
        print("Do you want to change it?\nPress 1 for Yes\nPress 2 for No")
        choice = int(input())
        if choice == 1:
            newLimit = int(input("Enter new withdrawal limit: "))
            self.__withdrawalLimit = newLimit
            return "Withdrawal limit changed successfully"
        else:
            return f"Thanks for Opting XYZ Banking Services."


account1 = BankAccount("John Doe","1234567890","123 Main St")

#Following lines will throw error because of private attributes
# print(account1.AccountHolderName)
# print(account1.AccountHolderAddress)
# print(account1.AccountHolderPhone)
# print(account1.CurrentBalance)

print(account1.displayBalance())
print(account1.deposit(100))
print(account1.withdraw(50))  
print(account1.getAccountDetails())      

account2 = BankAccount("Radha","0987654321","456 Main St")

print(account2.displayBalance())
#print(account2.withdrawlLimit) # This will throw error because of private attribute
print(account2.deposit(100000))

print(account2.getWithdrawalLimit())


