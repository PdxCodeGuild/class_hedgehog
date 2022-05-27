"""
Let's convert a dollar amount into a number of coins. 
The input will be the total amount, the output will be
the number of quarters, dimes, nickles, and pennies. 
Always break the total into the highest coin value 
first, resulting in the fewest amount of coins. 
First convert the dollar amount (1.36) into the total
number of pennies (136), then use floor division //, 
which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.
"""
user_input = float(input("Enter a dollar amount including cents (eg.. 4.38): "))

total_pennies = round(user_input*100)

quarters = total_pennies//25
t = total_pennies%25

dimes = t//10
t = t%10

nickels = t//5
t = t%5

pennies = t

print(f"You entered {user_input}. Total change for this amount is: {quarters} quarters, {dimes} dimes, {nickels} nickels, {pennies} pennies")