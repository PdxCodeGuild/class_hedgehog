"""Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"
Print out the current total point value and the advice.

What's your first card? Q
What's your second card? 2
What's your third card? 3
15 Hit

What's your first card? K
What's your second card? 5
What's your third card? 5
20 Stay

What's your first card? Q
What's your second card? J
What's your third card? A
21 Blackjack!
"""
values = {"K":10,"Q":10,"J":10,"10":10,"9":9,"8":8,"7":7,"6":6,"5":5,"4":4,"3":3,"2":2,"A":1}


"""def blackjack_advice():
    hand = []
    total = 0
    while len(hand) <3:
        player_input = input("Please enter your number card, or the FIRST letter of a face card: ").upper()
        if player_input not in values.keys():
            print("That is not an option, please try again")
            continue
        else:
            hand.append(player_input)
    # Less than 17, advise to "Hit"
    # Greater than or equal to 17, but less than 21, advise to "Stay"
    # Exactly 21, advise "Blackjack!"
    # Over 21, advise "Already Busted"

    total = sum([values[c] for c in hand])
    if total >21:
        return f"{total}, Already busted."
    elif total == 21:
        return f"{total}, Blackjack!"
    elif total in range(17,21):
        return f"{total}, I would suggest staying."
    else:
        return f"{total}, I would suggest a hit."

print(blackjack_advice())"""

    

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"


"""Version 2"""

def blackjack_advice():
    hand = []
    total = 0
    while len(hand) <3:
        player_input = input("Please enter your number card, or the FIRST letter of a face card: ").upper()
        if player_input not in values.keys():
            print("That is not an option, please try again")
            continue
        else:
            hand.append(player_input)
    
    total = sum([values[c] for c in hand])
# Added in for loop, checks for "A" in hand and adds in 10. I cannot think of a need for an actual for loop in this to check every card since you could only ever benefit from one Ace being counted as elevel at a time, but it felt more complete to me so it stays
    #if "A" in hand and total <=11:
    #    total+=10
    for x in hand:
        if x =="A" and total <=11:
            total += 10

    if total >21:
        return f"{total}, Already busted."
    elif total == 21:
        return f"{total}, Blackjack!"
    elif total in range(17,21):
        return f"{total}, I would suggest staying."
    else:
        return f"{total}, I would suggest a hit."

print(blackjack_advice())








