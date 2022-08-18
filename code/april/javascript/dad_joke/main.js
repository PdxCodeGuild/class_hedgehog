
const newJokeBtn = document.querySelector("#new-joke-btn")
let displayJoke = document.querySelector("#display-joke")
let searchJokes = document.querySelector("#search-jokes")
const searchBtn = document.querySelector("#search-btn")
const showJokes = document.querySelector('#show-jokes')



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


function searchForJokes(){
    let searchTerm =searchJokes.value

    fetch(`https://icanhazdadjoke.com/search?term=${searchTerm}`,{
        headers: {
            accept: "application/json"
        }
    }).then(response => response.json())
    .then(data => {
        for(let result of data.results){
            const p = document.createElement('li')
            p.innerHTML = result.joke
            showJokes.appendChild(p)
        }
    }).catch(err => console.error(err))
    showJokes.textContent = ''
}

searchBtn.addEventListener("click", searchForJokes)

// #TODO: Display error/nothing if search input is blank

// #TODO: Hide and unhide divs
// searchBtn.addEventListener("click", () => {
//     if(displayJoke.style.display === "none") {
//         displayJoke.style.display = "block"
//     } else {
//         displayJoke.style.display = "none"
//     }
// })

// newJokeBtn.addEventListener("click", () => {
//     if(displayJoke.style.display === "none") {
//         showJokes.style.display = "block"
//     } else {
//         showJokes.style.display = "none"
//     }
// })