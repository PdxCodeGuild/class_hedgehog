# Make Change
# Let's convert a dollar amount into a number of coins. The input will be the total amount, 
# the output will be the number of quarters, dimes, nickles, and pennies. Always break the 
# total into the highest coin value first, resulting in the fewest amount of coins. First 
# convert the dollar amount (1.36) into the total number of pennies (136), then use floor 
# division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

# Enter a dollar amount: 1.36
# 5 quarters, 1 dime, and 1 penny
# Enter a dollar amount: 0.67
# 2 quarters, 1 dime, 1 nickel, 2 pennies

dollar_amount = float(input("Enter a dollar ammount: \n\t> "))
amount_in_pennies = int(round(dollar_amount * 100)) # I ran into a problem. Multiplying the float returned a number just below the actual value, so I had to round.
quarters = amount_in_pennies // 25
remainder_after_quarters = amount_in_pennies % 25
dimes = remainder_after_quarters // 10
remainder_after_dimes = remainder_after_quarters % 10
nickels = remainder_after_dimes // 5
pennies = remainder_after_dimes % 5
coins = f"""Dollar amount: {dollar_amount} 
Number of quarters: {quarters}
Number of dimes: {dimes}
Number of nickels: {nickels}
Number of pennies: {pennies}"""
print(coins)

# Version 2 (optional)
# Instead of hard-coding the coins, store them in a list of tuples. This way you can make custom coins.
# coins = [
#     ('half-dollar', 50),
#     ('quarter', 25),
#     ('dime', 10),
#     ('nickel', 5),
#     ('penny', 1)
# ]


