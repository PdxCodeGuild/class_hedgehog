from flask import Flask, request
app = Flask(__name__)


@app.route("/")
def index():
    return "Hello Class Hedgehog!"


@app.route("/signup")
def signup():
    return "You have signed up as a new user!"


@app.route("/hello/<string:name>")
def hello(name):
    return f"Hello {name}"


@app.route("/grade/<int:num>")
def remarks(num):
    if num >= 90:
        return f"You got an A"
    elif num >= 80:
        return f"You got an B"
    elif num >= 70:
        return f"You got an C"
    elif num >= 60:
        return f"You got an D"
    else:
        return f"You got an F"

# localhost:5000/fruit-price?fruit=banana&price=2.4
@app.route("/fruit-price")
def fruit_price():
    fruit = request.args.get("fruit", "")
    price = float(request.args.get("price", 0))

    return f"The price of {fruit} is ${price}"


app.run()
