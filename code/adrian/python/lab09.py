
# Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. 
# Number cards are worth their number, all face cards are worth 10. 
# At this point, assume aces are worth 1. Use the following rules to determine the advice:

# Less than 17, advise to "Hit"
# Greater than or equal to 17, but less than 21, advise to "Stay"
# Exactly 21, advise "Blackjack!"
# Over 21, advise "Already Busted"
# Print out the current total point value and the advice.


# A = 1
# J = Q = K = 10

cards = {"A": 1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

def black_jack():
    card1 = str(input("What's your first card? ")) # int(input("What's your first card? ")) gives value error had to use dictionary and convert to str.
    card2 = str(input("What's your first card? "))
    card3 = str(input("What's your first card? "))
    all_cards = cards[card1] + cards[card2] + cards[card3]

    if all_cards > 10:
        cards["A"] = 11

    if all_cards < 17:
        print ("Hit")
    elif all_cards >= 17 and all_cards < 21:
        print("Stay")
    elif all_cards == 21:
        print("Blackjack!")
    else:
        print("Busted")

black_jack()
