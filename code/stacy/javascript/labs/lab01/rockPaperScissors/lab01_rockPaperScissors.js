// import random
//     valid_choices = ['rock', 'paper', 'scissors']
//     player_choice = input("Please choose rock, paper, or scissors: \n\t> ").replace(' ','').lower()
//     if player_choice not in valid_choices:
//         print(f"{player_choice} is not a valid choice! Try again!")
//         return rock_paper_scissors()
//     computer_choice = random.choice(valid_choices)
//     if beats.get(player_choice) == computer_choice:
//         return f"{player_choice.title()} beats {computer_choice}, you win!"
//     elif beats.get(computer_choice) == player_choice:
//         return f"{computer_choice.title()} beats {player_choice}. You lose!"
//     elif player_choice == computer_choice:
//         return f"You both chose {player_choice}! You tie!"
// #########################################################################################################
// '''Version 2'''
// def main():
//     while True:
//         result = rock_paper_scissors()
//         print(result)
//         play_again = input("Would you like to play again? y for yes, anything else to quit: \n\t> ").lower().replace(' ','')
//         if play_again != 'y':
//             print("Thank you for playing! Goodbye!")
//             break
// main()



function getRandomItem(choices) {
    const index = Math.floor(Math.random() * choices.length);
    const item = choices[index];
    return item;
}


function rockPaperScissors() {

    const valid_choices = ['rock', 'paper', 'scissors']

    const beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

    let playerChoice = prompt("Choose Rock, Paper, or Scissors").toLowerCase()
    if ($.inArray(playerChoice, valid_choices)) {
        // no code, just a crude if not statement
    } else {
        alert("Not a valid choice!")
        return rockPaperScissors()
    }



}
// let inputUnit = prompt("Enter input unit \n\t> ")
// get player input

// generate computer choice

// compare and decide who wins with if/else



//     player_choice = input("Please choose rock, paper, or scissors: \n\t> ").replace(' ','').lower()
//     if player_choice not in valid_choices:
//         print(f"{player_choice} is not a valid choice! Try again!")
//         return rock_paper_scissors()
//     computer_choice = random.choice(valid_choices)
//     if beats.get(player_choice) == computer_choice:
//         return f"{player_choice.title()} beats {computer_choice}, you win!"
//     elif beats.get(computer_choice) == player_choice:
//         return f"{computer_choice.title()} beats {player_choice}. You lose!"
//     elif player_choice == computer_choice:
//         return f"You both chose {player_choice}! You tie!"