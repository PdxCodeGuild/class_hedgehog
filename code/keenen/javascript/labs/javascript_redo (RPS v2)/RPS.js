
const playerChoice = document.querySelector('#player')
// console.log(rock)

const weaponChoice = [
    'rock',
    'paper',
    'scissors'
]

// console.log(rock)


function computerRandom() {

    const random = Math.floor(Math.random() * weaponChoice.length)
    const computerChoice = weaponChoice[random]
    // console.log(computerChoice)
    return computerChoice
}

function main() {
    let user = String(playerChoice.value)
    let computer = computerRandom(weaponChoice)
    let userMessage = ""
    let computerMessage = ""; computer
    
    if(computer == user) {
        userMessage += "It's a Tie!"
        computerMessage += "Computer chose: " 
    }

    else if(user == 'Rock') {
        if(computer == 'Scissors'){
        userMessage += "You won!"
        computerMessage += "Computer chose: " 
        }
    }

    else if(user == 'Paper') {
        if(computer == 'Rock'){
        userMessage += "You won!"
        computerMessage += "Computer chose: " 
        }
    }

    else if(user == 'Scissors'){
        if(computer == 'Paper'){
        userMessage += "You won!"
        computerMessage += "Computer chose: "
        }
    }
        
    else {
        userMessage += "Bummer, you lost"
        computerMessage += "Computer chose: "
    }
alert(userMessage)
console.log(computerMessage)
}
   
play.addEventListener('click', main)
