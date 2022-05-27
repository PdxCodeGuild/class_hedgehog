# Version 2 (optional)
# Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.

coins = [
    ('dollar', 100), 
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]
dollar_amount = float(input("Enter a dollar ammount: \n\t> "))
amount_in_pennies = int(round(dollar_amount * 100))
dollars = amount_in_pennies // coins[0][1]
remainder = amount_in_pennies % coins[0][1]
half_dollars = remainder // coins[1][1]
remainder = remainder % coins[1][1]
quarters = remainder // coins[2][1]
remainder = remainder % coins[2][1]
dimes = remainder // coins[3][1]
remainder = remainder % coins[3][1]
nickels = remainder // coins[4][1]
pennies = remainder % coins[4][1]

coins = f"""dollars coins: {dollars}
half-dollars: {half_dollars} 
quarters: {quarters}
dimes: {dimes}
nickels: {nickels}
pennies: {pennies}"""
print (coins)
