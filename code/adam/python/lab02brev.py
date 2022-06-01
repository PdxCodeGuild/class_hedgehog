

# dollar_amount = float(input("Enter an amount in dollars: "))

# pennies  = int(round(dollar_amount * 100))

# quarters = pennies // 25
# pennies %= 25
# dimes = pennies // 10 
# pennies %= 10
# nickels = pennies // 5
# pennies %= 5

# print("Quarters:", quarters)
# print("Dimes:", dimes)
# print("Nickels:", nickels)
# print("Pennies:", pennies)


####################PART2#####################################################################################

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





    




