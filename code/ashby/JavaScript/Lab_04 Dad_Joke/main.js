const dadContainer = document.querySelector('#dad-container');
const randomDad = document.querySelector('#random-dad');
const searchDad = document.querySelector('#search-dad');
const dadInput = document.querySelector('#dad-input');


function createDad(joke){
    dadContainer.innerHTML = ''
    let h = document.createElement('h4');
    h.innerText = joke;
    dadContainer.appendChild(h);
}

function multiDad(jokes){
    dadContainer.innerHTML = ''
    for(let joke of jokes){
        let h = document.createElement('h4');
        h.innerText = joke.joke;
        dadContainer.appendChild(h);
        let br = document.createElement('br');
        dadContainer.appendChild(br);
    }
}

async function findDad(){
    const response = await fetch('https://icanhazdadjoke.com/', {
        headers: {
            accept: "application/json"
        }})
    const data = await response.json()
    createDad(data.joke)
    console.log(data);
}

findDad()


async function searchFunction(){
    let input = dadInput.value
    if(!input){
        alert('Daddy requires a valid input!')
    } else{
    const response = await fetch(`https://icanhazdadjoke.com/search?term=${input}&limit=5`, {
        headers: {
            accept: "application/json"
        }})
    const data = await response.json()
    console.log(data);
    multiDad(data.results)
}}



randomDad.onclick = () => findDad()

searchDad.onclick = () => searchFunction()