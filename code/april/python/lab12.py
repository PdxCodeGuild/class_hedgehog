"""
Lab 12: ATM
April
13 Jun2 2022
"""

"""Let's represent an ATM with a class containing two attributes: a balance and an interest rate. 
A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the 
initializer, as well as the following functions:

-   `check_balance()` returns the account balance
-   `deposit(amount)` deposits the given amount in the account
-   `check_withdrawal(amount)` returns true if the withdrawn amount won't put the account in the negative
-   `withdraw(amount)` withdraws the amount from the account and returns it
-   `calc_interest()` returns the amount of interest calculated on the account

"""

# class ATM:
#     def __init__(self, 
#                 balance=0, 
#                 interest_rate=0.1):

#         self.balance = float(balance)
#         self.interest_rate = float(interest_rate)


#     def check_balance(self):
#     # Returns account balance
#         return self.balance

#     def deposit(self, amount):   
#     # deposits the given amount to the account
#         self.balance += float(amount)
#         return self.balance
        

#     def check_withdrawal(self, amount):
#     # returns true if the withdrawn amount won't put the account in the negative
#         withdrawal = self.balance - amount
#         if withdrawal >= 0:
#             success = True
#         else:
#             success = False
#         return success


#     def withdraw(self, amount):
#         self.balance -= amount
#         return self.balance

#     def calc_interest(self):
#         interest = self.balance * self.interest_rate
#         self.balance += interest
#         return interest


# atm = ATM()  # create an instance of our class
# print("Welcome to the ATM")




# menu_options = {
#     '1': 'Balance',
#     '2': 'Deposit',
#     '3': 'Withdraw',
#     '4': 'Interest',
#     '5': 'Exit'
# }

# while True:
#     print()
#     for label, option in menu_options.items():
#         print(f'{label}. {option}')

#     command = input(
#         "\nEnter the number of the option you would like to perform\n-> ")
#     command = menu_options.get(command)

#     if command == "Balance":
#         balance = atm.check_balance()  # call the check_balance() method
#         print(f"Your Balance is: ${balance:.2f}")

#     elif command == "Deposit":
#         amount = float(input("How much would you like to deposit?\n-> "))
#         success = atm.deposit(amount)  # call the deposit(amount) method
#         if not success:
#             print("Deposit amount must be a positive number.")
#         else:
#             print(f"Deposited: ${amount:.2f}")

#     elif command == "Withdraw":
#         amount = float(input('How much would you like to withdraw?\n> $'))
#         success = atm.check_withdrawal(amount)

#         if not success:
#             print("Insufficient funds")
#         else:
#             atm.withdraw(amount)
#             print(f"Withdrew ${amount:.2f}")

#     elif command == "Interest":
#         amount = atm.calc_interest()  # call the calc_interest() method
#         # atm.deposit(balance) # this give the interest on the deposit amount not the balance #
#         print(f"Accumulated ${amount:.2f} in interest")

#     elif command == "Exit":
#         print("Goodbye!")
#         break

#     else:
#         print("Command not recognized")



##### Version 2 (Optional) #####

"""Have the ATM maintain a list of transactions. Every time the user makes 
a deposit or withdrawal, add a string to a list saying 'user deposited $15' 
or 'user withdrew $15'. Add a new method `print_transactions()` to your class 
for printing out the list of transactions."""

class ATM:
    def __init__(self, 
                balance=0, 
                interest_rate=0.1,
                transactions=[]):

        self.balance = balance
        self.interest_rate = interest_rate
        self.transactions = transactions


    def check_balance(self):
    # Returns account balance
        return self.balance

    def deposit(self, amount):   
    # deposits the given amount to the account
        self.balance += amount
        self.transactions.append(f"You deposited: ${amount:.2f}")
        return self.balance
        

    def check_withdrawal(self, amount):
    # returns true if the withdrawn amount won't put the account in the negative
        withdrawal = self.balance - amount
        if withdrawal >= 0:
            success = True
        else:
            success = False
        return success


    def withdraw(self, amount):
        self.balance -= amount
        self.transactions.append(f"You withdrew:  ${amount:.2f}")
        return self.balance

    def calc_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        # updated to show the interest earned in the transaction history
        self.transactions.append(f"Interest earned: ${interest:.2f}") 
        return interest

    def transaction_history(self):
        for i in self.transactions:
            return self.transactions

   

atm = ATM()  # create an instance of our class
print("Welcome to the ATM")


menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'History',
    '6': 'Exit'
}

while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input(
        "\nEnter the number of the option you would like to perform\n-> ")
    command = menu_options.get(command)

    if command == "Balance":
        balance = atm.check_balance()  # call the check_balance() method
        print(f"Your Balance is: ${balance:.2f}")

    elif command == "Deposit":
        amount = float(input("How much would you like to deposit?\n-> $"))
        success = atm.deposit(amount)  # call the deposit(amount) method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f"Deposited: ${amount:.2f}")

    elif command == "Withdraw":
        amount = float(input('How much would you like to withdraw?\n-> $'))
        success = atm.check_withdrawal(amount)

        if not success:
            print("Insufficient funds")
        else:
            atm.withdraw(amount)
            print(f"Withdrew: ${amount:.2f}")

    elif command == "Interest":
        amount = atm.calc_interest()  
        print(f"Interest: ${amount:.2f}")
    
    elif command == "History":
        balance = atm.check_balance()
        history = atm.transaction_history()
        print("\nTransaction History:\n") # update to print Transaction history nicer
        for item in history:
            print(item)

    elif command == "Exit":
        print("Goodbye!")
        break

    else:
        print("Command not recognized")
