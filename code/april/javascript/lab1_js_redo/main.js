

let quantity = Number(prompt("Enter the distance in meters:"))

let unitName = (prompt("Enter the units (feet, miles, meters,kilometers, yards, or inches):"))

let unitConversions = {
    feet: 0.3048,
    miles: 1609.34,
    meters: 1,
    kilometers: 1000,
    yards: 0.9144,
    inches: 0.0254 
}

let unit = unitConversions[unitName]

let total = quantity * unit

let convertedAmt =`${quantity} meter(s) equals ${total} ${unitName}`

console.log(convertedAmt)
alert(convertedAmt)

// console.log (`${quantity} meter(s) equals ${total} ${unitName}`)
