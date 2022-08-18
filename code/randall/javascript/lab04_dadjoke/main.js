// dad joke api using javascript

btn = document.querySelector("#btn");
btn.addEventListener("click", function() {
  fetch("https://icanhazdadjoke.com/", {
    headers: {
      accept: "application/json"
    }
  }).then(response => response.json())
  .then(data => {
    console.log(data);
    document.querySelector("#joke").innerHTML = data.joke;
  }).catch(error => console.log(error));
}   );





