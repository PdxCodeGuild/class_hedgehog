from random import randint
def pick6():
    ticket = []
    for x in range(6):
        x = randint(1, 99)
        ticket.append(x)
    return ticket

def num_matches(winning_ticket, player_ticket):
    number_of_matches = 0
    for i, number in enumerate(player_ticket):
        if number == winning_ticket[i]:
            number_of_matches += 1
    return number_of_matches

# def play100000():
#     winning_ticket = pick6()
#     balance = 0
#     for _ in range(100000): 
#         player_ticket = pick6()
#         number_of_matches = num_matches(winning_ticket, player_ticket)   
#         balance -= 2
#         if number_of_matches == 1:
#             balance += 4
#             # print("1 matching number. You won $4!") #This was for testing purposes
#         elif number_of_matches == 2:
#             balance += 7
#             # print("2 matches. You won $7.") #For testing purposes
#         elif number_of_matches == 3:
#             balance += 100
#             print("3 matches! You won $100!")
#         elif number_of_matches == 4:
#             balance += 50000
#             print("4 matches! You won $50,000!")
#         elif number_of_matches == 5:
#             balance += 1000000
#             print("5 matching numbers! You won $1,000,000!")
#         elif number_of_matches == 6:
#             balance += 25000000
#             print("JACKPOT! All numbers match! You won $25,000,000!")
#     return_on_investment = (balance-200000)/200000
#     results = {
#         'Balance': balance,
#         'ROI': return_on_investment
#     }
#     return results

def main():
    payout = {
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }
    outcome_counter = {}
    winning_ticket = pick6()
    balance = 0
    for _ in range(100000): 
        player_ticket = pick6()
        number_of_matches = num_matches(winning_ticket, player_ticket)   
        if number_of_matches not in outcome_counter:
            outcome_counter[number_of_matches] = 1
        else:
            outcome_counter[number_of_matches] += 1
        balance -= 2
        balance += payout.get(number_of_matches, 0)
    return_on_investment = (balance-200000)/200000
    results = {
        'Balance': balance,
        'ROI': return_on_investment
    }
    print(outcome_counter)
    print(results)
    '''
    Pick6
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

    Steps
    Generate a list of 6 random numbers representing the winning ticket
    Start your balance at 0
    Loop 100,000 times, for each loop:
    Generate a list of 6 random numbers representing the ticket
    Subtract 2 from your balance (you bought a ticket)
    Find how many numbers match
    Add to your balance the winnings from your matches
    After the loop, print the final balance
    Version 2
    The ROI (return on investment) is defined as (earnings - expenses)/expenses. Calculate your ROI, print it out along with your earnings and expenses.
    '''

main()
