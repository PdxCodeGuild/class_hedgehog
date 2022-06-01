import random
def rock_paper_scissors():
    beats = {
        'rock': 'scissors',
        'paper': 'rock',
        'scissors': 'paper'
    }
    valid_choices = ['rock', 'paper', 'scissors']
    player_choice = input("Please choose rock, paper, or scissors: \n\t> ").replace(' ','').lower()
    if player_choice not in valid_choices:
        print(f"{player_choice} is not a valid choice! Try again!")
        return rock_paper_scissors()
    computer_choice = random.choice(valid_choices)
    if beats.get(player_choice) == computer_choice:
        return f"{player_choice.title()} beats {computer_choice}, you win!"
    elif beats.get(computer_choice) == player_choice:
        return f"{computer_choice.title()} beats {player_choice}. You lose!"
    elif player_choice == computer_choice:
        return f"You both chose {player_choice}! You tie!"
#########################################################################################################
'''Version 2'''
def main():
    while True:
        result = rock_paper_scissors()
        print(result)
        play_again = input("Would you like to play again? y for yes, anything else to quit: \n\t> ").lower().replace(' ','')
        if play_again != 'y':
            print("Thank you for playing! Goodbye!")
            break
main()


'''
Rock Paper Scissors
Let's play rock-paper-scissors with the computer. You may want to try using these emojis 🗿📃✂️✊✋✌

The computer will ask the user for their choice (rock, paper, scissors)
The computer will randomly choose rock, paper or scissors
Determine who won and tell the user
Let's list all the cases:

rock vs rock (tie)
rock vs paper
rock vs scissors
paper vs rock
paper vs paper (tie)
paper vs scissors
scissors vs rock
scissors vs paper
scissors vs scissors (tie)
Version 2 (optional)
After playing, ask them if they'd like to play again. If they say yes, restart the game, otherwise exit.

'''