"""
Pick6 Version 1&2
Have the computer play pick6 many times and determine net balance.

Initially the program will pick 6 random numbers as the 'winner'. Then try playing pick6 100,000 times, with the ticket cost and payoff below.

A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. Order matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. Calculate your net winnings (the sum of all expenses and earnings).

a ticket costs $2
if 1 number matches, you win $4
if 2 numbers match, you win $7
if 3 numbers match, you win $100
if 4 numbers match, you win $50,000
if 5 numbers match, you win $1,000,000
if 6 numbers match, you win $25,000,000
One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.
"""

import random

def the_picks(the_picks):
    the_picks = [random.randint(1, 99) for x in range(0, 6)]
    balance = 0
    winnings = 0
    for _ in range(100000):
        balance -= 2
        next6 = [random.randint(1, 99) for x in range(0, 6)]
        six = [x for x in range(0,6)]
        chk_res = dict(zip(six, the_picks))
        chk_comp = dict(zip(six, next6))
        same_num = 0
        if chk_res[0] == chk_comp[0]:
            same_num += 1
        elif chk_res[1] == chk_comp[1]:
            same_num += 1
        elif chk_res[2] == chk_comp[2]:
            same_num += 1
        elif chk_res[3] == chk_comp[3]:
            same_num += 1    
        elif chk_res[4] == chk_comp[4]:
            same_num += 1
        elif chk_res[5] == chk_comp[5]:
            same_num += 1
        match_winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
        winnings += (match_winnings[same_num])
    print(f"ROI: {(winnings - abs(balance))/abs(balance) *100} %")
    print(f"Total Winnings: {winnings}")
    print(f"Total Expenses: {balance}")
    return (f'Total lost: {abs(balance) - winnings}')
print(the_picks(the_picks))