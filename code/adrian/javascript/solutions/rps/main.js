// Option 1
// const btn1 = document.querySelector(".rock")
// const btn2 = document.querySelector(".paper")
// const btn3 = document.querySelector(".scissors")

// btn1.addEventListener("click", someFunction)
// btn2.addEventListener("click", someFunction)
// btn3.addEventListener("click", someFunction)

// Option 2
const buttons = document.querySelectorAll(".btn")

// button.className is the last button to iterate
// for(button of buttons){
//   button.addEventListener("click", function () {
//     console.log(button.className)
//   })
// }

buttons.forEach(function(button) {
  button.addEventListener("click", function() {
    rps(button.classList[1])
  })
})


function rps(player){
  // Get opponents choice
  // [-1] scissors loses to [0] rock loses to [1] paper loses to [2] scissors
  const choices = ["rock", "paper", "scissors"]
  const opponent = choices[Math.floor(Math.random() * 3)]

  const wins = [
    "rockscissors",
    "paperrock",
    "scissorspaper"
  ]

  let p = document.createElement("p")
  p.classList.add("result")
  // Calculate winner
  if(player === opponent){
    p.innerText = `You chose ${player}. Opponent chose ${opponent}. It was a tie.`
    p.classList.add("tie")
  } else if (wins.includes(player + opponent)){ // check to see if 'rock'+'scissors' is in winning array
    p.innerText = `You chose ${player}. Opponent chose ${opponent}. You win!`
    p.classList.add("win")
  } else {
    p.innerText = `You chose ${player}. Opponent chose ${opponent}. You lost.`
    p.classList.add("lose")
  }

  document.querySelector("#gamelog").prepend(p)
}