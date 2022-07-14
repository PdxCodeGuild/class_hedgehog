# Lab 12: ATM

"""Let's represent an ATM with a class containing two attributes: a balance and an interest rate. A newly created account will default to a balance of 0 and an interest rate of 0.1%. Implement the initializer, as well as the following functions:

-   `check_balance()` returns the account balance
-   `deposit(amount)` deposits the given amount in the account
-   `check_withdrawal(amount)` returns true if the withdrawn amount won't put the account in the negative
-   `withdraw(amount)` withdraws the amount from the account and returns it
-   `calc_interest()` returns the amount of interest calculated on the account

```python"""
class ATM:
    def __init__(self, balance=0, interest_rate= 0.001):
        self.balance =  balance
        self.interest_rate = interest_rate
        self.transactions = []


    def check_balance(self):
        return round(self.balance, 2)

    def deposit(self, amount):
        if amount >0:
            self.balance = self.balance + amount
            self.transactions.append(f"User deposited ${amount}")
            return self.balance
        else:
            return False    
        
    def check_withdrawal(self, amount):
        if (self.balance - amount) >= 0:
            return True

    def withdraw(self, amount):
        # withdraws the amount from the account and returns the amount
        self.balance = self.balance - amount
        self.transactions.append(f"User withdrew ${amount}")
        return self.balance
       

    def calc_interest(self):
        # returns the amount of interest calculated on the account
        interest_balance = (self.balance*self.interest_rate)
        self.balance = self.balance + interest_balance
        self.transactions.append(f"User earned ${interest_balance} from interest")
        return interest_balance
        

    def __str__(self):
        for transaction in self.transactions:
            print(transaction)


atm = ATM()  # create an instance of our class
print('Welcome to the ATM')

menu_options = {
    '1': 'Balance',
    '2': 'Deposit',
    '3': 'Withdraw',
    '4': 'Interest',
    '5': "Print transactions",
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
        try:
            amount = float(input('How much would you like to deposit? '))
            success = atm.deposit(amount)  # call the deposit(amount) method
            if not success:
                print("Deposit amount must be a positive number.")
            else:
                print(f'Deposited ${amount}')
        except ValueError:
            print("Invalid amount")


    elif command == 'Withdraw':
        try:
            amount = float(input('How much would you like to withdraw?\n> $'))
            success = atm.check_withdrawal(amount)


            if not success:
                print('Insufficient funds')
            else:
                atm.withdraw(amount)
                print(f'Withdrew ${amount}')
        except ValueError:
            print("Invalid amount")

    elif command == 'Interest':
        amount = atm.calc_interest()  # call the calc_interest() method
        print(f'Accumulated ${amount} in interest')

    elif command == "Print transactions":
        try:
            print(atm)
        except TypeError:
            print("End of transactions.")
    

    elif command == 'Exit':
        print("Goodbye!")
        break

    else:
        print('Command not recognized')



## Version 2 (Optional)

"""Have the ATM maintain a list of transactions. Every time the user makes a deposit or withdrawal, add a string to a list saying 'user deposited $15' or 'user withdrew $15'. Add a new method `print_transactions()` to your class for printing out the list of transactions."""

