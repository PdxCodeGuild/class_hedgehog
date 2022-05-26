quarter = 25
dime = 10
nickel = 5
penny = 1

dollar_amount = input("Enter a dollar amount: ")

dollar_amount = float(dollar_amount) * 100

quarters = dollar_amount//quarter

leftover = dollar_amount - quarters * 25

dimes = leftover//dime

leftover_2 = leftover - dimes * 10

nickels = leftover_2//nickel

leftover_3 = leftover_2 - nickels * 5

pennies = leftover_3//penny

print(f"{int(quarters)} quarters, {int(dimes)} dimes, {int(nickels)} nickels and {int(pennies)} pennies")
