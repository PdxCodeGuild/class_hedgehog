// $ = (a) => document.querySelector(a);

// const passwordLength = $("#password-length");
// const lowercase = $("#lowercase");
// const uppercase = $("#uppercase");
// const digits = $("#digits");
// const special = $("#special");
// const generateBtn = $("#generate-btn");

const passwordLength = document.querySelector("#password-length");
const lowercase = document.querySelector("#lowercase");
const uppercase = document.querySelector("#uppercase");
const digits = document.querySelector("#digits");
const special = document.querySelector("#special");
const generateBtn = document.querySelector("#generate-btn");

// console.log(lowercase);

function getCharacters() {
    let characters = '';
    if (lowercase.checked) {
        characters += "abcdefghijklmnopqrstuvwxyz";
    };
    if (uppercase.checked) {
        characters +=   "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    };
    if (digits.checked) {
        characters += "0123456789";
    };
    if (special.checked) {
        characters += "!@#$%^&*()_+-=?<>";
    };
    return characters;
};

function generatePassword() {
    // console.log(passwordLength.value);
    // console.log(lowercase.checked);
    // console.log(uppercase.checked);
    const characters = getCharacters()
    let password = ""
    for (let i = 0; i < parseInt(passwordLength.value); i++) {
        let index = Math.floor(Math.random() * characters.length);
        password += characters[index];
    };
    // console.log(password);
    document.querySelector("#password").innerText = password
};

generateBtn.addEventListener("click", generatePassword);