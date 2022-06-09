# # # Blackjack Advice


# # Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards. 
# First, ask the user for three playing cards (A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K). 
# Then, figure out the point value of each card individually. Number cards are worth their number, all face cards are worth 10. 
# At this point, assume aces are worth 1. Use the following rules to determine the advice:

# # * Less than 17, advise to "Hit"
# # * Greater than or equal to 17, but less than 21, advise to "Stay"
# # * Exactly 21, advise "Blackjack!"
# # * Over 21, advise "Already Busted"

# # Print out the current total point value and the advice.

# # ```
# # What's your first card? Q
# # What's your second card? 2
# # What's your third card? 3
# # 15 Hit

# # What's your first card? K
# # What's your second card? 5
# # What's your third card? 5
# # 20 Stay

# # What's your first card? Q
# # What's your second card? J
# # What's your third card? A
# # 21 Blackjack!


    
def main():
    cards_op = {"A": 1,
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
    
    card_1 = str(input("Enter your first card: ").upper())
    card_2 = str(input("Enter your second card: ").upper())
    card_3 = str(input("Enter your third card: ").upper())
   


    
    card_total = cards_op[card_1] + cards_op[card_2] + cards_op[card_3]
    
    #Thanks April for helping me figure out he Code body for this!
    if card_total >= 11:
        cards_op["A"] = 11
        card_total = cards_op[card_1] + cards_op[card_2] + cards_op[card_3]

    def advice():
        if card_total < 17: 
            return "Hit"
        elif 17 <= card_total < 21:
            return "STAY"
        elif card_total == 21:
            return "BLACKJACK!"
        else:
            return "Busted!"
    
    print(f"{card_total}, {advice()}!") 
main()


