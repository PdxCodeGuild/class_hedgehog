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
    const validChoices = ['rock', 'paper', 'scissors'];
    const beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"};
    let playerChoice = prompt("Choose Rock, Paper, or Scissors").toLowerCase();
    // console.log(playerChoice)
    if (validChoices.includes(playerChoice)) {
        // alert(`You chose ${playerChoice}!`);
    } else {
        alert("Not a valid choice!");
        return rockPaperScissors();
    };
    computerChoice = getRandomItem(validChoices);
    // console.log(computerChoice) 
    if (beats[playerChoice] == computerChoice) {
        return alert(`You chose ${playerChoice}. Computer chose ${computerChoice}. You win!`);
    } else if (beats[computerChoice] == playerChoice) {
        return alert(`You chose ${playerChoice}. Computer chose ${computerChoice}. Computer wins!`);
    } else if (playerChoice == computerChoice) {
        return alert(`You both chose ${playerChoice}. It's a tie!`);
    }
}

rockPaperScissors()
