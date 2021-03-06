# ATM
# Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

# check_balance() returns the account balance
# deposit(amount) deposits the given amount in the account
# check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
# withdraw(amount) withdraws the amount from the account and returns it
# calc_interest() returns the amount of interest calculated on the account
class ATM:
    def __init__(self):
        self.balance = 0
        self.interest_rate = 0.001
        self.transactions = []

    def check_balance(self):
        # Returns account balance
        return self.balance

    def deposit(self, amount):
        # deposits he given amount to the account
        self.balance += amount
        self.transactions.append(f"Deposited ${amount}")

    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        return self.balance - amount >= 0

    def withdraw(self, amount):
        # withdraws the amount from the account and returns the amount
        self.balance -= amount
        self.transactions.append(f"Withdrew ${amount}")
        return amount

    def calc_interest(self):
        # returns the amount of interest calculated on the account
        self.transactions.append(f"Added interest")
        return self.interest_rate * self.balance

    def print_transactions(self):
        return self.transactions

atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': 'Print Transactions',
    '6': 'Exit'
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
        print(f'Your balance is ${balance}')

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

    elif command == 'Print Transactions':
        transactions = atm.print_transactions()
        for transaction in transactions:
            print(transaction)

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')
# Version 2 (Optional)
# Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method print_transactions() to your class for printing out the list of transactions.


'''
ATM
Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

check_balance() returns the account balance
deposit(amount) deposits the given amount in the account
check_withdrawal(amount) returns true if the withdrawn amount won't put the account in the negative
withdraw(amount) withdraws the amount from the account and returns it
calc_interest() returns the amount of interest calculated on the account
class ATM:
    def __init__(self):
        pass

    def check_balance(self):
        # Returns account balance
        pass

    def deposit(self, amount):
        # deposits he given amount to the account
        pass

    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        pass

    def withdraw(self, amount):
        # withdraws the amount from the account and returns the amount
        pass

    def calc_interest(self):
        # returns the amount of interest calculated on the account
        pass


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

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
        print(f'Your balance is ${balance}')

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
Version 2 (Optional)
Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method print_transactions() to your class for printing out the list of transactions.
'''
