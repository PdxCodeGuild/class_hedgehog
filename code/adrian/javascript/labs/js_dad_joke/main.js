const jokesDiv = document.querySelector("#jokes")
const searchJoke = document.querySelector("#search-joke")
const submitBtn = document.querySelector("#submit-btn")


submitBtn.addEventListener("click", function() {
    console.log(searchJoke.value)
    fetch(`https://icanhazdadjoke.com/search?term=${searchJoke.value}`, {
        headers: {
          accept: "application/json"
        }
      }).then(response => response.json())
      .then(data => showDadJoke(data))
})


function showDadJoke(data) {
  console.log(data)
    if (data.results[0]){
        jokesDiv.textContent = data.results[0].joke

    } 
}