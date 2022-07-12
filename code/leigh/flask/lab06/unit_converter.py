from flask import Flask, request, render_template
import string
app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    phrase = request.form.get("phrase", "")
    message = ""
    rot_phrase = ""
    try:
        rot = int(request.form.get("rot", 0))
        char_sets = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation, " "]
        for letter in phrase:
            for char_set in char_sets:
                if letter in char_set:
                    loc = char_set.index(letter)
                    rot_phrase += char_set[(loc + rot) % len(char_set)]
    except (ValueError, TypeError):
        message = "Rot amount must be a whole number"
    return render_template("index.html", phrase=phrase, rot=rot, message=message, rot_phrase=rot_phrase)

app.run()