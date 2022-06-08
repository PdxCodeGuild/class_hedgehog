"""
Lab 9

Blackjack Advice

Let's write a python program to give basic blackjack playing advice 
during a game by asking the player for cards. First, ask the user 
for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
Then, figure out the point value of each card individually. Number 
cards are worth their number, all face cards are worth 10. At this 
point, assume aces are worth 1. Use the following rules to determine 
the advice:

Less than 17, advise to "Hit"
Greater than or equal to 17, but less than 21, advise to "Stay"
Exactly 21, advise "Blackjack!"
Over 21, advise "Already Busted"

Print out the current total point value and the advice.
"""

# First, ask the user for three playing cards 
# (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)

def main():
    # point values of the cards stored in dictionary to access 
    # later to help determine total
    point_value = {
    "A": 1,
    "2": 2,
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "10": 10, 
    "J": 10, 
    "Q": 10, 
    "K": 10
    }
    # Then, figure out the point value of each card individually. 
    card1 = str(input("Your card choices are 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K'\nPlease, enter your first card: ").upper())
    card2 = str(input("Please, enter your second card: ").upper())
    card3 = str(input("Please, enter your third card: ").upper())

    card_total = point_value[card1] + point_value[card2] + point_value[card3]
    print(card_total)

    card_value = card_total

    if card_value < 17:
        print("Hit!")
    elif card_value >= 17:
        print("Stay")
    elif card_value == 21:
        print("Blackjack")
    elif card_value >21:
        print("Already Busted")        


main()


"""
Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both 
cards over 21. Remember that you can have multiple aces in a hand. 
"""