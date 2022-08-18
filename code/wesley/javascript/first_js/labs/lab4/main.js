
const newJoke = document.querySelector('#new-joke')
const searchTerm = document.querySelector('#search')
const hitBtn = document.querySelector('#search-term')
const jokeContainer = document.querySelector('#results')
const joke = document.querySelector('#joke')

newJoke.addEventListener('click', function(){
    fetch("https://icanhazdadjoke.com/", {
    headers: {
      accept: "application/json"
    }
  }).then(response => response.json())
  .then(data => showJoke(data))
  .catch(err => console.error(err))

  jokeContainer.textContent = ''
})

fetch("https://icanhazdadjoke.com/", {
    headers: {
      accept: "application/json"
    }
  }).then(response => response.json())
  .then(data => showJoke(data))
  .catch(err => console.error(err))

function showJoke(data) {
   let joke = data.joke
   document.querySelector('#joke').innerText = joke
}

hitBtn.addEventListener('click', function(){
    let term = searchTerm.value
    search(term)
    jokeContainer.textContent = ''
    joke.textContent =''
})

function search(term){
    fetch(`https://icanhazdadjoke.com/search?term=${term}`, {
        headers: {
          accept: "application/json"
        }
      }).then(response => response.json())
      .then(data => showResults(data))
      .catch(err => console.error(err))

}    

function showResults(data){
    for(let joke of data.results){
        const p = document.createElement('p')
        p.textContent = joke.joke
        jokeContainer.appendChild(p)
    }
}


