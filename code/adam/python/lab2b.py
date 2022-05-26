# Enter a dollar amount: 1.36
# 5 quarters, 1 dime, and 1 penny


 
amount = input("Enter a dollar amount: ")
amount = float(amount)
#print(type(amount))
amount = amount * 100
#print(int(amount))
num_pennies = 0
num_nickels = 0
num_dime = 0
num_quaters = 0
amount = int(amount)
if amount >= 25:
    num_quaters = amount // 25
    amount = amount % 25
if amount >= 10:
    num_dime = amount // 10
    amount = amount % 10
if amount >= 5:
    num_nickels = amount // 5
    amount = amount % 5
if amount >= 1:
    num_pennies = amount

    
print(f"Quarters {num_quaters}, Dime {num_dime}, Nickels {num_nickels}, Pennies {num_pennies}")




quarter = .25
dime = .10
nickel = .05
penny = .01

