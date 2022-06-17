import random

# function to deal cards


def deal(num, deck):
    hand = []
    for _ in range(num):
        hand.append(deck.pop())

    return hand


def new_deck():
    suit = ['A', 'J', 'Q', 'K'] + list(range(2, 11))
    deck = suit * 4
    random.shuffle(deck)
    return deck


# Collect cards
deck = new_deck()
hand = deal(3, deck)


# Get total card values
total = 0
for card in hand:
    if card == "A":
        total += 1
    elif card in ["J", "Q", "K"]:
        total += 10
    else:
        total += card

if "A" in hand and total <= 11:
    total += 10

print(hand, total)

# Give advice
if total > 21:
    print("Bust")
elif total < 17:
    print("You should hit")
elif total == 21:
    print("Blackjack!!!")
else:
    print("Stay")
