const jokeBtn = document.getElementById("joke-btn")
const jokeEl = document.getElementById("joke-el")
const ulEl = document.getElementById("ul-el")


let myJokes = []

jokeBtn.addEventListener("click", function(){

    fetch("https://icanhazdadjoke.com/", {
        headers: {
            accept: "application/json"
        }
   
    }).then(response => response.json())
    .then(data =>  myJokes.push(data.joke))
    renderJokes()



})

function renderJokes(){
    let listItems = ""
    for(let i = 0; i < myJokes.length; i++){
        listItems +=`
        <li>
            ${myJokes[i]}
        </li>
        `
    }
    ulEl.innerHTML = listItems
}