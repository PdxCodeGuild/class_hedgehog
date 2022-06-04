"""
Lab 8 
Pick 6: Versions 1 and  2
April 
1 Jun 2022

Ticket contains 6 numbers (1 to 99) and number of matches between 
ticket and winning numbers determines payoff. Position matters.
Calculate net winnings (the sum of all expenses and earnings).

Steps:
Generate a list of 6 random numbers representing the winning ticket
Start your balance at 0
Loop 100,000 times, for each loop:
Generate a list of 6 random numbers representing the ticket
Subtract 2 from your balance (you bought a ticket)
Find how many numbers match
Add to your balance the winnings from your matches
After the loop, print the final balance (Hint: This will be negative)

Version 2:
The ROI (return on investment) is defined as (earnings - expenses)/expenses. 
Calculate ROI, print it out along with earnings and expenses.
"""

import random

def pick6(): # Define pick6 to generate ticket numbers for both winning numbers and tickets
    ticket_generator = []
    for numbers in range(0, 6):
        ticket_generator.append(random.randint(1, 99))
    return ticket_generator    

def num_matches(winning, ticket): # Define num_matches which returns number of matches between winning and ticket
    number_of_matches = 0 # Start number of matches at 0
    for numbers in range(0,6):
        if winning[numbers] == ticket[numbers]: # For each match add to number of matches
            number_of_matches += 1      
    return number_of_matches # Return the total number of matches    

def main():
    winning = pick6() # Set winning ticket value
    balance = 0 
    earnings = 0
    expenses = 0

    # Dictionary with payoff values for the corresponding match amounts (number of matches:dollar amount won)
    payoff = { 
        0: 0,
        1: 4,
        2: 7,
        3: 100,
        4: 50000,
        5: 1000000,
        6: 25000000
    }

    for check_for_matches in range(100000):
        expenses += 2 # Calculate total cost of tickets 100000 times $2 ticket cost
        balance -= 2 # Subtract 2 from your balance (you bought a ticket)
        
        check_for_matches = num_matches(winning, pick6()) # Check how many numbers match from all tickets from loop and winning ticket
    
        earnings += payoff[check_for_matches] # Total earnings with payoff
        balance += payoff[check_for_matches] # Add earnings to balance    

    roi = (earnings - expenses)/expenses # Calculate ROI

    print(f"Your final balance is: {balance}") # Net winnings
    print(f"Your earnings are: {earnings}")
    print(f"Your expenses are: {expenses}")
    print(f"Your ROI is: {roi} ") 
main()        


