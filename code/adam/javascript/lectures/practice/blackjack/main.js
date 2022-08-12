let firstCard = 10

let secondCard = 11

let sum = firstCard + secondCard

let hasBlackJack = false
let isAlive = true
let message = ""

// let messageEl = document.querySelector("#message-el")
// let sumEl = document.querySelector("#sum-el")


startGameBtn.addEventListener('click', function startGame() {
    if (sum <= 20) {
        message = ("Do you want to draw a new card?")
        
    } else if (sum === 21) {
        message = ("Woohoo! You've got blackjack!")
        hasBlackJack = true
    
    }else {
        message = ("You are out of the game!")
        isAlive = false
    }
    console.log(message)
})




