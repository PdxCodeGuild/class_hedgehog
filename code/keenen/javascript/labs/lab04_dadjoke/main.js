
const search = document.querySelector('#search')
const btnJoke = document.querySelector('#btn-joke')
const displayJokeDiv = document.querySelector('#display-joke')

btnJoke.addEventListener("click", function(){
    fetch(`https://icanhazdadjoke.com/search?term=${search.value}`, {
  headers: {
    accept: "application/json"
  }
}).then(response => response.json())
.then(data => generateJoke(data))
}
)



function generateJoke(data) {
   console.log(data)
    if(data.results){
        displayJokeDiv.textContent = `${data.results[0].joke}`
    }
    else {
        displayJokeDiv.textContent = 'Joke 404'
    }

    // for(let jokes of data.joke){
    // const joke = document.createElement('joke')
    // displayJokeDiv.appendChild(jokes)    

    // console.log(joke)

    }

