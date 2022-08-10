const phrase = prompt('Enter phrase to encrypt:')
let rotateAmount = prompt("Enter amount ot rotate:")
const lowerPhrase = phrase.toLowerCase()

rotateAmount = parseInt(rotateAmount)
const alphabets = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '01234567789', '!@#$%^&*()', ' ']

function rotatePhrase(phrase){
    let rotatedPhrase = ''
    for (letter of phrase){
        for(let alphabet of alphabets){
            if (alphabet.includes(letter)){
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