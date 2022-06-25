#password generator using flask

from flask import Flask, request

app = Flask(__name__) 

@app.route('/generate/<int:num_of_characters>')

def generate_password(num_of_characters):
    import random
    import string
    password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(num_of_characters))
    return password

app.run(debug=True)