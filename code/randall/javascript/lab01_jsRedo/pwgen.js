let numberLength=prompt('How many numbers would you like in your password?')
let specialLength=prompt('How many special characters would you like in your password?')
let upperLength=prompt('How many uppercase letters would you like in your password?')
let lowerLength=prompt('How many lowercase letters would you like in your password?')
let finalPassword = generatePassword(numberLength, specialLength, upperLength, lowerLength)
finalPassword = shuffleWord(finalPassword)

function randint(a, b) {
    return Math.floor(a + Math.random()*(b-a+1))
}

function randomChoice(arr) {
    let i = randint(0, arr.length-1);
    return arr[i]
}

function getChars(desiredLength, array){
    let passIndex=0;
    let charString = '';
    array = array.split('')
    while (passIndex < desiredLength){
       let choice = randomChoice(array)
       let choiceIndex = array.indexOf(choice)
       if (choiceIndex > -1) {
        array.splice(choiceIndex, 1);
      }
       charString =charString + choice
       ++passIndex
    }
    return charString
}

function generatePassword(){
    passNums = '0123456789';
    passSpecial = '!#$%&*+,-.=>?@[]^_`~';
    passCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    passLowerCase = 'abcdefghijklmnopqrstuvwxyz';
    numPass = getChars(numberLength, passNums)
    specialChars = getChars(specialLength, passSpecial) 
    upperPass = getChars(upperLength, passCaps) 
    lowerPass = getChars(lowerLength, passLowerCase)
    finalPass = numPass + specialChars + upperPass + lowerPass 
    console.log(finalPass)
    finalPass = getChars(finalPass.length, finalPass)
    return finalPass
}

function shuffleWord (word){
    var shuffledWord = '';
    word = word.split('');
    while (word.length > 0) {
      shuffledWord +=  word.splice(word.length * Math.random() << 0, 1);
    }
    return shuffledWord;
}

alert("Password: " + finalPassword)