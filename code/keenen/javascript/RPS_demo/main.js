

const btn1 = document.querySelector(".rock")
const btn2 = document.querySelector(".paper")
const btn3 = document.querySelector(".scissors")
console.log(btn1, btn2, btn3)

btn1.addEventListener("click", someFunction)
btn2.addEventListener("click", someFunction)
btn3.addEventListener("click", someFunction)

const buttons = document.querySelectorAll(".btn")
// console.log(buttons)


buttons.forEach(function(button) {
    button.addEventListener("click", function() {
        // console.log(button.className)
        rps(button.classList[1])
    })
})

function rps(player){
    const choices = ["rock", "paper", "scissors"]
    const opponent = choices[Math.floor(Math.random() * 3)]

    const wins = [
        "rockscissors",
        "paperrock",
        "scissorspaper",
    ]

    let p = document.createElement("p")
    p.classList.add("result")

    if(player === opponent){
        p.innerText = `You chose: ${player}. opponent chose: ${opponent}. It was a tie.`
        p.classList.add("tie")
        // console.log("It was a tie")
    } else if (wins.includes(player +opponent)){
        p.innerText = `You chose: ${player}. Opponent chose: ${opponent}. You win!`
        p.classList.add("win")

        // console.log("You win!")
    } else {
        p.innerText = `You chose: ${player}. Opponent chose: ${opponent}. You lose...`
        p.classList.add("lose")
        // console.log("You lose...")
    }
    document.querySelector("#gamelog").prepend(P)
}





    // console.log(player, opponent)

//     if(player === opponent){
//         console.log("It was a tie")
//     } else if(player!== "rock" && choices.indexOf(player) > choices.indexOf(opponent)){ console.log("You win!")
//     } else if(player === "rock") {
//         if(opponent === "scissors"){

//         } else {

//         }
//     }

// }

