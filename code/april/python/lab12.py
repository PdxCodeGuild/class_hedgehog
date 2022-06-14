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

class ATM:
    def __init__(self, 
                account_number="", 
                first_name="", 
                last_name="", 
                balance=0, 
                interest_rate=0.1,
                amount=""):

        self.account_number = account_number
        self.first_name = first_name
        self.last_name = last_name 
        self.balance = balance
        self.interest_rate = interest_rate
        self.amount = amount

    # def account_detail(self):
    #     print("\nAccount Information")
    #     print(f"First Name: {self.first_name()}")
    #     print(f"Last Name: {self.last_name()}")
    #     print(f"Account Number: {self.account_number}")
    #     print(f"Balance: {self.balance}")
    #     print(f"Interest Rate: {self.interest_rate}\n")

    # def __str__(self):
    #     return(f"""
    #     Account Information
    #     First Name: {self.first_name},
    #     Last Name: {self.last_name},
    #     Account Number: {self.account_number},
    #     Balance: {self.balance},
    #     Interest Rate: {self.interest_rate}
    #     """)



    def check_balance(self):
    # Returns account balance
        # return (f"Your Balance is: ${self.balance}")
        return self.balance
        # pass

    def deposit(self, amount):   
    # deposits the given amount to the account
        self.balance += float(amount)
        print(f"Deposited: ${amount}")
        print(f"Current account balance: ${self.balance}")

        # pass
        

    def check_withdrawal(self, amount):
    # returns true if the withdrawn amount won't put the account in the negative
        if amount <= self.balance:
            success = True
        else:
            success =False
        return success


    def withdraw(self, amount):
        # withdraws the amount from the account and returns the amount
        pass

    def calc_interest(self):
        # returns the amount of interest calculated on the account
        pass

# balance = 0
# interest_rate = 0.1

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')


def select_account(accounts):
    print("Select Account: ")
    for i, account in enumerate(accounts):
        print(i, account.account_number)
    selection = input("-> ")
    return int(selection)


accounts = [ATM(12345), ATM(98765)]


menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Exit'
}

while True:
    print()
    for label, option in menu_options.items():
        print(f'{label}. {option}')

    command = input(
        '\nEnter the number of the option you would like to perform\n> ')
    command = menu_options.get(command)

    if command == 'Balance':
        balance = atm.check_balance()  # call the check_balance() method
        print(f"Your Balance is: ${balance}")

    elif command == 'Deposit':
        amount = float(input('How much would you like to deposit? '))
        success = atm.deposit(amount)  # call the deposit(amount) method
        if not success:
            print("Deposit amount must be a positive number.")
        else:
            print(f'Deposited ${amount}')

    elif command == 'Withdraw':
        amount = float(input('How much would you like to withdraw?\n> $'))
        success = atm.check_withdrawal(amount)

        if not success:
            print('Insufficient funds')
        else:
            atm.withdraw(amount)
            print(f'Withdrew ${amount}')

    elif command == 'Interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        atm.deposit(amount)
        print(f'Accumulated ${amount} in interest')

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')



## Version 2 (Optional)

"""Have the ATM maintain a list of transactions. Every time the user makes 
a deposit or withdrawal, add a string to a list saying 'user deposited $15' 
or 'user withdrew $15'. Add a new method `print_transactions()` to your class 
for printing out the list of transactions."""