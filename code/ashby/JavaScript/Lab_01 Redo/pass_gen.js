qS = (a) => document.querySelector(a);

let passLength = document.querySelector('#pass_length');

let pwGen = document.querySelector('#pw_gen');

let passwordPrint = document.querySelector('#password_print');

//alternative to .onclick
//pw_gen.addEventListener('click', function(){    })
pwGen.onclick = function() {
   let pwLength = passLength.value;
   let password = ""
   for(let x = 0 ; x < pwLength ; x++){
    seed = (Math.floor((Math.random() * 94)+32))
    
    password = password + String.fromCharCode(seed)
    

   } 
   passwordPrint.innerText = password
}