# Lab 08
# Pick 6
# Leigh Fair-Smiley
# 6/1/2022

import random
from typing import NewType

def pick6():
    ticket = []
    for x in range(6):
        ticket.append(random.randint(1, 99))
    
    return ticket

def num_matches(winning_ticket, new_ticket):
    matches = 0
    for x in range(len(winning_ticket)):
        if winning_ticket[x] == new_ticket[x]:
            matches += 1
    return matches

def main():
    winning_ticket = pick6()
    total_cost = 0
    total_profit = 0
    for x in range(100000):
        total_cost += 2
        matches = num_matches(winning_ticket, pick6())
        if matches == 6:
            total_profit += 25000000
        elif matches == 5:
            total_profit += 1000000
        elif matches == 4:
            total_profit += 50000
        elif matches == 3:
            total_profit += 100
        elif matches == 2:
            total_profit += 7
        elif matches == 1:
            total_profit += 4
    print(f"Final balance = {total_profit - total_cost}")
    print(f"ROI = {(total_profit - total_cost) / total_cost}")    

main()