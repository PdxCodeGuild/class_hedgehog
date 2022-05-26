"""
Lab_02B.1
make change
"""

"""
Let's convert a dollar amount into a number of coins. The input will be the total amount, 
the output will be the number of quarters, dimes, nickles, and pennies. Always break the total 
into the highest coin value first, resulting in the fewest amount of coins.
"""

#create store of values. Could also use a dictionary I reckon


coin_list = [('golden dollar coin',100),('half-dollar', 50),('quarter', 25),('dime', 10),('nickel', 5),('penny', 1)]
coin_quantity = {'golden dollar coin': 0, 'half-dollar': 0, 'quarter': 0, 'dime':0, 'nickel': 0, 'penny':0}

#Get value and convert into pennies
value = float(input("Hello! please enter a dollar amount in the format of '0.00': "))
while value < 0.01 :
    value = float(input("Please choose a positive value, or a value greater than 0. Also, no fractions of a penny please: "))
value = value*100
#various coin value calculations. 

for x in coin_list:
    coin_quantity[x[0]] = int(value // x[1])
    value %= x[1]

#Old code for reference

# coin_quantity['quarter'] = int(value //coin_list[2][1])
# value %= coin_list[2][1]            
# coin_quantity['dime'] = int(value //coin_list[3][1])
# value %= coin_list[3][1]   
# coin_quantity['nickel'] = int(value //coin_list[4][1])
# value %= coin_list[4][1]  
# coin_quantity['penny'] = int(value //coin_list[5][1])
# value %= coin_list[5][1]

print(f"{coin_quantity['golden dollar coin']} golden dollar(s), {coin_quantity['half-dollar']} half-dollar(s), {coin_quantity['quarter']} quarter(s), {coin_quantity['dime']} dime(s), {coin_quantity['nickel']} nickel(s), {coin_quantity['penny']} {'penny' if coin_quantity['penny']==1 else 'pennies'}.")
