# Have the computer play pick6 many times and determine net balance.

# Initially the program will pick 6 random numbers as the 'winner'. 
# Then try playing pick6 100,000 times, with the ticket cost and payoff below.

# A ticket contains 6 numbers, 1 to 99, and the number of matches between the ticket and the winning numbers determines the payoff. 
# Position matters, if the winning numbers are [5, 10] and your ticket numbers are [10, 5] you have 0 matches. 
# If the winning numbers are [5, 10, 2] and your ticket numbers are [10, 5, 2], you have 1 match. 
# Calculate your net winnings (the sum of all expenses and earnings).

# a ticket costs $2
# if 1 number matches, you win $4
# if 2 numbers match, you win $7
# if 3 numbers match, you win $100
# if 4 numbers match, you win $50,000
# if 5 numbers match, you win $1,000,000
# if 6 numbers match, you win $25,000,000
# One function you might write is pick6() which will generate a list of 6 random numbers, which can then be used for both the winning numbers and tickets. 
# Another function could be num_matches(winning, ticket) which returns the number of matches between the winning numbers and the ticket.

import random


def pick6():
    winning_ticket = []   
    for _ in range(6):
        winning_ticket.append(random.randint(1, 99))

    return winning_ticket

# pick6()

def num_matches(winning, current):
    matches = 0
    for x in range(6):
        if winning[x] == current[x]:
            matches += 1

    return matches


def main():
    payout = {
        1: 4,
        2: 7,
        3: 100,
        4: 50_000,
        5: 1_000_000,
        6: 25_000_000
    }

    outcome = {}
    
    winning = pick6()

    cost = 0
    profit = 0
    
    for _ in range(100_000):

        ticket = pick6()

        cost += 2

        matches = num_matches(winning, ticket)
        if matches not in outcome:
            outcome[matches] = 1
        else:
            outcome[matches] += 1

        profit += payout.get(matches, 0)

    print(f"Balance: ${profit - cost}")
    print(f"ROI: {(profit - cost) / cost}")
    print(outcome)


if __name__=="__main__":
    main()