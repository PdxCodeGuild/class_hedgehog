// Old input system here
// const playerChoice = prompt("enter Rock, Paper, or Scissors: ").toLowerCase();

let player_choice = document.querySelector("#player_choice");

let runGame = document.querySelector("#run_game");

let game_result = document.querySelector("#game_result");

const computerArr = ['rock', 'paper', 'scissors']


runGame.onclick = function(){ let playerChoice = player_choice.value.toLowerCase();

let computerSeed = Math.floor(Math.random() * computerArr.length)

let computerChoice = computerArr[computerSeed]
    
let winner = ''

// Spaghettiiiii I am not enjoying Javascript so faaarrrrrr :[

alert(`Player played ${playerChoice} and computer played ${computerChoice}.`)

if( playerChoice == computerChoice){
    winner = 'Draw! Nobody'
} else if( playerChoice == 'rock') 
    if  (computerChoice == 'paper'){ winner = 'Computer';
        } else if(computerChoice == 'scissors'){ winner = 'Player'}

        if( playerChoice == 'paper') 
            if (computerChoice == 'scissors'){ winner = 'Computer';} 
            else if (computerChoice == 'rock'){ winner = 'Player'}

    if (playerChoice == 'scissors') 
        if (computerChoice == 'paper'){ winner = 'Player'} 
        else if (computerChoice == 'rock'){ winner = 'Computer';} 

    if (computerArr.includes(playerChoice) == false){
        alert('Invalid player input.')
        winner = 'Nobody'    
    }
    
        game_result.innerText = `${winner} wins!`

    }