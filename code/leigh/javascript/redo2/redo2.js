

let phrase_input = document.querySelector('#phrase');
let rot_input = document.querySelector('#rot');
let run_bt = document.querySelector('#run');
let output = document.querySelector('#output');

run_bt.onclick = function() {
    const phrase = phrase_input.value
    const rot = parseInt(rot_input.value)
    let rot_phrase = ""
    const char_sets = ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789", "/'].;[,=-`?\"}{:><+_)(*&^%$#@!~)}\\|", " "]
    for (let letter of phrase) {
        for (let char_set of char_sets) {
            if (char_set.includes(letter)) {
                const loc = char_set.indexOf(letter)
                rot_phrase += char_set[(loc + rot) % char_set.length]
            }
        }
    }
    output.innerText = rot_phrase;
}