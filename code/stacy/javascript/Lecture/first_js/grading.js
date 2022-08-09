

const numberGrade = Number(prompt("Enter your grade \n\t> "))

const gradeTable = {
    "10": "A+",
    "9": "A",
    "8": "B",
    "7": "C",
    "6": "D"
}

const key = Math.floor(numberGrade / 10)

let letterGrade = gradeTable[String(key)]

if (letterGrade == undefined){letterGrade = "F"}

console.log(`You got a(n) ${letterGrade}`)