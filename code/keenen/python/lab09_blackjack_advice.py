# Blackjack Advice


# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Print out the current total point value and the advice.

# * Less than 17, advise to "Hit"
# * Greater than or equal to 17, but less than 21, advise to "Stay"
# * Exactly 21, advise "Blackjack!"
# * Over 21, advise "Already Busted"
# ```
# What's your first card? Q
# What's your second card? 2
# What's your third card? 3
# 15 Hit

# What's your first card? K
# What's your second card? 5
# What's your third card? 5
# 20 Stay

# What's your first card? Q
# What's your second card? J
# What's your third card? A
# 21 Blackjack!
# ```

# ## Version 2 (optional)

# Aces can be worth 11 if they won't put the total point value of both cards over 21. Remember that you can have multiple aces in a hand.

def main():

    cards = {
        "A": 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10
        }

    # print(cards)

    advice = {
        'bust': 'Already Busted!',
        'hit': 'Hit!',
        'stay': 'Stay!',
        'blackjack': 'Blackjack!'
        }

    # print(advice)

    hand = []

    hand.append(str(input("What's your first card: ")).upper())
    hand.append(str(input("What's your second card: ")).upper())
    hand.append(str(input("What's your third card: ")).upper())

    # print(hand)
    total = 0
    for i in hand:
        if i in cards:
            # print(cards.get(i))
            total += cards.get(i)
    # print(total)

    while True:
        if total > 21:
            print(f"{total} {advice['bust']}")
        elif 17<= total < 21:
            print(f"{total} {advice['stay']}")
        elif total < 17:
            print(f"{total} {advice['hit']}")
        else:
            print(f"{total} {advice['blackjack']}") 
        break
main()
