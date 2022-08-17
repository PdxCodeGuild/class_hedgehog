
// run_op.onclick = function choice(array){
//     const index = Math.floor(Math.random() * array.length)
//     return array[index]
// }
const phrase = prompt("Enter phrase to encrypt: ")
let rotateAmount = prompt("Enter amount to rotate: ")

rotateAmount = parseInt(rotateAmount)

// const lowerPhrase = phrase.toLowerCase()

const alphabets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890", " "]


function rotatePhrase(phrase){
    let rotatedPhrase = ""

    for(let letter of phrase){
      for(let alphabet of alphabets){

        if(alphabet.includes(letter)){
            
            const index = alphabet.indexOf(letter);
              
            const rotatedIndex = (index + rotateAmount) % alphabet.length;
            const rotatedLetter = alphabet[rotatedIndex];
           
            rotatedPhrase += rotatedLetter
        }
      }

    }
    return rotatedPhrase
}


console.log(rotatePhrase(phrase))