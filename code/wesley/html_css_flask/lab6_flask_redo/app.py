from flask import Flask, request, render_template
import string

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    word = request.form.get("word", "")
    rotation = request.form.get("rotation", 0)
    rotation = int(rotation)
    message = ""
    rot = []
    rot1 = ""
    try:
        letters = list(string.printable)
        for i, word in enumerate(word):
            if i + rotation < len(letters):
                rot.append(letters[i + rotation])
            else:
                rot.append(letters[i - rotation])
        rot1 = "".join(rot)
    except (ValueError, TypeError):
        message = "Rotation must be a whole number"

        
    return render_template("index.html", word=word, rotation=rotation, message=message, rot1=rot1)



app.run(debug=True)
