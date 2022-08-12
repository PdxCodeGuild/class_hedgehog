let message = document.querySelector("#message")
let rotAmount = document.querySelector("#rot-amount")
let encryptBtn = document.querySelector("#encrypt-btn")
// let encryption = document.querySelector("#encryption").innerText





function rot(){
    rotAmount = parseInt(rotAmount.value)
    const alphabet = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "1234567890", "!@#$%^&*()_+-=,./<>?", " "]
    let encrypt = ""
    for(let char of message.value){
        for(let abc of alphabet){
            if(abc.includes(char)){
                const index = abc.indexOf(char)
                const rotIndex = (index + rotAmount) % abc.length
                const rotChar = abc[rotIndex]
                encrypt += rotChar
            }
        }

        }
        document.querySelector("#encryption").innerText = encrypt
        
    }
    
    
encryptBtn.addEventListener("click", rot)