const encounter = document.querySelector("#encounter")
const playersDiv = document.querySelector("#players-div")
const monstersDiv = document.querySelector("#monsters-div")
const addPlayerBtn = document.querySelector("#add-player-btn")
const addMonsterBtn = document.querySelector("#add-monster-btn")
const easy = document.querySelector("#easy")
const medium = document.querySelector("#medium")
const hard = document.querySelector("#hard")
const deadly = document.querySelector("#deadly")
const dailyBudget = document.querySelector("#daily-budget")
const expDiv = document.querySelector("#exp-div")
const deleteBtn = document.querySelector("#delete-btn")

document.querySelector("input[type='Number']").addEventListener("change", function() {
    calculateEXP()
});

deleteBtn.addEventListener("click", function() {
    this.parentElement.remove(this)
})

function calculateEXP() {
    let levels = document.querySelectorAll("input[type='Number']")
    let players = []
    for (player of levels){
        players.push(player.value)
    }
    console.log(players)
    easyEXP = 0
    mediumEXP = 0
    hardEXP= 0
    deadlyEXP = 0
    dayEXP = 0
    for (player of players) {
        easyEXP += exp_threshold_per_character_level[player]["Easy"]
        mediumEXP += exp_threshold_per_character_level[player]["Medium"]
        hardEXP += exp_threshold_per_character_level[player]["Hard"]
        deadlyEXP += exp_threshold_per_character_level[player]["Deadly"]
        dayEXP += adventuring_day_exp_per_character[player]
    }
    easy.innerHTML = `Easy: ${easyEXP}`
    medium.innerHTML = `Medium: ${mediumEXP}`
    hard.innerHTML = `Hard: ${hardEXP}`
    deadly.innerHTML = `Deadly: ${deadlyEXP}`
    dailyBudget.innerHTML = `Daily Budget: ${dayEXP}`
    }
    
addPlayerBtn.addEventListener("click", function(){
    let div = document.createElement("div")
    div.innerText = 'Lvl: '
    let lvl = document.createElement("INPUT")
    lvl.setAttribute("type", "Number")
    lvl.setAttribute("value", "1")
    lvl.setAttribute("min", "1")
    lvl.setAttribute("max", "20")
    lvl.onchange = () => {
        calculateEXP()
    }
    document.body.appendChild(lvl)
    let deleteBtn = document.createElement("button")
    deleteBtn.innerText = "Delete"
    deleteBtn.id = "delete-btn"
    div.append(lvl, deleteBtn)
    playersDiv.append(div)
    calculateEXP()
    deleteBtn.onclick = () => {
        div.parentElement.removeChild(div)
        calculateEXP()
    }
})

addMonsterBtn.addEventListener("click", function(){
    let p = document.createElement("p");
})

// monster should default to empty. field for monster name, field for cr. field for exp.
// total exp, adjusted exp
// button for save encounter

