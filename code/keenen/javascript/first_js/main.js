// alert('Merry Christmas');

// declare viariables as either let or const
// let can be re-declared later
// const, values cannot change 
let className = "Hedgehog"
const classType = "Fullstack"

let age = 30      // Number
let amount = 4.20 // Number

let javaScriptIsCool = true // Bool

// Array
const fruits = ['apples', 'bananas', 'coconut'] 
// Add element to Array
fruits.push('dragon fruit')
// Remove last element from Array
fruits.pop()

console.log(fruits)

// Object
const person = {
    firstName: 'James',
    lastName: 'Jamison',
    age: 30
}

// person.age += 1

// console.log(person['firstName'])
// console.log(person.lastName)
// console.log(person.age)

// null
let luck = null
// undefined
let answer

// Get user input
// const color = prompt('Enter your favorite color: ')

if(person.age > 30){
    // alert('You are over 30')
} 
else if(person.age < 30) {
    // alert('You are still young')
}
else {
    // alert('Prime time')
}


// for loops 
for(let x = 0; x < 10; x++){
    // console.log(fruits[x])
}

// for in will give indexes
for(let fruit in fruits){
    console.log(fruit)
}

// for of will give elements 
for(let fruit of fruits){
    console.log(fruit)
}

// iterate over object
for(let x in person){
    // console.log(x)
    console.log(person[x])
}