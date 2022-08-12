// Authors: Leigh, Adrian, Ezekiel, Wesley, Randall

// Let's make a todo-list with the following features:

//     a text input and button to add an item to the list
//     a button on each item to remove the item from the list
//     a button on each item to mark the item as completed

// Removed items should disappear entirely. Completed items 
// should appear at the bottom (or in a separate list) with a 
// line through them.

// Version 2

// Use Bootstrap, Materialize, or custom CSS to make it look beautiful. Try to add as much detail as possible.

// pull input and button from index

let create = document.querySelector('#create');
let createBtn = document.querySelector('#create-btn');

let index = 0

function createTodo() {
    let newElement = document.createElement("p");
    newElement.innerHTML = create.value;
    newElement.id = String(index);
    newElement.classList.add('animate__animated');
    newElement.classList.add('animate__backInLeft');
    document.getElementById("todos").appendChild(newElement); 

    let removeBtn = document.createElement("button");
    removeBtn.innerHTML = "remove";
    removeBtn.id = "remove-" + String(index);
    removeBtn.addEventListener("click", function() {
        document.getElementById(removeBtn.id.slice(7)).remove();
    })
    document.getElementById(String(index)).appendChild(removeBtn);

    let completeBtn = document.createElement("button");
    completeBtn.innerHTML = "complete";
    completeBtn.id = "complete-" + String(index);
    completeBtn.onclick = function() {
        document.getElementById("completed").appendChild(document.getElementById(completeBtn.id.slice(9)));
        document.getElementById(completeBtn.id.slice(9)).style.setProperty("text-decoration", "line-through");
    }
    document.getElementById(String(index)).appendChild(completeBtn);

    index++;
}

createBtn.addEventListener("click", createTodo);