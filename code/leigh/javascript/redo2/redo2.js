

let phrase_input = document.querySelector('#phrase');
let rot_input = document.querySelector('#rot');
let run_bt = document.querySelector('#run');
let output = document.querySelector('#output');

run_bt.onclick = function() {
    phrase = phrase_input.value
    rot = Number(rot_input.value)
    console.log(rot + " " + phrase)
    message = ""
    rot_phrase = ""
    char_sets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "/'].;[,=-`?\"}{:><+_)(*&^%$#@!~)}\\|"]
    for (letter of phrase) {
        for (char_set of char_sets) {
            if (char_set.includes(letter)) {
                loc = char_set.indexOf(letter)
                rot_phrase += char_set[(loc + rot) % char_set.length]
            }
        }
    }
    output.innerText = rot_phrase;
}