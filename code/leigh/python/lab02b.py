# lab02b
# Make change
# Leigh Fair-Smiley
# 5/25/2022

coins = [
    ('half-dollar', 50),
    ('quater', 25),
    ('dime', 10),
    ('nickel', 5),
    ('penny', 1)
]

amount = float(input("Enter  dollar amount: "))
amount = int(amount * 100)

for coin in coins:
    print(f"{amount // coin[1]} {coin[0]}, ")
    amount = amount % coin[1]