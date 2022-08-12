let input_message = document.querySelector('#input_message');

let input_rotation = document.querySelector('#input_rotation');

let encrypt_button = document.querySelector('#encrypt_button'); 

let encrypted_message = document.querySelector('#encrypted_message');   


encrypt_button.onclick = function(){ 
let    rotatedPhrase = '';
const alphabets = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz', '1234567890', '!@#$%^&*()+=+,-./'];
let    inputMessage = input_message.value;
let    inputRotation = Number(input_rotation.value);
    for(let letter of inputMessage){
        for(let alphabet of alphabets){
            if (alphabet.includes(letter)){
                const index = alphabet.indexOf(letter);
                const rotatedIndex = ((index + inputRotation) % alphabet.length)
                const rotatedLetter = alphabet[rotatedIndex];
                console.log(rotatedLetter)
                rotatedPhrase += rotatedLetter
                
            } else if(letter == ' '){ rotatedPhrase += ' '}
        }
        
    }
    console.log(rotatedPhrase)
    encrypted_message.innerText = rotatedPhrase;

}