import random

def pick6():
    winning_num = []
    for x in range(0,6):
        winning_num.append(random.randint(1,99))
    return(winning_num)

winning_ticket = pick6()

x = 0
expenses = 0
ticket = []
earnings = 0
while x <= 100000:
    ticket = pick6()
    expenses -= 2
    x += 1 
    for num in ticket:
        matches = 0
        if ticket[0] == winning_ticket[0]:
            matches += 1 
    if matches == 1:
        earnings += 4
    elif matches == 2:
        earnings += 7
    elif matches == 3:
        earnings += 100
    elif matches == 4:
        earnings += 50000
    elif matches == 5:
        earnings += 1000000
    elif matches == 6:
        earnings += 25000000

print(f'{earnings} -this is your earnings')
print(f'{expenses} -this is your expenses')
print(f"{(earnings - expenses)/expenses} -this is your ROI")






