# class Customer:
#     def __init__(self, name, customer_id):
#         self.name = name
#         self.customer_id = customer_id

#     def get_details(self):
#         return f"Customer [ID: {self.customer_id}, Name: {self.name}]"


# class Account:
#     def __init__(self, account_number, customer, balance=0.0):
#         self.account_number = account_number
#         self.customer = customer
#         self.balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited {amount}. New balance: {self.balance}")
#         else:
#             print("Deposit amount must be positive.")

#     def withdraw(self, amount):
#         if 0 < amount <= self.balance:
#             self.balance -= amount
#             print(f"Withdrew {amount}. New balance: {self.balance}")
#         else:
#             print("Insufficient funds or invalid amount.")

#     def get_balance(self):
#         return self.balance

#     def get_account_details(self):
#         return f"Account [Number: {self.account_number}, Balance: {self.balance}, Customer: {self.customer.get_details()}]"


# class Bank:
#     def __init__(self, name):
#         self.name = name
#         self.accounts = {}

#     def add_account(self, account):
#         self.accounts[account.account_number] = account
#         print(f"Account {account.account_number} added for customer {account.customer.name}.")

#     def get_account(self, account_number):
#         return self.accounts.get(account_number, None)

#     def get_all_accounts(self):
#         return self.accounts.values()


# # Example usage:
# if __name__ == "__main__":
#     # Create customers
#     customer1 = Customer("Alice", 1)
#     customer2 = Customer("Bob", 2)

#     # Create accounts
#     account1 = Account(1001, customer1, 500.0)
#     account2 = Account(1002, customer2, 1000.0)

#     # Create bank and add accounts
#     bank = Bank("MyBank")
#     bank.add_account(account1)
#     bank.add_account(account2)

#     # Perform some operations
#     account1.deposit(200)
#     account1.withdraw(100)
#     account2.deposit(500)
#     account2.withdraw(1500)  # This should print an error message

#     # Print account details
#     print(account1.get_account_details())
#     print(account2.get_account_details())

class Customer:
    def __init__(self, name, customer_id):
        # Initialize customer with name and customer ID
        self.name = name
        self.customer_id = customer_id

    def get_details(self):
        # Return customer details as a string
        return f"Customer [ID: {self.customer_id}, Name: {self.name}]"


class Account:
    def __init__(self, account_number, customer, balance=0.0):
        # Initialize account with account number, customer, and balance
        self.account_number = account_number
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        # Deposit amount to the account
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        # Withdraw amount from the account if sufficient balance is available
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        # Return the current balance of the account
        return self.balance

    def get_account_details(self):
        # Return account details as a string
        return f"Account [Number: {self.account_number}, Balance: {self.balance}, Customer: {self.customer.get_details()}]"


class Bank:
    def __init__(self, name):
        # Initialize bank with name and an empty dictionary of accounts
        self.name = name
        self.accounts = {}

    def add_account(self, account):
        # Add an account to the bank
        self.accounts[account.account_number] = account
        print(f"Account {account.account_number} added for customer {account.customer.name}.")

    def get_account(self, account_number):
        # Retrieve an account by its number
        return self.accounts.get(account_number, None)

    def get_all_accounts(self):
        # Return all accounts in the bank
        return self.accounts.values()


# Example usage:
if __name__ == "__main__":
    # Create customers
    customer1 = Customer("Alice", 1)
    customer2 = Customer("Bob", 2)

    # Create accounts for the customers with initial balances
    account1 = Account(1001, customer1, 500.0)
    account2 = Account(1002, customer2, 1000.0)

    # Create a bank and add the accounts to it
    bank = Bank("MyBank")
    bank.add_account(account1)
    bank.add_account(account2)

    # Perform some operations on the accounts
    account1.deposit(200)  # Deposit money into account1
    account1.withdraw(100)  # Withdraw money from account1
    account2.deposit(500)  # Deposit money into account2
    account2.withdraw(1500)  # Attempt to withdraw more money than available in account2

    # Print account details
    print(account1.get_account_details())  # Print details of account1
    print(account2.get_account_details())  # Print details of account2
    
    
# OOP Features Explained:
# Object-oriented programming (OOP) is a programming paradigm that uses objects and classes to model real-world entities and their interactions. The code snippet demonstrates the following OOP features: 

# Class: A blueprint for creating objects with attributes and methods. In this example, the Customer, Account, and Bank classes are defined as blueprints for creating customer, account, and bank objects, respectively. Each class has attributes (e.g., name, customer_id) and methods (e.g., get_details, deposit) associated with it. 
# Objects: Instances of classes that have specific values for their attributes. In this example, customer1, customer2, account1, account2 are objects created from the Customer and Account classes. 

# Inheritance: 
# The ability to create a new class (subclass) from an existing class (superclass) to reuse code and extend functionality. Polymorphism: The ability to use a common interface for multiple forms (data types). 
# Note: This example does not explicitly demonstrate inheritance or polymorphism, but they can be implemented to extend the functionality of the classes. For example, you could create a SavingsAccount class that inherits from the Account class and overrides the deposit method to include interest calculations.


# Encapsulation: 
# Wrapping data (attributes) and methods (functions) into a single unit (class). 
# Example: The Customer, Account, and Bank classes encapsulate their respective attributes and methods.  


# Abstraction:
# Hiding the complex implementation details and showing only the necessary features. In this example, the deposit and withdraw methods provide a simple interface for depositing and withdrawing money without exposing the internal workings. The code demonstrates the basic principles of OOP in Python through a simple bank system. 



# Inheritance:

# Creating a new class from an existing class to reuse code.
# Note: This example does not explicitly demonstrate inheritance, but it can be extended to include it. For example, you could create a SavingsAccount class that inherits from the Account class.


# Polymorphism:

# The ability to use a common interface for multiple forms (data types).
# Example: The get_details method in the Customer class and the get_account_details method in the Account class both return details, but they are specific to their respective classes.
# This code demonstrates the basic principles of OOP in Python through a simple bank system with customers, accounts, and a bank. The classes encapsulate data and methods, providing a clear structure for modeling real-world entities and interactions. The code also demonstrates abstraction by hiding complex implementation details and providing a simple interface for common operations like depositing and withdrawing money.
# The code can be extended to include inheritance and polymorphism to further enhance the functionality and flexibility of the bank system. For example, you could create specialized account types (e.g., SavingsAccount, CheckingAccount) that inherit from the Account class and override specific methods to handle different types of transactions or calculations. This would demonstrate the power and flexibility of OOP in Python.




