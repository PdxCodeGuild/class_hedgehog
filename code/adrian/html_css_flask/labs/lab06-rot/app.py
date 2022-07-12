from flask import Flask, request, render_template
import string
import random


app = Flask(__name__)





@app.route('/', methods=["GET", "POST"])
def index():
    message = request.form.get("message", "")
    amount = int(request.form.get("amount", 0))
    
    abc = string.ascii_lowercase
    encrypt = ""
    text = ""

    try:
        for ch in message:
            if ch == " ":
                encrypt = encrypt + " "
            else:
                rotate = abc.index(ch) + int(amount)
                if rotate < 26:
                    encrypt = encrypt + abc[rotate]
                else:
                    encrypt = encrypt + abc[rotate % 26]
    
    except (ValueError, TypeError):
        text = "Error: Input a string and a whole number"

    return render_template("index.html", message=message, amount=amount, encrypt=encrypt, text=text)



app.run(debug=True)