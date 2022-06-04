import random

def pick6():
    ticket = []
    for x in range(6):
        ticket.append(random.randint(1, 99))

    # print(ticket)
    return ticket
    
def play_100k(winning_ticket, number_of_tix):
    # winning_ticket = pick6()
    print(f'\nYour winning numbers are:  {winning_ticket}\n')
    balance = 0
    earnings = 0
   
    for x in range (number_of_tix):
        new_ticket = pick6()
        balance -= 2
        matches = 0
        # print(f'Lottery numbers drawn are: {new_ticket}')
        for x in range(len(winning_ticket)):
            if new_ticket[x] == winning_ticket[x]:
                matches += 1

        # print('matches: ', matches)
        # print('balance: ', balance)

        if matches == 1:
            earnings += 4
        elif matches  == 2:
            earnings += 7
        elif matches == 3:
            earnings += 100
        elif matches == 4:
            earnings += 50000
        elif matches == 5:    
            earnings += 1000000
        elif matches == 6:
            earnings += 25000000
        # earnings += balance
    # print('matches: ', matches)
    balance = balance * -1
    print(f'balance: -${balance}')
    print(f'earnings: ${earnings}')
    expenses = balance * -1
    # print(expenses)
    roi = (earnings - expenses)/expenses
    print(f'ROI: {roi}')

num_of_tix = int(input('\nEnter the number of tickets you would like to purchase: '))

the_winner = pick6()
# the_winner = [3, 3, 3, 3, 3, 3]
play_100k(the_winner, num_of_tix)
