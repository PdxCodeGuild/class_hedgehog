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



// let userNumber = document.querySelector("#user-number")
// let userUnit = document.querySelector("#user-unit")
// let outputUnit = document.querySelector("#output-unit")


// function unitConversion(){ 
//     // console.log("test")
//     let inputNumber = Number(userNumber.value);
//     let inputUnit = userUnit.value;
//     let outputUnitvalue = outputUnit.value;

//     let meterUnit = inputNumber * unitConverter[inputUnit];

//     let convertedUnit = meterUnit / unitConverter[outputUnitvalue]
//     console.log(convertedUnit)
// }
