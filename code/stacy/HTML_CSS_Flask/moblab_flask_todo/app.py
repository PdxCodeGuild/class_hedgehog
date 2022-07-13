"""
Flask Todo List
Let's build a simple todo list with Flask.

Part 1

Using a form, allow the user to save a new todo item to the database. This should include a input for text, a select for the priority, and a button for submitting the form.
Store added todos into a list.
Display those todos in the browser.
<ul>
  <li>walk the dog (high)</li>
  <li>butter the cat (medium)</li>
  <li>wash dishes (low)</li>
</ul>

Part 2

Add styles to each todo to display its priority, e.g. style high priority todos as red.

Part 3

Add the ability to complete a todo
These can be styled with a line through them

Part 4

Add the ability to delete a todo
"""

from flask import Flask, request, render_template, redirect

app = Flask(__name__)

todos = [  
  {
    "text": "Complete this todo list", 
    "priority": "High",
    "completed": False
  },
   {
    "text": "Test", 
    "priority": "Medium",
    "completed": True
  }
]

@app.route("/", methods=["GET","POST"])
def index():
    
    if request.method == "POST":
      todo_text = request.form.get("todo_text")
      todo_priority = request.form.get("todo_priority")
      if todo_text:
        todos.append({"text": todo_text, "priority": todo_priority, "completed": False})
    return render_template("index.html", todos=todos)

@app.route("/complete/<int:index>", methods=["GET","POST"])
def complete_todo(index):
    todos[index]["completed"] = not todos[index]["completed"]
    return redirect("/")

@app.route("/delete/<int:index>", methods=["GET","POST"])
def delete(index):
    todos.pop(index)
    return redirect("/")

app.run(debug=True)