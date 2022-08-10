const choice = prompt("Enter 'Rock', 'Paper', or 'Scissors' : ")

const weapons = [
    'Rock',
    'Paper',
    'Scissors'
]

const random_computer = Math.floor(Math.random() * weapons.length)


const computer = weapons[random_computer]

// console.log(computer)

const win = 'You Win!'
const lose = 'You Lose!'

if(choice == computer){
    alert("It's a Tie!"),
    console.log('Computer chose:', computer)
}
else if(choice == 'Rock')
    if(computer == 'Scissors'){
        alert(win),
        console.log('Computer chose:', computer)
    }
else if(choice == 'Paper')
    if(computer == 'Rock'){
        alert(win),
        console.log('Computer chose:', computer)
    }
else if(choice == 'Scissors')
    if(computer == 'Paper'){
        alert(win),
        console.log('Computer chose:', computer)
    }
else {
    alert(lose),
    console.log('Computer chose:', computer)
}
