"""
Let's convert a dollar amount into a number of coins. The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. Always break the total into the highest coin value first, resulting in the fewest amount of coins. First convert the dollar amount (1.36) into the total number of pennies (136), then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
"""

""" VERSION 1
dollar_amount = float(input("Enter an amount in dollars: "))

pennies = int(round(dollar_amount * 100))

quarters = pennies // 25
pennies %= 25

dimes = pennies // 10
pennies %= 10

nickels = pennies // 5
pennies %= 5

print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickels: ", nickels)
print("Pennies: ", pennies)
"""

# Version 2
coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

dollar_amount = float(input("Enter an amount in dollars: "))

pennies = int(round(dollar_amount * 100))

# end parameter
# for coin in coins:
#     number_of_coins = pennies // coin[1]
#     pennies %= coin[1]

#     print(coin[0], number_of_coins, end=", ")

# string concatenation
# output = ""
# for coin in coins:
#     number_of_coins = pennies // coin[1]
#     pennies %= coin[1]

#     output += f"{coin[0]} {number_of_coins}, "

# print(output)

# List output
# output = []
# for coin in coins:
#     number_of_coins = pennies // coin[1]
#     pennies %= coin[1]

#     output.append(f"{coin[0]} {number_of_coins}")

# print(", ".join(output))

# dictionary
output = {}
for coin in coins:
    number_of_coins = pennies // coin[1]
    pennies %= coin[1]

    if (number_of_coins):  # if not 0
        output[coin[0]] = number_of_coins


print(output)
