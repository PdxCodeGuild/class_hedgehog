"""
Password Generator
Keenan, Randall, Adam, Wesley, Leigh
"""

import string
import random
from flask import Flask, request

app = Flask(__name__)


# localhost:5000/generate/12?uppercase=True
@app.route("/generate/<int:num>")
def password_generator(num):

    choices = {
        "uppercase": string.ascii_uppercase,
        "digits": string.digits,
        "special": string.punctuation,
        "spaces": " ",
        "emojis": "🚀💥🗑"
    }

    characters = string.ascii_lowercase

    for arg in request.args:
        if arg in choices:
            characters += choices[arg]

    password = [random.choice(characters) for _ in range(num)]
    return {"password": "".join(password)}


app.run(debug=True)
