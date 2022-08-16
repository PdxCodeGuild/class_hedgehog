const todosContainer = document.querySelector("#todos")


// fetch("https://jsonplaceholder.typicode.com/todos/")
// .then(function(response){
//   return response.json()
// }).then((data) => showTodos(data))
// .catch(err => console.error(err))

async function getData(){
  try {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/")
    const data = await response.json()
  } catch(err) {
    console.error(err)
  }
  showTodos(data)
}

getData()


function showTodos(data) {
  for(let todo of data){
    const p = document.createElement("p")
    p.textContent = todo.title
    todosContainer.appendChild(p)
  }
}

console.log("Hello there")


