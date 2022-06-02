"""Pick Six"""

"""
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Position matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000

One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
"""


# Generate a list of 6 random numbers representing the winning ticket
from random import randint


def random_list(nums=6):
    from random import randint
    rand_list = []
    for num in range(nums):
        rand_list.append(randint(1,99))
    return rand_list

def pick_6_prize(check_value):
    if check_value ==1:
        return(1, 4)
    elif check_value ==2:
        return(2, 7)
    elif check_value ==3:
        return(3, 100)
    elif check_value ==4:
        return(4, 50000)
    elif check_value == 5:
        return(5, 1000000)
    elif check_value ==6:
        return(6, 25000000)
    else:
        return(0,0)


def pick_6(user_ticket, winning_ticket):
    check = 0
    #check print statements
    #print(user_ticket, winning_ticket)
    for x in range(len(winning_ticket)):
        if user_ticket[x] == winning_ticket[x]:
            check +=1 
    return(pick_6_prize(check))



list_1= [55, 27, 40, 37, 17, 65]
list_2 = [55, 27, 6, 37, 6, 65]




# Start your balance at 0
balance = 0

winning_ticket = random_list()
"""check, winnings = pick_6(list_1,list_2)
balance += winnings-2"""

# Loop 100,000 times, for each loop:
play_iteration= 100000
while play_iteration != 0:

    # Generate a list of 6 random numbers representing the ticket
    # Find how many numbers match
    check, winnings = pick_6(random_list(), winning_ticket)
    play_iteration -= 1

    # Subtract 2 from your balance (you bought a ticket)
    # Add to your balance the winnings from your matches
    balance += winnings - 2
    print(f" {check} match(es)")

# After the loop, print the final balance (Hint: This will be negative)
print(balance)








