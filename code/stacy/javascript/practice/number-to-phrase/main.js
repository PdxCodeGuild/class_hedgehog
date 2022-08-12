$ = (a) => document.querySelector(a);

const number = $("#number");
const runBtnPhrase = $("#run-btn-phrase");
const runBtnRomanNumeral = $("#run-btn-roman-numeral");
const outputDiv = $("#output-div");

const teens = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen"
};

const onesPlace = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eigth",
    "9": "nine"
};

const tensPlace = {
    "0": "",
    "2": "twenty",
    "3": "thirty",
    "4": "fourty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety"
};

const hundredsPlace = {
    "0": "",
    "1": "one-hundred",
    "2": "two-hundred",
    "3": "three-hundred",
    "4": "four-hundred",
    "5": "five-hundred",
    "6": "six-hundred",
    "7": "seven-hundred",
    "8": "eight-hundred",
    "9": "nine-hundred"
}

function convertToPhrase() {
    const numString = number.value;
    const lengthString = numString.length;
    // console.log(lengthString)
    let phrase = '';
    if (lengthString > 3 || (lengthString == 3 && numString[0] == 0)) {
        phrase += "Please enter a number between 0 and 999 without leading 0s";
    };
    if (lengthString == 1) {
        phrase += onesPlace[numString[0]];
    } else if (lengthString == 2 && numString[lengthString - 2] == 1) {
        phrase += teens[numString];
    } else if (lengthString == 2 && numString[lengthString - 1] != 1) {
        phrase += tensPlace[numString[0]] + '-' + onesPlace[numString[1]];
    } else if (lengthString == 3 && numString[1] == 1) {
        phrase += hundredsPlace[numString[0]] + " and " + teens[numString.slice(1)];
    } else if (lengthString == 3 && numString[1] != 1) {
        if (numString[1] == 0 && numString[2] == 0) {
            phrase += hundredsPlace[numString[0]];
        } else if (numString[1] == 0 && numString[2] != 0) {
            phrase += hundredsPlace[numString[0]] + " and " + onesPlace[numString[2]];
        } else if (numString[1] > 1 && numString[2] == 0) {
            phrase += hundredsPlace[numString[0]] + " and " + tensPlace[numString[1]];
        } else if (numString[1] > 1 && numString[2] != 0) {
            phrase += hundredsPlace[numString[0]] + " and " + tensPlace[numString[1]] + "-" + onesPlace[numString[2]];
        };
    };
    
    outputDiv.innerText = phrase;
    return phrase;
}

function convertToRomanNumeral() {
    let numNumber = ParseInt(number.value);
    if (numNumber) { // TODO: this is where I left off

    }

    let romanNumeral = '';

    return romanNumeral;
};

runBtnPhrase.addEventListener("click", convertToPhrase);
runBtnRomanNumeral.addEventListener("click", convertToRomanNumeral);

// Version 3 (optional)
// Convert a number to roman numerals.

// Version 4 (optional)
// Convert a time given in hours and minutes to a phrase.

