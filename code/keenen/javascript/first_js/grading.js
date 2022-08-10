
//number_grade = int(input("Enter your grade: "))
const numberGrade = Number(prompt("Enter your grade: "))

// grade_table = {
//     "10": "A",
//     '9': 'A',
//     "8": "B",
//     "7": "C",
//     "6": "D"
// }
const gradeTable = {
    "10": "A",
    '9': 'A',
    "8": "B",
    "7": "C",
    "6": "D"
}

// key = number_grade // 10
const key = Math.floor(numberGrade / 10)

// letter_grade = grade_table.get(str(key), "F")
let letterGrade = gradeTable [String(key)]
if(letterGrade == undefined){
    letterGrade = "F"
}

console.log(`You got a(n) ${letterGrade}`)