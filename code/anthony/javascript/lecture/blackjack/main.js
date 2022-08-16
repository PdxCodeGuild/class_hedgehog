const playerCardsDiv = document.querySelector("#player-cards")
const hitBtn = document.querySelector("#hit-btn")
const advice = document.querySelector("#advice")
const playAgain = document.querySelector("#play-again")
const cardCount = document.querySelector("#card-count")
const playersHand = []
let deckId = ""
let score = 0

hitBtn.disabled = true

playAgain.addEventListener("click", function() {
  playerCardsDiv.innerHTML = ""
  advice.textContent = ""
  cardCount.textContent = ""
  playersHand.splice(0, playersHand.length)
  getDeck()
})

hitBtn.addEventListener("click", function() {
  drawCards(deckId, 1)
})

function calculateScore(){
  score = 0
  for(let card of playersHand){
    if(Number(card.value)){
      score += Number(card.value)
    } else if(card.value === "ACE"){
      score += 1
    } else{
      score += 10
    }
  }
  cardCount.textContent = `Total: ${score}`

  if(score > 21){
    advice.textContent = "Sorry... you busted..."
    hitBtn.disabled = true
  } else if(score === 21){
    advice.textContent = "BlackJack!!!"
    hitBtn.disabled = true
  } else if(score >= 17){
    advice.textContent = "Hint... you should stay."
  } else{
    advice.textContent = "Hint... you should hit."
  }
}

function renderCards() {
  playerCardsDiv.innerHTML = ""
  for(let card of playersHand){
    const img = document.createElement("img")
    img.src = card.image
    img.style.width = `${Math.min(100/playersHand.length, 25)}vw`
    playerCardsDiv.appendChild(img)
  }
  calculateScore()
}

async function drawCards(deckId, amount=2){
  const response = await fetch(`https://deckofcardsapi.com/api/deck/${deckId}/draw/?count=${amount}`)
  const data = await response.json()

  for(let card of data.cards){
    playersHand.push(card)
  }

  renderCards()
}

async function getDeck() {
  const response = await fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1")
  const data = await response.json()
  drawCards(data.deck_id)
  deckId = data.deck_id
  hitBtn.disabled = false
}

getDeck()