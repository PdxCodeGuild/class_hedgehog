    
def blackjack_advice():    
    card_values = {"A": 1,"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    
    cards =[]
    card1 = str(input("What's your first card: ").upper())
    cards.append(card1)
    card2 = str(input("What's your second card: ").upper())
    cards.append(card2)
    card3 = str(input("What's your third card: ").upper())
    cards.append(card3)

    total = card_values[card1] + card_values[card2] + card_values[card3]

    for card in cards:
        if card == "A" and total <= 21:
            total += 10 
            
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