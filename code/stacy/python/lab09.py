from random import randint

# def advice(hand_value: int):
#     if hand_value <= 17:
#         return f'{hand_value}: Hit!'
#     elif hand_value >= 17 and hand_value < 21:
#         return f'{hand_value}: Stay.'
#     elif hand_value == 21:
#         return 'Stay'
#     else:
#         return f"{hand_value}: Already Busted."
    
# def just_asking_for_advice():
#     first_card = input("Enter your first card: \n\t> ").replace(' ','')
#     if first_card.isnumeric():
#         first_card = int(first_card)
#     elif first_card.upper() == 'A':
#         first_card = 1
#     elif first_card.upper() in ['J', 'Q', 'K']:
#         first_card = 10
#     else:
#         print("Error. Please start over.")
#         return (just_asking_for_advice())
#     second_card = input("Enter your second card: \n\t> ")
#     if second_card.isnumeric():
#         second_card = int(second_card)
#     elif second_card.upper() == 'A':
#         second_card = 1
#     elif second_card.upper() in ['J', 'Q', 'K']:
#         second_card = 10
#     else:
#         print("Error. Please start over.")
#         return (just_asking_for_advice())
#     third_card = input ("Enter your third card: ")
#     if third_card.isnumeric():
#         third_card = int(third_card)
#     elif third_card.upper() == 'A':
#         third_card = 1
#     elif third_card.upper() in ['J', 'Q', 'K']:
#         third_card = 10
#     else:
#         print("Error. Please start over.")
#         return (just_asking_for_advice())
#     hand_value = first_card + second_card + third_card
#     return advice(hand_value)

def advice(hand_value: int):
    if hand_value <= 17:
        return f'{hand_value}: Hit!'
    elif hand_value >= 17 and hand_value <= 21:
        return f'{hand_value}: Stay.'

def draw(deck: list):
    card = deck.pop(randint(0, len(deck)))
    return card

def value(hand: list):
    sum = 0
    for card in hand:
        if card.isnumeric() == True:
            card = int(card)
        elif card.upper() == 'A':
            card = 1
        elif card.upper() in ['J', 'Q', 'K']:
            card = 10
        sum += card
    return sum

def play_blackjack():
    cards = ['A', '2', '3', '4', '5', '6' , '7', '8', '9', 'J', 'Q', 'K']
    deck = []
    deck.extend(cards*4)

    hand = []
    player_hand = 0
    hand.append(draw(deck))
    hand.append(draw(deck))
    player_hand = value(hand)

    keep_drawing = True
    if (player_hand == 21 and len(player_hand) == 2):
        print(f'{player_hand}, Blackjack!')
        keep_drawing = False
    while keep_drawing == True:
        draw_again = input(f'You drew {hand}. Your score is {player_hand}. Would you like to stay, hit, or ask for advice? \n\t> ').lower().replace(' ','')
        if draw_again[0] == 's':    
            keep_drawing = False
        elif draw_again[0] == 'h':
            hand.append(draw(deck))
            player_hand = value(hand)
            if player_hand > 21:
                winner = f'Player busts. Dealer wins.'
                return winner
        elif draw_again[0] == 'a':
            print(advice(player_hand))
        else:
            print("Please choose 'stay', 'draw', or 'advice'.")

    hand = []
    dealer_hand = 0
    hand.append(draw(deck))
    hand.append(draw(deck))
    dealer_hand = value(hand)
    while dealer_hand < 17:
        hand.append(draw(deck))
        dealer_hand = value(hand)
        
    if (player_hand == 21 and len(player_hand) == 2) and not (dealer_hand == 21 and len(dealer_hand) == 2):
        winner = 'Blackjack! Player wins!'
    elif (player_hand == 21 and len(player_hand) == 2) and (dealer_hand == 21 and len(dealer_hand) == 2):
        winner = 'Player and Dealer both got Blackjack! Dealer wins!'
    elif player_hand <= 21 and dealer_hand > 21:
        winner = 'Dealer busts! Player wins!'
    elif player_hand <= 21 and player_hand > dealer_hand:
        winner = f'Player got {player_hand}, Dealer got {dealer_hand}. Player wins!'
    elif player_hand < dealer_hand:
        winner = f'Player got {player_hand} and Dealer got {dealer_hand}. Dealer wins.'
    return winner

def main():
    winner = play_blackjack()
    print(winner)

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