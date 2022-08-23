const todosContainer = document.querySelector("#todos");

// fetch('https://jsonplaceholder.typicode.com/todos/').then(function(response) {
//     // console.log(response)
//     return response.json();
// }).then(function(data){
//   showTodos(data);
// }).catch(err => console.error(err));

async function getData() {
    const response = await fetch('https://jsonplaceholder.typicode.com/todos/');
    // console.log(response);
    const data = await response.json();
    // console.log(data);
    showTodos(data);
};

getData();

function showTodos(data) {
    for (let todo of data) {
        const p = document.createElement('p');
        p.textContent = todo.title;
        todosContainer.appendChild(p);
        // console.log(todo);
    };
};

console.log("Hello there");



