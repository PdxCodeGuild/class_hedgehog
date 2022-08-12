$ = (a) => document.querySelector(a);

const ccNum = $("#cc-num");
// console.log(ccNum);
const validateBtn = $("#validate-btn");
// console.log(validateBtn);

function validate() {
    const stringNums = ccNum.value;
    // console.log(stringNums);
    // console.log(stringNums.length);
    let listNums = [];
    for (let i=0; i < stringNums.length; i++) {
        listNums[i] = parseInt(stringNums[i]);
    };
    // console.log(listNums);
    // console.log(typeof listNums[0]);
    let checkDigit = listNums.pop();
    checkDigit = checkDigit.toString();
    // console.log(typeof checkDigit);
    // console.log(checkDigit);
    listNums.reverse();
    // console.log(listNums);
    const listLength = listNums.length; // not sure if I'll run into range errors in the following for loop
    for (i=0; i < listLength; i++) {
        if (i % 2 == 0) {
            listNums[i] *= 2;
            // console.log(listNums);
            if (listNums[i] > 9) {
                listNums[i] -= 9;
                // console.log("subtracted");
            };
        };
    };
    let sum = 0;
    for (i=0; i < listLength; i++) {
        sum += listNums[i];
    }
    // console.log(sum);
    // console.log(listNums);
    sum = sum.toString();
    // console.log(sum, typeof sum);
    if (sum[1] == checkDigit) {
        $("#is-valid").innerText = `${stringNums} is a valid credit card number`;
    } else {
        $("#is-valid").innerText = `${stringNums} is not a valid credit card number`;
    };
    return;
};

validateBtn.addEventListener("click", validate);

