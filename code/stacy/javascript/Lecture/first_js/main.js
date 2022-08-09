// alert("Merry Christmas!")
// let and const are variables in javascript, let is changable and const is not
let className = "Hedgehog"
const classType = "Fullstack"


console.log(className) // console.log is the print() statement in python


let age = 30 // number datatype
let amount = 4.20 // number datatype

let javascriptIsCool = true //Boolean (Bool) datatype

const fruits = ['apples', 'bananas', 'coconut'] // array datatype
fruits.push('dragonfruit') // push appends the list
fruits.pop() // pop only removes last item of array, unlike python

const person = { // object datatype
    firstName: "James", //firstName is a string but quotes aren't required, value requires key though
    lastName: "Jamison",
    age: 34
}

person.age += 1

console.log(person['firstName'])
console.log(person.lastName) // can use object.key instead of object['key']

let luck = null // null datatype

let answer // undefined datatype
 

// console.warn()
// console.error()
// console.table()

// const color = prompt("Enter your favorite color: ")
// you have access to all global variables in the console


// arguments go inside parenthesis, code goes in curly brackets
// if (person.age > 30){alert("You are over 30")} 

// else if (person.age < 30) {alert("Still young")} 

// // else doesn't take an argument
// else {alert("Prime time")}



// for loops, essentially just a while loop

// x++ is the same as x+=1
for(let x = 0; x < fruits.length; x++){
    // console.log(x)
}


// fruit in fruits gives indeices, fruit of fruits gives the elements
for (let fruit of fruits) {
    console.log(fruit)
}

// gives the keys
// for (let x in person) {
//     console.log(x)
// }

// gives the values
// for (let x in person) {
//    console.log(person[x])
//}

// of does not work with objects (dictionaries)


