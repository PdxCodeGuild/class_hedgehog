const playerCardsDiv = document.querySelector('#player-cards')
const hitBtn = document.querySelector('#hit-btn')
const advice = document.querySelector('#advice')
const playAgain = document.querySelector('#play-again')
const cardCount = document.querySelector('#card-count')
const playerHand = []
let deckId = ''
let score = 0

hitBtn.disabled = true
hitBtn.addEventListener('click', function(){
    drawCards(deckId, 1)
})

playAgain.addEventListener('click', function(){
    playerCardsDiv.innerHTML = ''
    advice.textContent = ''
    cardCount.textContent = ''
    playerHand.splice(0, playerHand.length)
    getDeck()
})

function calculateScore(){
    let score = 0
    for(let card of playerHand){
        if(Number(card.value)){
            score += Number(card.value)
        } else if (card.value === 'Ace'){
            score += 1
        } else {
            score += 10
        }
    }

    if(score > 21){
        advice.textContent = "Sorry.. you busted"
        hitBtn.disabled = true
    } else if (score === 21){
        advice.textContent = 'Blackjack'
        hitBtn.disabled = true
    } else if (score >= 17){
        advice.textContent = 'You should stay'
    } else{
        advice.textContent = 'Hit!!'
    }
}


function renderCards() {
    playerCardsDiv.innerHTML = ''
    for (let card of playerHand){
        const img = document.createElement('img')
        img.src = card.image
        img.style.width = `${Math.min(100/playerHand.length, 25)}vw` 
        playerCardsDiv.appendChild(img)
        
    }
    calculateScore()
}


async function drawCards(deckId, amount=2){
    const response = await fetch (`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=${amount}`)
    const data = await response.json()
    for(let card of data.cards){
        playerHand.push(card)
    }
    renderCards()
}

async function getDeck() {
    const response = await fetch('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
    const data = await response.json()
    drawCards(data.deck_id)
    deckId = data.deck_id
    hitBtn.disabled = false
}

getDeck()