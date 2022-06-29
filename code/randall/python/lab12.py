#ATM
class ATM:
    def __init__(self):
        self.balance = 0
        self.interest = 0.01

    def check_balance(self):
        # Returns account balance
        return self.balance

    def deposit(self, amount):
        # deposits he given amount to the account
        self.balance += amount
        return self.balance

    def check_withdrawal(self, amount):
        # returns true if the withdrawn amount won't put the account in the negative
        if amount > self.balance:
            return False
        else:
            return True

    def withdraw(self, amount):
        # withdraws the amount from the account and returns the amount
        if self.check_withdrawal(amount):
            self.balance -= amount
            return self.balance
        else:
            print("Insufficient funds")
            
    def calc_interest(self):
        # returns the amount of interest calculated on the account
        self.balance = self.balance + (self.balance * self.interest)
        return self.balance

    def print_transactions(self, amount, transactions):
        pass
        
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
        pass

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')