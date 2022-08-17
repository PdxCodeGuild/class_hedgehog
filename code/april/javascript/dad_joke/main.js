
const newJokeBtn = document.querySelector("#new-joke-btn")
const displayJoke = document.querySelector("#display-joke")


async function newJoke() {
    fetch("https://icanhazdadjoke.com", {
        headers: {
            accept: "application/json"
        }
    }).then(response => response.json())
    .then(data => {
        displayJoke.innerHTML = data.joke
    }).catch(err => console.error(err))
}

newJokeBtn.addEventListener("click", newJoke)
