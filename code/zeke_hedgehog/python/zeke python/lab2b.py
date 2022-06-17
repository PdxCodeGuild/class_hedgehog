""" 
Let's convert a dollar amount into a number of coins. The input will be the total amount, 
the output will be the number of quarters, dimes, nickles, and pennies.
 
Always break the total into the highest coin value first, resulting in the fewest amount of coins.
First convert the dollar amount (1.36) into the total number of pennies (136), 
then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.

Enter a dollar amount: 1.36
5 quarters, 1 dime, and 1 penny
Enter a dollar amount: 0.67
2 quarters, 1 dime, 1 nickel, 2 pennies


"""


#Variables
quarter = 25
dime = 10
nickel = 5
penny = 1


# print(type(quarter))

amount = float(input('Enter a dollar amount: '))
print(amount)

# covert into pennies
# use floor division to determine the number of quarters
# extract 25 from amount


#total amount
penny = int(round(100 * amount))
#floor division of amount by 25
quarter = penny // 25
# Modulo- take whats left over after the quarters 
# and do floor division by 10
dime = (penny % 25) // 10
# Modulo- take whats left over after the dimes a
# and do floor division by 5
nickel = (penny % 25 % 10) // 5
# Modulo- take whats left over after the nickel a
# and do floor division by 1
pennies = (penny % 25 % 10 % 5) // 1




print(f'{quarter} quarters, {dime} dimes, {nickel} nickels, {pennies} pennies')






