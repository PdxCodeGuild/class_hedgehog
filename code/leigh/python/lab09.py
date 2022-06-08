# Lab 09
# blackjack advice
# Leigh Fair-Smiley
# 6/7/2022

"""
Let's write a python program to give basic blackjack
 playing advice during a game by asking the player
  for cards. First, ask the user for three playing
   cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
   Then, figure out the point value of each card individually.
    Number cards are worth their number, all face cards are worth 10. 
    At this point, assume aces are worth 1. Use the following rules 
    to determine the advice:

    Less than 17, advise to "Hit"
    Greater than or equal to 17, but less than 21, advise to "Stay"
    Exactly 21, advise "Blackjack!"
    Over 21, advise "Already Busted"
"""

def collect_cards():
    cards = []
    cards.append(input("What's your first card? "))
    cards.append(input("What's your second card? "))
    cards.append(input("What's your third card? "))
    return cards
    
def advice(total):
    if total < 17:
        print(total, "Hit")
    elif 17 <= total < 21:
        print(total, "Stay")
    elif total == 21:
        print(total, "Blackjack!")
    else:
        print(total, "Already Busted")

def main():
    cards = collect_cards()
    total = 0
    aces = 0
    for card in cards:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            num_aces += 1
        else:
            total += int(card)
    for ace in range(aces):
        if total + 11 <= 21:
            total += 11
        else:
            total += 1
    advice(total)


main()
