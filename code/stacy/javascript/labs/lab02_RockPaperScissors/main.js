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


const validChoices = ['rock', 'paper', 'scissors'];
const beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"};
const playerChoice = document.querySelector("#player-choice")
const shootBtn = document.querySelector("#shoot")

function getRandomItem(choices) {
    const index = Math.floor(Math.random() * choices.length);
    const item = choices[index];
    return item;
}

function rockPaperScissors() {
    let winner = '';
    let player = playerChoice.value;
    let computer = getRandomItem(validChoices);        
    if (beats[player] == computer) {
        winner = "Winner: player!"
    } else if (beats[computer] == player) {
        winner = "Winner: computer!"
    } else if (player == computer) {
        winner = "Winner: tie!"
    };
    document.querySelector("#winner").innerText = winner;
    document.querySelector("#player-hand").innerText = "Player choice: " + player;
    document.querySelector("#computer-hand").innerText = "Computer choice: " + computer;
    return winner;
}

shootBtn.addEventListener("click", rockPaperScissors);