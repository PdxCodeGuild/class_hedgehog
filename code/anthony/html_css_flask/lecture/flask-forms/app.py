from flask import Flask, request, render_template
import string
import random

app = Flask(__name__)  # __main__


@app.route('/', methods=["GET", "POST"])
def index():
    username = request.form.get("name", "")
    pw_length = request.form.get("length", 0)
    message = ""
    password = ""
    try:
        pw_length = int(pw_length)
        password = [random.choice(
            string.ascii_lowercase) for _ in range(pw_length)]
        password = "".join(password)
    except (ValueError, TypeError):
        message = "Password length must be a whole number"

    return render_template("index.html", name=username, password=password, message=message)


@app.route("/logic")
def flask_logic():
    fruits = ["apple", "banana", "kiwi", "watermelon", "strawberry"]

    users = [
        {"name": "bob", "age": 30, "fav_color": "red"},
        {"name": "carl", "age": 25, "fav_color": "blue"},
        {"name": "john", "age": 34, "fav_color": "yellow"},
        {"name": "sarah", "age": 28, "fav_color": "green"},
    ]

    temperature = 70

    return render_template("logic.html", fruits=fruits, users=users, temp=temperature)


app.run(debug=True)
