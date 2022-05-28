coins = [
    ('half-dollar', 50),
    ('quarter', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

dollar_amount = input("Enter a dollar amount: ")

dollar_amount = round(float(dollar_amount) * 100)

leftover = dollar_amount

for coin in coins:
    change = leftover//coin[1]
    leftover = leftover - change * coin[1]
    print(f"You have {int(change)} {coin[0]} ")
    