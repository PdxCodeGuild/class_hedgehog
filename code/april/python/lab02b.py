"""
Lab 02b - Make Change
April
25 May 2022
"""

# Convert a dollar amount into a number of coins.The input will be the total 
# amount, the output will be the number of quarters, dimes, nickles, and pennies.
# Always break the total into the highest coin value first, resulting in the fewest 
# amount of coins.

pennies = 0.01 #set value for pennies

total_amount = float(input("Enter a dollar amount: ")) # convert input into a float for use later

# Convert dollar amount into pennies
convert_pennies = total_amount/pennies

total_amount = convert_pennies

quarters = total_amount//25 # use floor division to determine the number of quarters
total_amount = total_amount%25 #use modulus to determine leftover after quarters
dimes = total_amount//10 # use floor division to determine the number of dimes
total_amount = total_amount%10 #use modulus to determine leftover after dimes
nickles = total_amount//5 # use floor division to determine the number of nickles
total_amount = total_amount%5 #use modulus to determine leftover after nickles
pennies = total_amount//1 # use floor division to determine the number of pennies after all other coins

# print the out put of the number of each coin
print(f"{int(quarters)} quarter(s), {int(dimes)} dime(s), {int(nickles)} nickle(s), {int(pennies)} penny/pennies. ")
