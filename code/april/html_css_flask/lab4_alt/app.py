"""
LAB 4 - Intro to Flask
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

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    message = ""
    user_input = request.form.get("string_input", "")
    rot_choice = request.form.get("rotation", 0)
    # rot_choice = int(rot_choice)
    encoded = ""

    try:
        
        def rotate(item, some_string=lower, rot_choice=13):
            if item in some_string:
                convert_it = some_string.index(item) + rot_choice
                return some_string[convert_it % len(some_string)]
            else:
                return item

        for item in user_input:
            rot_choice = int(rot_choice)
            if item in lower:
                encoded += rotate(item, rot_choice=rot_choice)
            elif item in upper:
                encoded += rotate(item, upper, rot_choice)
            elif item in digits:
                encoded += rotate(item, digits, rot_choice)
            elif item in special:
                encoded += rotate(item, special, rot_choice)
            else:
                encoded += item  

    except (ValueError, TypeError):
        message = "Input Error. Please input a string and a whole number."

    return render_template("index.html", string_input=user_input, encoded=encoded, message=message)


app.run(debug=True)

