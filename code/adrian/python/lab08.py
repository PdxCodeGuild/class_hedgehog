import random
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



def pick6():
    winning_ticket = []   
    for x in range(0,6):
        i = random.randint(1,99)
        winning_ticket.append(i)

    return winning_ticket

# pick6()

def num_matches(winning, ticket):
    matches = 0
    for x in range(len(winning)):
        if winning[x] == ticket[x]:
            matches += 1
        return matches


winning = pick6()
balance = 0
total = 0


for x in range(100000):
    matches = num_matches(winning, pick6())
    balance -= 2
    if matches == 1:
        total += 4 
    elif matches == 2:
        total += 7
    elif matches == 3:
        total += 100
    elif matches == 4:
        total += 50000
    elif matches == 5:
        total += 1000000
    elif matches == 6:
        total += 25000000
    
print(balance - total)
