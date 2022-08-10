const phrase = prompt("Enter phrase to encrypt \n\t> ")
let rotateAmount = prompt("Enter amount to rotate \n\t> ")
rotateAmount = parseInt(rotateAmount)

const alphabet = 'abcdefghijklmnopqrstuvwxyz'
const validCharacters = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '0123456789', '!@#$%^&*()', ' ']
function rotatePhrase(phrase) {
    let rotatedPhrase = ''
    for (let letter of phrase) {
        for (let alphabet of validCharacters) {
        if (alphabet.includes(letter)) {
            const index = alphabet.indexOf(letter)
            const rotatedIndex = (index + rotateAmount) % alphabet.length
            const rotatedLetter = alphabet[rotatedIndex]
            rotatedPhrase += rotatedLetter
        } 
    }
}
    return rotatedPhrase
}
    
console.log(rotatePhrase(phrase))




