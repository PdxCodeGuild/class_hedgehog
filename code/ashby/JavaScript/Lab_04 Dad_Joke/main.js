const dadContainer = document.querySelector('#dad-container');
const moreDad = document.querySelector('#more-dad');


function createDad(joke){
    dadContainer.innerHTML = ''
    let h = document.createElement('h4');
    h.innerText = joke;
    dadContainer.appendChild(h);
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


moreDad.onclick = () => findDad()