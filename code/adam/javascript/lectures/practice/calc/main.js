let num1 = 0

let num2 = 2

document.querySelector("#num1-el").innerText = num1
document.querySelector("#num2-el").innerText = num2


let sumEl = document.querySelector("#sum-el")


function add(){
    results = num1 + num2
    sumEl.textContent = "Sum: " + results
}



function subtract(){
    results = num1 - num2
    sumEl.textContent = "Difference: " + results
}



function divide(){
    results = num1 % num2
    
}



function multiply(){
    console.log("multiply clicked")
}   