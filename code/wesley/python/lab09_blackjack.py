    
def blackjack_advice():    
    card_values = {"A": 1,"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    
    card1 = str(input("What's your first card: ").upper())
    card2 = str(input("What's your second card: ").upper())
    card3 = str(input("What's your third card: ").upper())

    total = card_values[card1] + card_values[card2] + card_values[card3]

    def advice():
        if total < 17:
            return "Hit"
        elif 17 < total < 21:
            return "Stay"
        elif total == 21:
            return "BlackJack"
        else:
            return "Already Busted"

    print(f"{total} ",  (advice())) 

blackjack_advice()