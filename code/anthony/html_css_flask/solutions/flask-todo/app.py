from flask import Flask, request, render_template, redirect

app = Flask(__name__)

todos = [
    {
        "text": "Complete this todo list",
        "priority": "High",
        "completed": False
    },
    {
        "text": "Test completed",
        "priority": "Medium",
        "completed": True
    }
]


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        todo_text = request.form.get("todo_text")
        todo_priority = request.form.get("todo_priority")
        if todo_text:
            todos.append({
                "text": todo_text,
                "priority": todo_priority,
                "completed": False
            })

    return render_template("index.html", todos=todos)


@app.route("/complete/<int:index>")
def completeTodo(index):
    todos[index]["completed"] = not todos[index]["completed"]

    return redirect("/")


@app.route("/delete/<int:index>")
def deleteTodo(index):
    todos.pop(index)

    return redirect("/")


app.run(debug=True)
