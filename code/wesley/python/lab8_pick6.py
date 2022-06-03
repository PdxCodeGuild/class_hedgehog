import random

def pick6():
    winning_num = []
    for x in range(0,6):
        winning_num.append(random.randint(1,99))
    return(winning_num)

winning_ticket = pick6()

x = 0
balance = 0
ticket = []
while x <= 100000:
    ticket = pick6()
    balance -= 2
    x += 1 
    for num in ticket:
        matches = 0
        if ticket[0] == winning_ticket[0]:
            matches += 1 
    if matches == 1:
        balance += 4
    elif matches == 2:
        balance += 7
    elif matches == 3:
        balance += 100
    elif matches == 4:
        balance += 50000
    elif matches == 5:
        balance += 1000000
    elif matches == 6:
        balance += 25000000

print(balance)

pick6()




