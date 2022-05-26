# lab02b
# Make change
# Leigh Fair-Smiley
# 5/25/2022

amount = float(input("Enter  dollar amount: "))
amount = int(amount * 100)

print(f"""{amount // 25} quarters,
{(amount % 25) // 10} dimes,
{(amount % 25 % 10) // 5} nickles,
{amount % 5} pennies
""")