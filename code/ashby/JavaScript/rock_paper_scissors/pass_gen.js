let pass_length = document.querySelector('#pass_length');

let pw_gen = document.querySelector('#pw_gen');

let password_print = document.querySelector('#password_print');

pw_gen.onclick = function() {
    alert('starting')
   let pwLength = Number(pass_length.value);
   let password = ""
   for(let x = 0 ; x < pwLength ; x++){
    seed = (Math.floor((Math.random() * 94)+32))
    
    password = password + String.fromCharCode(seed)
    

   } 
   password_print.innerText = password
}