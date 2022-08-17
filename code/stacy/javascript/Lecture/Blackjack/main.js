const playerCardsDiv = document.querySelector("#player-cards");
const hitBtn = document.querySelector("#hit-btn");
const resetBtn = document.querySelector("#reset-btn");
const advice = document.querySelector("#advice");
const cardCount = document.querySelector("#card-count");
const playerHand = [];
let deckID = '';
let score = 0;

hitBtn.diabled = true;

hitBtn.addEventListener("click", function () {
    drawCards(deckID, 1);
});

resetBtn.addEventListener("click", function () {
    playerCardsDiv.innerHTML = "";
    advice.textContent = "";
    cardCount.textContent = "";
    playerHand.splice(0, playerHand.length);
    getDeck();
});

function calculateScore() {
    score = 0;
    for (let card of playerHand) {
        if (Number(card.value)) {
            score += Number(card.value);
        } else if (card.value === "ACE") {
            score += 1;
        } else {
            score += 10;
        };
    };
    document.querySelector("#card-count").textContent = `Score: ${score}`;
    if (score > 21) {
        advice.textContent = "Bust!";
        hitBtn.disabled = true;
    } else if (score === 21) {
        advice.textContent = "Blackjack!"
        hitBtn.disabled = true;
    } else if (score >= 17) {
        advice.textContent = "Stand."
    } else {
        advice.textContent = "Hit!"
    };
};

function renderCards() {
    // console.log(playerHand);
    playerCardsDiv.innerHTML = ""
    for (let card of playerHand) {
        const img = document.createElement("img");
        img.src = card.image;
        img.style.width = `${Math.min(100 / playerHand.length, 25)}vw`;
        playerCardsDiv.appendChild(img);
        calculateScore();
    };
};

async function drawCards(deckID, amount=2) {
    const response = await fetch(`https://deckofcardsapi.com/api/deck/${deckID}/draw/?count=${amount}`);
    const data = await response.json();
    for (let card of data.cards) {
        playerHand.push(card)
    };
    renderCards();
};

async function getDeck() {
    const response = await fetch("https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1");
    const data = await response.json();
    console.log(data);
    drawCards(data.deck_id);
    deckID = data.deck_id;
    hitBtn.disabled = false;
};

getDeck();
