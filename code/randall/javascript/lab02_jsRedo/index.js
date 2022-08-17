$(document).ready(function () {
    let todoList = [
    {item : "This is the first item",
    complete : false},
    {item : "This item should be struck through because it is complete",
    complete : true},
    {item : "Go to the store",
    complete : false},
]

let $openList = $("#openList");
let $completeList = $("#completeList");
let $newTask = $("#newTask");

//new todo
$newTask.click(()=>{
    addTodo()
    createTodoList()
  })

//add todo
function addTodo() {
    let newTodo = prompt("Enter your todo item: ") // get new todo
    appendTodo(newTodo)
}

//append todo
function appendTodo(todo) {
    let newItem = {
      item: todo,
      complete: false
    }
    todoList = todoList.concat(newItem)
    createTodoList()
    
  }


//delete
function deleteTodo(todoToDelete){
    for(let i=0; i < todoList.length; i++) {
        if(todoList[i].item === todoToDelete.item){
            todoList.splice(i,1)
            return
        }
    }
}

//change
function changeTodo(targetTodo) {
    for (let i=0; i < todoList.length; i++) {
        if(todoList[i].item === targetTodo.item) {
            todoList[i].complete = !todoList[i].complete
        }
        }
    }



// Create
function makeNewTodoItem(todo) {
   let $newTodoItem, $newButtons

    // new div
    $newTodoItem = $(`<div>${todo.item}</div>`) 
    $newTodoItem.addClass("col-12 col-lg-6 offset-lg-3")

    $newButtons = makeNewButtons(todo) 

    $newTodoItem.append($newButtons)
    console.log($newTodoItem)

    return $newTodoItem
}

function makeNewButtons(todo) {
    let $buttons, $completeButton, $deleteButton

    $buttons = $('<a></a>')
    $buttons.addClass('mx-2')

    $completeButton = $(`<button></button>`)
    $completeButton.addClass('bi bi-check-square')
    $completeButton.click(() => {
        changeTodo(todo)
        createTodoList()
    })


    $deleteButton = $(`<button></button>`)
    $deleteButton.addClass('bi bi-trash mx-1')
    $deleteButton.click(() => {
        deleteTodo(todo)
        createTodoList()
    })
    $buttons.append([$completeButton, $deleteButton])
    return $buttons
}

// Clear
function clearTodoList() {
    $completeList.html('')
    $openList.html('')
}

// Update
function createTodoList () {
    let $todoItem

    clearTodoList()
    todoList.forEach(todo => { 
        $todoItem = makeNewTodoItem(todo)
        if (todo.complete) {
            $completeList.append($todoItem)
            
        } else { 
            $openList.append($todoItem)
    }
 }); 
}
createTodoList()
})
