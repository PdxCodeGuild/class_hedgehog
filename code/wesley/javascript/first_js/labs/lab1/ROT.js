

const userString = prompt('Enter the string: ')
let rotateAmount = prompt('Enter amount to rotate:')
rotateAmount = parseInt(rotateAmount)
const lowerUserString = userString.toLowerCase()
const lowercase = ['abcdefghijklmnopqrstuvwxyz']

function rotatePhrase(userString){
    let rot = ''
    for (char of userString){
        for (let char2 of lowercase){
           if (char2.includes(char)){
               const location = char2.indexOf(char)
               const rotatedIn = (location + rotateAmount) % char2.length
               const rotatedLet = char2[rotatedIn]
               rot += rotatedLet
            }
        }
    }
    return rot
    
}
console.log(rotatePhrase(userString))