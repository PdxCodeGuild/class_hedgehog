const jokeDiv = document.querySelector("#joke")
const query = document.querySelector("#query")
const searchBtn = document.querySelector("#search-btn")

searchBtn.addEventListener("click", function() {
        
    fetch(`https://icanhazdadjoke.com/search?term=${query.value}`, {
        headers: {
        accept: "application/json"
        }
    }).then(response => response.json())
    .then(data => postJoke(data))
})


function postJoke(data) {
    if (data.results[0]) {
        jokeDiv.textContent = data.results[0].joke
    } else {
        jokeDiv.textContent = "Joke not found"
    }
}