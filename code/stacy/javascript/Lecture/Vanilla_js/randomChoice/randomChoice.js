function choice(array) {
    randomIndex = Math.floor(Math.random()*array.length)
    return array[randomIndex]
}

const labs = [
    "random password generator",
    "rock paper scissors",
    "unit converter",
    "credit card validation",
    "rot13"
]

console.log(choice(labs))