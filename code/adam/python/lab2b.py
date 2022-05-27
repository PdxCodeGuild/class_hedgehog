# Enter a dollar amount: 1.36
# 5 quarters, 1 dime, and 1 penny


 
amount = float(input("Enter a dollar amount: "))

#print(type(amount))
amount = int(round(amount * 100))
#print(int(amount))
num_pennies = 0
num_nickels = 0
num_dime = 0
num_quaters = 0


if amount < 0:
    print("""
    
            ---invalid input----
    
    """)
    quit(0)
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

################################################################################################################
################################################################################################################

#####################PART 2#####################################################################################
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]


dollar_amount = float(input("Enter an amount in dollars: "))

pennies  = int(round(dollar_amount * 100))
output = ""
for coin in coins:
    num_of_coins = pennies // coin[1]
    pennies %= coin[1]
    
    
    print(f"{coin[0]} {num_of_coins}")
    
output = {}


# for coin in coins:
#     num_of_coins = pennies // coin[1]
#     pennies %= coin[1]

#     output[coin[0]] = num_of_coins