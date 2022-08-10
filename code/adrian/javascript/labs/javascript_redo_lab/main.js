const choices = ["rock", "paper", "scissors"]

const userChoice = prompt("Rock, paper or scissors: ")
const compChoice = choices[Math.floor((Math.random()* choices.length))]



if(userChoice == "rock" && compChoice == "paper"){
    alert("You lose! Paper covers rock")
}
else if(userChoice == "rock" && compChoice == "scissors"){
    alert("You win! Rock smashes scissors")
}
else if(userChoice == "paper" && compChoice == "rock"){
    alert("You win! Paper covers rock")
}
else if(userChoice == "paper" && compChoice == "scissors"){
    alert("You lose! Scissors cut paper")
}
else if(userChoice == "scissors" && compChoice == "rock"){
    alert("You lose! Rock smashes scissors")
}
else if(userChoice == "scissors" && compChoice == "Paper"){
    alert("You win! Scissors cuts paper")
}
else if(userChoice == compChoice){
    alert("It's a tie!")
}