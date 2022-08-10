const phrase = prompt("Enter phrase to encrypt:")
let rotateAmount = prompt("Enter amount to rotate:")

rotateAmount = parseInt(rotateAmount)

// convert phrase to lowercase
// const lowerPhrase = phrase.toLowerCase()

// create alphabet -> ["a", "b", ...]
const alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "!@#$%^&*()", " "]

function rotatePhrase(phrase){
  let rotatedPhrase = ""
  // iterate over phrase
  for(let letter of phrase){
    for(let alphabet of alphabets){
      // check if letter from phrase is in alphabet
      if(alphabet.includes(letter)){
        // get index of character from alphabet
        const index = alphabet.indexOf(letter)
  
        // find character that is 13 indices away
        // use modulus to not go out of range
        const rotatedIndex = (index + rotateAmount) % alphabet.length
        const rotatedLetter = alphabet[rotatedIndex]
  
        // add new character to rotated phrase
        rotatedPhrase += rotatedLetter
      }
    }
    
  }
  
  return rotatedPhrase
}


console.log(rotatePhrase(phrase))