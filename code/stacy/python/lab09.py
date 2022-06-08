
def advice(hand_value):
    if hand_value <= 17:
        return f'{hand_value}: Hit!'
    elif hand_value >= 17 and hand_value < 21:
        return f'{hand_value}: Stay.'
    elif hand_value == 21:
        return 'Blackjack!'
    else:
        return f"{hand_value}: Already Busted."

def just_asking_for_advice():
    first_card = input("Enter your first card: \n\t> ").replace(' ','')
    if first_card.isnumeric():
        first_card = int(first_card)
    elif first_card.upper() == 'A':
        first_card = 1
    elif first_card.upper() in ['J', 'Q', 'K']:
        first_card = 10
    else:
        print("Error. Please start over.")
        return (just_asking_for_advice())
    second_card = input("Enter your second card: \n\t> ")
    if second_card.isnumeric():
        second_card = int(second_card)
    elif second_card.upper() == 'A':
        second_card = 1
    elif second_card.upper() in ['J', 'Q', 'K']:
        second_card = 10
    else:
        print("Error. Please start over.")
        return (just_asking_for_advice())
    third_card = input ("Enter your third card: ")
    if third_card.isnumeric():
        third_card = int(third_card)
    elif third_card.upper() == 'A':
        third_card = 1
    elif third_card.upper() in ['J', 'Q', 'K']:
        third_card = 10
    else:
        print("Error. Please start over.")
        return (just_asking_for_advice())
    hand_value = first_card + second_card + third_card
    return advice(hand_value)

def play_blackjack():

    pass

def main():
    print(just_asking_for_advice())

main()

'''
Blackjack Advice
Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

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
Version 2 (optional)
Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand. Try generating a list of all possible hand values by doubling the number of values in the output whenever you encounter an ace. For one half, add 1, for the other, add 11. This ensures if you have multiple aces that you account for the full range of possible values.
'''