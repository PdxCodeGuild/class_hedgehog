
let phrase_input = document.querySelector('#userString');
let rot_input = document.querySelector('#rotateAmount');
let run_bt = document.querySelector('#run');
let output = document.querySelector('#output');


run_bt.onclick = function(){
    const userString = phrase_input.value
    let rotateAmount = rot_input.value
    rotateAmount = parseInt(rotateAmount)
    const lowerUserString = userString.toLowerCase()
    const lowercase = ['abcdefghijklmnopqrstuvwxyz']
    
    
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
    output.innerText = rot
}
