
from operator import ne
import random
# Pick6
# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Position matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, 
# which can then be used for both the winning numbers and tickets.
# Another function could be num_matches(winning, ticket) 
# which returns the number of matches between the winning numbers and the ticket.

# Steps
# Generate a list of 6 random numbers representing the winning ticket
# Start your balance at 0
# Loop 100,000 times, for each loop:
# Generate a list of 6 random numbers representing the ticket
# Subtract 2 from your balance (you bought a ticket)
# Find how many numbers match
# Add to your balance the winnings from your matches
# After the loop, print the final balance (Hint: This will be negative)
# 
#   Version 2
# The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
# Calculate your ROI, print it out along with your earnings and expenses.



def pick_6():
    import random
    ticket = []
    for x in range(6):
        ticket.append(random.randint(0, 100))
    return ticket


def num_matchers(winning_ticket, rand_ticket):

    matches = 0
    for x in range(len(winning_ticket)):
        if winning_ticket[x] == rand_ticket[x]:
            matches += 1
    return matches

#def ROI():

    # ROI = (new_earnings - new_expenses)/ new_expenses
    # return ROI





def winner():
    balance = 0
    net_loss = 0
    winning_ticket = pick_6()
    total = 0
    for num in range(100000):
        
        net_loss += 2
        ticket = pick_6()
        # winning_ticket = pick_6()
        # winning_matches = 0
        winning_matches = num_matchers(winning_ticket, ticket)
        if winning_matches == 0:
            balance = net_loss
        if winning_matches == 1:
            balance += 4
           
        elif winning_matches == 2:
            balance += 7
            
        elif winning_matches == 3:
            balance += 100
            
        elif winning_matches == 4:
            balance += 50000
           
        elif winning_matches == 5:
            balance += 1000000
           
        elif winning_matches == 6:
           balance += 25000000
        total = balance - net_loss
        
    #ROI(balance, expense)
    print(f"{winning_matches}")
    print(f"You spent ${net_loss} on tickets and won {total}.")
    #print(f"Your return on investment is {ROI()} . ")


winner()