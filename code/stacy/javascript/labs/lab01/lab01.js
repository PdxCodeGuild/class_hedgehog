// Lab 1: JavaScript Redo
// Version 1
// Pick a Python lab and re-do it in JavaScript. You should first try to write them using JavaScript's prompt and alert in place of Python's input and print.

// Unit Converter

// Version 2 (optional)
// Once you have that working, use input and button elements, with events. You can read the docs on DOM Manipulation and Events. You can view a demo here.


// measurement_in_meters = measurement * unit_conversions.get(input_unit, 1)
// converted_measurement = measurement_in_meters / unit_conversions.get(output_unit, 1)

const unitConversions = {
    ft: "0.3048",
    mi: "1609.34",
    m: "1",      
    km: "1000",
    yd: "0.9144",
    in: "0.0254"  
}

let inputNumber = Number(prompt("Enter meausurement \n\t> "))
// console.log(inputNumber)
let inputUnit = prompt("Enter input unit \n\t> ")
// console.log(inputUnit)
let outputUnit = prompt("Enter output unit \n\t> ")
// console.log(outputUnit)
let measurementInMeters = inputNumber * unitConversions[inputUnit]
// console.log(measurementInMeters)
let outputNumber = measurementInMeters / unitConversions[outputUnit]
// console.log(outputNumber)
alert(`${inputNumber} ${inputUnit} is ${outputNumber} ${outputUnit}`)
