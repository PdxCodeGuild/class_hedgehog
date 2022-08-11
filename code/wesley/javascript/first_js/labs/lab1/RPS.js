
let userInput = document.querySelector('RPS')
let run_bt = document.querySelector('run2')
let output = document.querySelector('output')


run_bt.onclick = function () {

    const choicesArray = ['rock', 'paper', 'scissors'];
    const userChoice = userInput.options[userInput.selectedIndex].value;
    const compChoice = choicesArray[(Math.floor(Math.random()* choicesArray.length))]
    
    if (userChoice == compChoice) {
        alert("It's a tie!")
    }
    else if (userChoice == 'rock' && compChoice == 'paper'){
        alert('computer wins with paper')
    }
    else if (userChoice == 'rock' && compChoice == 'scissors'){
        alert('You win with Rock, comp chose Scissors')
    }
    else if (userChoice == 'paper' && compChoice == 'rock'){
        alert('you win with Paper, comp chose Rock')
    }
    else if (userChoice == 'scissors' && compChoice == 'paper'){
        alert('you win with Scissors, comp chose Paper')
    }
    else if (userChoice == 'paper' && compChoice == 'scissors'){
        alert('you lose, comp wins with scissors')
    }
    else if (userChoice == 'scissors' && compChoice == 'rock'){
        alert('you lose, comp wins with Rock')
    }
}