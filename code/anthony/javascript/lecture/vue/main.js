
Vue.createApp({
  // Data stores application level variables
  data() {
    return {
      message: "Brian that other person",
      todoText: "",
      todoList: [],
      nextId: 0
    }
  },
  // methods stores application functions
  methods: {
    surprise: function() {
      // use 'this.' to access variables from data
      alert(this.message)
    },
    addTodo: function() {
      this.todoList.push({
        text: this.todoText,
        id: this.nextId,
        completed: false
      })
      this.todoText = ""
      this.nextId += 1
      this.saveToLocalStorage()
    },
    removeTodo: function(id) {
      this.todoList = this.todoList.filter(todo => todo.id !== id)
      this.saveToLocalStorage()
    },
    toggleComplete: function(id) {
      this.todoList.forEach(todo => {
        if(todo.id === id){
          todo.completed = !todo.completed
        }
      })
      this.saveToLocalStorage()
    },
    saveToLocalStorage: function () {
      const todoListString = JSON.stringify(this.todoList)
      localStorage.setItem("nextId", this.nextId)
      localStorage.setItem("todoItems", todoListString)
    }
  },
  computed: {
    completedTodos: function () {
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
    if(localStorage.getItem("todoItems")){
      this.todoList = JSON.parse(localStorage.getItem("todoItems"))
    } else {
      this.todoList = []
    }
    console.log(this.todoList)
    if(localStorage.getItem("nextId")){
      this.nextId = Number(localStorage.getItem("nextId"))
    } else {
      this.nextId = 0
    }
  }
}).mount("#app")
















// name the app to get access to app.message
// const app = Vue.createApp({
//   // Data stores application level variables
//   data() {
//     return {
//       message: "Brian that other person"
//     }
//   },
//   // methods stores application functions
//   methods: {
//     surprise: function() {
//       // use 'this.' to access variables from data
//       alert(app.message)
//     }
//   }
// }).mount("#app")