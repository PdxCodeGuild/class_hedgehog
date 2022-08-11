const userInput = document.querySelector("#user-input")
const button = document.querySelector("#submit")


function logValue(event){
  // console.log(userInput.value)
  console.log(event)
}

userInput.addEventListener("keydown", logValue)

userInput.addEventListener("mouseenter", function() {
  userInput.style.backgroundColor = "red"
})

userInput.addEventListener("mouseleave", function() {
  userInput.style.backgroundColor = "white"
})



// userInput.addEventListener("click", function() {
//   button.innerText = "Type something fun"
// })

// button.addEventListener("click", logValue)