// Version 1

function footConvert(num1) {
    console.log(num1 * .3408)

}

// footConvert(12)

// Version 2


const unitConverter = {
    in: "o.0254",
    ft: "0.03048",
    yd: "0.9144",
    mi: "1609.34",
    m: "1",
    km:"1000"

}


let userNumber = prompt("Enter Unit to be converted: ")
let userUnit =  prompt("Enter input unit type: ")
let outputUnit = prompt("Enter desired output unit: ")

let meterUnit = userNumber * unitConverter[userUnit];

let convertedUnit = meterUnit / unitConverter[outputUnit]


console.log(convertedUnit)



let inputEl = document.getElementById("input-el")
let userUnitEl = document.getElementById("user-unit-el")
let outputUnitEl = document.getElementById("output-unit-el")
let outputEl = document.getElementById("output-el")
const convertBtn = document.getElementById("convert-btn")



convertBtn.addEventListener('click', function(){
    inputEl = Number(inputEl.value);
    userUnitEl = userUnitEl.value;
    outputUnitEl = outputUnitEl.value;

    let meterUnit = inputEl * unitConverter[userUnitEl];
    let convertedUnit = meterUnit / unitConverter[outputUnitEl]
    outputEl.innerHTML = convertedUnit
    console.log(inputEl)
    console.log(userUnitEl)
    console.log(outputUnitEl)
    console.log(convertedUnit)
})



// function unitConversion(){ 
//     // console.log("test")
//     let inputNumber = Number(userNumber.value);
//     let inputUnit = userUnit.value;
//     let outputUnitvalue = outputUnit.value;

//     let meterUnit = inputNumber * unitConverter[inputUnit];

//     let convertedUnit = meterUnit / unitConverter[outputUnitvalue]
//     console.log(convertedUnit)
// }
