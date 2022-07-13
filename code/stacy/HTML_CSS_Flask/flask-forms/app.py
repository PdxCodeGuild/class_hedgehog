from flask import Flask, request, render_template
import string
import random

app = Flask(__name__) # __main__

@app.route('/', methods=["GET", "POST"])
def index():
    username = request.form.get("name","") #if there is a name, then return it, else return empty string
    # print(username)
    pw_length = request.form.get("length", 0)
    message = ""
    password = ""
    try:
        pw_length = int(pw_length)
        password = [random.choice(string.ascii_lowercase)for _ in range(pw_length)]
        password = "".join(password)
    except (ValueError, TypeError):
        message = "Password length must be a whole number"

    print(password)
    return render_template("index.html", name=username, password=password, message=message) #passes is name as variable name


@app.route('/logic')
def flask_logic():
    fruits = ["apple","banana","kiwi","watermelon","strawberry"]
    users = [
        {"name": "Bob", "age": 20, "fav_color": "red"},
        {"name": "John", "age": 30, "fav_color": "blue"},
        {"name": "Sarah", "age": 25, "fav_color": "green"},
        {"name": "Yarp", "age": 35, "fav_color": "yellow"}
    ]

    temperature = 71

    return render_template("logic.html", fruits=fruits, users=users, temp=temperature)

app.run(debug=True)

