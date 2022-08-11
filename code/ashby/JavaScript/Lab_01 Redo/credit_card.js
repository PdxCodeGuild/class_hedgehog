const creditNumber = document.querySelector('#credit-number');
const creditButton = document.querySelector('#credit-button');
const creditResult = document.querySelector('#credit-result');

creditButton.addEventListener('click', function(){
    let creditNum = creditNumber.value;
    let creditList = [];
    let finalCheck = 0;

    
    if(String(creditNum).length != 16){ creditResult.innerText = 'Please enter a valid credit card number.'
    }else{


    for(let x of creditNum){
        creditList.push(x)
    }
    let creditCheck = String(creditList.pop());
    creditList = creditList.reverse()
    for( let x = 0; x < creditList.length; x ++){
        if( x%2 ==0){
            creditList[x] = creditList[x] * 2
        }
        finalCheck += Number(creditList[x])
    }
    finalCheck = String(finalCheck).slice(-1)

    if(finalCheck == creditCheck){
        creditResult.innerText = 'Your credit card number was successfully validated!'
    } else{
        creditResult.innerText = 'Your credit card number is not valid!'
    }
}
})