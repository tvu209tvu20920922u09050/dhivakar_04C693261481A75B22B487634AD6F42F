'''implenent a class called BankAccount that represents a bank the class should have private
attributes for accounrt number, account holder name, and account balance.Include method to
deposite money,withdraw money,and display the account balance. Ensure that the account balance
cannot be accessed directly from outside the claaa. Write a program to create an instance of the 
BankAccount class and test thge deposite and withdrawal functionlity.'''


class BankAccount:

  def __init__(self, account_number, account_holder_name, 
                                        initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name 
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited ₹{}. New balance: ₹{}".format(amount, 
                                      self.__account_balance))

    else:
      print("Invalid deposit amount")

  def withdraw(self, amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdrew ₹{}. New balance: ₹{}".format(amount, 
                                       self.__account_balance))

    else:
      print("Invalid withdrawal amount")

  def display_balance(self):
    print("account balance for {} (Account #{}): ₹{}".format(
        self.__account_holder_name, self.__account_number,
        self.__account_balance))
    
#Create an object for the BankAccount class
account=BankAccount(account_number="987654321",  
                    account_holder_name="Hari prabu",
                    initial_balance=6000.0)

#Test the deposit and withdrawal functions
account.display_balance()
account.deposit(1000.0)
account.withdraw(500.0)
account.display_balance()