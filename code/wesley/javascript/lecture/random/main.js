
function choice(array){
    const index = Math.floor(Math.random() * array.length)
    return array[index]
}

const labs = [
    'RPS',
    'RPG',
    'UC',
    'CCV',
    'rot'
]

console.log(choice(labs))