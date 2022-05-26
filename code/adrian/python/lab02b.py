# Let's convert a dollar amount into a number of coins. 
# The input will be the total amount, the output will be the number of quarters, dimes, nickles, and pennies. 
# Always break the total into the highest coin value first, resulting in the fewest amount of coins. 
# First convert the dollar amount (1.36) into the total number of pennies (136), 
# then use floor division //, which throws away the remainder. 10/3 is 3.333333, 10//3 is 3.


total_amount = float(input("Enter a dollar amount: "))
cents = float(total_amount * 100)

quarter = cents//25
cents = cents%25

dime = cents//10
cents = cents%10

nickel = cents//5
cents = cents%5

penny = cents//1
cents = cents%1

print(f'{quarter} quarters \n{dime} dimes \n{nickel} nickels \n{penny} pennies\n')