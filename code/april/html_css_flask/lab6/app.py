"""
LAB 6 - Intro to Flask
April 
July 2022

Implement Rot Cipher Python lab into a Flask app:
  - Simple version: the user could just input the word to encode.
  - Complex version: the user could also input the amount to rotate by.

"""

from flask import Flask, request, render_template
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    alphabet = list(string.ascii_lowercase)
    encoded = ""
    user_input = request.form.get("string_input", "")
    rot_choice = request.form.get("rotation", 0)
    message = ""

    try:
        user_input = user_input.lower()
        rot_choice = int(rot_choice)

        for item in user_input:
            if item in alphabet:
                letter = (alphabet.index(item) + rot_choice) % 26
                encoded += alphabet[letter]
            else:
                encoded += item
        

    except (ValueError, TypeError):
        message = "Input Error. Please input a string and a whole number."

    return render_template("index.html", string_input=user_input, encoded=encoded, message=message)


app.run(debug=True)
