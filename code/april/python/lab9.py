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
"""
Updates in Version 1:
Moved print statement into same line with advice

Removed variable reassignment, and just used card_total instead of 
using additional card_value variable

Updated error in code
"""
# # First, ask the user for three playing cards 
# # (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K)

# def main():
#     # point values of the cards stored in dictionary to access 
#     # later to help determine total
#     point_value = {
#     "A": 1,
#     "2": 2,
#     "3": 3, 
#     "4": 4, 
#     "5": 5, 
#     "6": 6, 
#     "7": 7, 
#     "8": 8, 
#     "9": 9, 
#     "10": 10, 
#     "J": 10, 
#     "Q": 10, 
#     "K": 10
#     }
#     # Then, figure out the point value of each card individually. 
#     card1 = str(input("Your card choices are 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K'\nPlease, enter your first card: ").upper())
#     card2 = str(input("Please, enter your second card: ").upper())
#     card3 = str(input("Please, enter your third card: ").upper())

#     card_total = point_value[card1] + point_value[card2] + point_value[card3]

#     if card_total < 17:
#         print(f"{card_total} Hit!")
#     elif card_total >= 17 and card_total < 21:
#         print(f"{card_total} Stay")
#     elif card_total == 21:
#         print(f"{card_total} Blackjack")
#     elif card_total >21:
#         print(f"{card_total} Already Busted")
#     else:
#         print("Error")  

# main()


"""
Version 2 (optional)

Aces can be worth 11 if they won't put the total point value of both 
cards over 21. Remember that you can have multiple aces in a hand. 
"""
"""
Changes from Version 1:

Added .strip() to remove errors that might occur from putting a space 
before or after entry

Added try/except to account for KeyErrors

Moved print statement into same line with advice

Removed variable reassignment, and just used card_total instead of 
using additional card_value variable

Updated error in code

Added option to try again or stop
"""

def main():
    while True:
        try:
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
            card1 = str(input("Your card choices are 'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K'\nPlease, enter your first card: ").upper().strip())
            card2 = str(input("Please, enter your second card: ").upper().strip())
            card3 = str(input("Please, enter your third card: ").upper().strip())
            # get total value of cards
            card_total = point_value[card1] + point_value[card2] + point_value[card3]
            # make aces worth 11 if they won't put total point value of cards over 21
            if card_total <= 11:
                # reassign value of "A" to 11 if the card total value is less than 10
                point_value["A"] = 11
                card_total = point_value[card1] + point_value[card2] + point_value[card3]
  
  
            if card_total < 17:
                print(f"{card_total} Hit!")
            elif 17 <= card_total < 21:
                print(f"{card_total} Stay")
            elif card_total == 21:
                print(f"{card_total} Blackjack")
            elif card_total >21:
                print(f"{card_total} Already Busted")
            else:
                print("Error")
   
            try_again = input("Would you like to try again?\nEnter 'y' or 'n': ").lower().strip()

            if try_again == "n":
                break

        except KeyError:
            print("Invalid Input")

main()