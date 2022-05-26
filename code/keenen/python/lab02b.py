
dollar_amount = float(input('Enter a dollar amount: '))

pennies = dollar_amount * 100

# print(pennies)

# how many times does .25 (quarter) go into variable pennies

quarters = pennies // 25

# print(quarters)

after_quarters = pennies - (quarters * 25)

# print(after_quarters)

# how many times does .10 (dime) go into remainder after variable quarters

dimes = after_quarters // 10

# print(dimes)

after_dimes = after_quarters - (dimes * 10)

# print(after_dimes)

nickels = after_dimes // 5

after_nickels = after_dimes - (nickels * 5)

pennies_remaining = after_nickels // 1

# print(pennies_remaining)

output = f'{int(quarters)} quarter(s), {int(dimes)} dime(s), {int(nickels)} nickel(s), and {int(pennies_remaining)} penny(ies)'

print(output)
