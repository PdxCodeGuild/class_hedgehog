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

new_ammt =  input("Enter a dollar amount: ")
new_ammt = float(amount)
new_ammt = new_ammt * 100
new_ammt = int(new_ammt)


print(coins[0][1])
def change(ammt):
 
    if ammt >= 50:
        num = ammt // (coins[0][1])
        ammt = ammt % 10
        return num(coins[0])
    if ammt >= 25:
        (coins[1]) = ammt // (coins[1][1]) 
        ammt = ammt % 10 
        return (coins[1])

print(change(new_ammt))

