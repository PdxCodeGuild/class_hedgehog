// const message = document.querySelector("#message");
// console.log(message);
// message.innerText = "I changed the text";

const userInput = document.querySelector("#user-input");
// console.log(userInput);

const button = document.querySelector("#submit");

function logValue() {
    // console.log(userInput.value);
    console.log(event)
}

userInput.addEventListener("keydown", logValue)
// userInput.addEventListener("input", function() {
//     button.innerText = "Type something fun"
// })

userInput.addEventListener("mouseenter", function() {
    userInput.style.backgroundColor = "red";
});

userInput.addEventListener("mouseleave", function() {
    userInput.style.backgroundColor = "white";
});

button.addEventListener("click", logValue);
