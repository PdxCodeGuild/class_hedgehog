// name the Vue app to target app level variables and functions instead of "this.""
// const app = Vue.createApp({
//     // data stores application level variabels
//     data() {
//         return {
//             message: "Class Hedgehog"
//         }
//     },
//     // methods stores application functions
//     methods: {
//         surprise: function () {
//             // use "app." to access variables from data
//             alert(app.message)
//         }
//     }
// }).mount("#app")

Vue.createApp({
    // data stores application level variabels
    data() {
        return {
            message: "Class Hedgehog",
            todoText: "",
            todoList: [],
            nextID: 0
        }
    },
    // methods stores application functions
    methods: {
        surprise: function() {
            // use "this." to access variables from data
            alert(this.message)
        },
        addTodo: function() {
            this.todoList.push({
                text: this.todoText, 
                id: this.nextID,
                completed: false
            })
            this.todoText = "",
            this.nextID += 1,
            this.saveToLocalStorage()
        },
        removeTodo: function(id) {
            this.todoList = this.todoList.filter(todo => todo.id !== id)
            this.saveToLocalStorage()
        },
        toggleComplete: function(id) {
            this.todoList.forEach(todo => {
                if(todo.id === id) {
                    todo.completed = !todo.completed
                }
                this.saveToLocalStorage()
            })
        },
        saveToLocalStorage: function() {
            const todoListString = JSON.stringify(this.todoList)
            localStorage.setItem("nextID", this.nextID)
            localStorage.setItem("todoItems", todoListString)
        }
    },
    computed: {
        completedTodos: function() {
            return this.todoList.filter(todo => todo.completed === true)
        },
        uncompletedTodos: function() {
            return this.todoList.filter(todo => todo.completed === false)
        },
        percentComplete: function() {
            return (this.completedTodos.length / this.todoList.length) * 100
        }
    },
    created: function() {
        if(localStorage.getItem("todoItems")) {
            this.todoList = JSON.parse(localStorage.getItem("todoItems"))
        } else {
            this.todoList = []
        }
        if(localStorage.getItem("nextID")) {
            this.nextID = Number(localStorage.getItem("nextID"))
        } else {
            this.nextID = 0
        }
    }
}).mount("#app")

