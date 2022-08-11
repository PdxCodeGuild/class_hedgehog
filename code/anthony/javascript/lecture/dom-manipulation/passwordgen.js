
$ = (a) => document.querySelector(a)

const passwordLength = document.querySelector("#password-length")
const lowercase = $("#lowercase")
const uppercase = document.querySelector("#uppercase")
const digits = document.querySelector("#digits")
const specialCharacters = document.querySelector("#special-characters")
const generateBtn = document.querySelector("#generate-btn")



function getCharacters() {
  let characters = ""
  if(lowercase.checked) {
    characters += "abcdefghijklmnopqrstuvwxyz"
  }
  if(uppercase.checked){
    // It was quicker to copy/paste lowercase string and add toupper
    characters += "abcdefghijklmnopqrstuvwxyz".toUpperCase()
  }
  if(digits.checked){
    characters += "1234567890"
  }
  if(specialCharacters.checked){
    characters += "!@#$%^&*()_-=+,./?<>"
  }
  return characters
}

function generatePassword() {
  const characters = getCharacters()

  let password = ""
  for(let i = 0; i < parseInt(passwordLength.value); i++){
    let index = Math.floor(Math.random() * characters.length)
    password += characters[index]
  }

  document.querySelector("#password").innerText = password
}

generateBtn.addEventListener("click", generatePassword)