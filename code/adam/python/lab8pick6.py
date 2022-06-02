
import random




def pick_6():
    import random
    ticket = []
    for x in range(6):
        ticket.append(random.randint(0, 99))
    return ticket


def num_matchers(winning_ticket, rand_ticket):

    matches = 0
    for x in range(len(winning_ticket)):
        if winning_ticket[x] == rand_ticket[x]:
            matches += 1
    return matches



def winner():
    balance = 0
    net_loss = 0
    winning_ticket = pick_6()

    for num in range(100,000):
        net_loss += 2
        ticket = pick_6()
        # winning_matches = 0
        winning_matches = num_matchers(winning_ticket, ticket)

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
            
    
    print(f"You won {balance}, and spent {net_loss}!!")


winner()