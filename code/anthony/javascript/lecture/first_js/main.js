// declare variables as either let or const
// let can be redeclared later
// const, values cannot change
let className = "Hedgehog"
const classType = "Fullstack" // String

let age = 30      // Number
let amount = 4.20 // Number

let javaScriptIsCool = true // Bool

// Array
const fruits = ['apples', 'bananas', 'coconut']
// Add element to Array
fruits.push('dragon fruit')
// Remove last element from Array
fruits.pop()

// Object
const person = {
  firstName: "James",
  lastName: "Jamison",
  age: 30
}


// null
let luck = null
// undefined
let answer

// Get user input
// const color = prompt("Enter your favorite color:")

// If statements
// if (condition) { logic }
if(person.age > 30){
  // alert("You are over 30")
} else if(person.age < 30) {
  // alert("Still young")
} else {
  // alert("Prime time")
}


// for loops
for(let x = 0; x < 10; x++){
  // console.log(x)
}

// for in will give indexes
for(let index in fruits){
  // console.log(index)
}

// for of will give elements
for(let fruit of fruits){
  // console.log(fruit)
}

// iterate over object
for(let x in person){
  // console.log(x)
  // console.log(person[x])
}
