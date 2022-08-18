const outputDiv = document.querySelector("#output-div");
const jokeBtn = document.querySelector("#joke-btn");
const searchBtn = document.querySelector("#search-btn");
const userInput = document.querySelector("#user-input");
const submitSearchBtn = document.querySelector("#submit-search-btn");
let resultsIndex = 0

jokeBtn.addEventListener("click", function () {
    getJoke();
    jokeBtn.textContent = "Another?";
});

searchBtn.addEventListener("click", function() {
    userInput.hidden = false;
    submitSearchBtn.hidden = false;
});

submitSearchBtn.addEventListener("click", function() {
    const searchTerm = userInput.value
    console.log(searchTerm)
    searchJoke(searchTerm);
    userInput.hidden = true;
    submitSearchBtn.hidden = true;
});

function getJoke() {
    const response = fetch("https://icanhazdadjoke.com/", {
        headers: {
            accept: "application/json"
        }
    }).then(response => response.json()).then(data => outputDiv.textContent = data.joke)
};

function searchJoke(searchTerm) {
    const response = fetch(`https://icanhazdadjoke.com/search?term=${searchTerm}`, {
        headers: {
            accept: "application/json"
        }
    }).then(response => response.json()).then(data => outputDiv.textContent = data.results[resultsIndex].joke).then(function(data){
        console.log(data);
        resultsIndex += 1;
    });
};
