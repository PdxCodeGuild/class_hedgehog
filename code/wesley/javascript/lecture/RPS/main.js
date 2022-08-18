// Option 1

// const btn1 = document.querySelector('.rock')
// const btn2 = document.querySelector('.paper')
// const btn3 = document.querySelector('.scissors')

// btn1.addEventListener('click', someFunction)
// btn2.addEventListener('click', someFunction)
// btn3.addEventListener('click', someFunction)

//  Option 2
const buttons = document.querySelectorAll('.btn')

// THIS DOES NOT WORK.
// button.className is the last button to iterate
// for(button of buttons){
//     button.addEventListener('click', function (){
//         console.log(button.className)
//     })
// }

// .className = full class
// classList = list of class


buttons.forEach(function(button) {
    button.addEventListener('click', function() {
        rps(button.classList[1])
    })
})

function rps (player){
    // Get opponents choic
    const choices = ['rock', 'paper', 'scissors']
    const opponent = choices[Math.floor(Math.random() * 3)]

    const wins = [
        'rockscissors',
        'paperrock',
        'scissorspaper'
    ]

    let p = document.createElement('p')
    p.classList.add('result')
    // Calculate winner
    if (player === opponent){
        p.innerText = `You chose ${player}. Opponent chose ${opponent}. It was a tie!.`
        p.classList.add('tie')
    } else if (wins.includes(player + opponent)){
        p.innerText = `You chose ${player}. Opponent chose ${opponent}. You win!.`
        p.classList.add('win')
    } else {
        p.innerText = `You chose ${player}. Opponent chose ${opponent}. You lose...`
        p.classList.add('lose')
    }
    
    document.querySelector('#gamelog').prepend(p)
}