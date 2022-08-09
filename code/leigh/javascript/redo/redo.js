

let choice = document.querySelector('#choice');
let run_bt = document.querySelector('#choose');
let output = document.querySelector('#output');

run_bt.onclick = function() {
    let human = choice.value;
    const choicesArray = ["rock", "paper", "scissors"];
    const computer = choicesArray[Math.floor((Math.random() * choicesArray.length))];
    let message = "";
    if (human == computer) {
        message = "tie";
    } else if (human == "rock" && computer == "paper") {
        message = "Computer wins with paper";
    } else if (human == "rock" && computer == "scissors") {
        message = "You win with rock";
    } else if (human == "paper" && computer == "rock") {
        message = "You win with paper";
    } else if (human == "paper" && computer == "scissors") {
        message = "Computer wins with paper";
    } else if (human == "scissors" && computer == "rock") {
        message = "Computer wins with rock";
    } else if (human == "scissors" && computer == "paper") {
        message = "You win with scissors";
    }

    output.innerText = message;
}