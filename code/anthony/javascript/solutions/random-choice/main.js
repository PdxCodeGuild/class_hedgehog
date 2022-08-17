function choice(array){
  const index = Math.floor(Math.random() * array.length)
  return array[index]
}

const labs = [
  "Random Password Generator",
  "Rot13"
]

console.log(choice(labs))