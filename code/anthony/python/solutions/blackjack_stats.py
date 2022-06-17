import random


def deal(deck, num):
    hand = []
    for _ in range(num):
        hand.append(deck.pop())

    return hand


def new_deck():
    suit = ['A', 'J', 'Q', 'K'] + list(range(2, 11))
    deck = suit * 4
    random.shuffle(deck)
    return deck


def count_cards(hand):
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

    return total


def main():
    iterations = 1000000
    count = {
        "less than 17": 0,
        "17 to 21": 0,
        "21": 0,
        "over 21": 0
    }
    deck = new_deck()
    for _ in range(iterations):
        if len(deck) < 3:
            deck = new_deck()

        hand = deal(deck, 3)

        total = count_cards(hand)

        if total > 21:
            count["over 21"] += 1
        elif total < 17:
            count["less than 17"] += 1
        elif total == 21:
            count["21"] += 1
        else:
            count["17 to 21"] += 1

    for key, value in count.items():
        perc = (value/iterations) * 100
        print(f"{value:5} {perc:.2f}% {key}")


if __name__ == "__main__":
    main()
