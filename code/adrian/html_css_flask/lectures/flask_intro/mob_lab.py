# Adrian, Ezekiel, Stacy, April, Zane
from flask import Flask, request
import string
import random

app = Flask(__name__)


# Let's create a simple password generator using Flask.

# Setup a route for localhost:5000/generate/<int:num_of_characters>
# This route will generate a password of length specified in the route.
# This can just be lowercase letters for now
# Allow for query params to alter the overall password
# uppercase=True should allow for uppercase characters
# digits=True should allow for numbers
# special=True should allow for special characters
# One, all, or none of these query params may be entered so be sure to account for all possibilities

# password len


@app.route("/password/<int:num>")
def password(num):
    print(request.args)
    final_pass = []
    char = string.ascii_lowercase
    if request.args.get("upper") == "True":
        char += string.ascii_uppercase
    if request.args.get("digits") == "True":
        char += string.digits
    if request.args.get("special") == "True":
        char += string.punctuation
    for x in range(num):
        final_pass.append(random.choice(char))
    return "".join(final_pass)






# @app.route("/password/user_input")
# def password():
#     parameters = []

#     password_len = int(input("Enter password length: "))
#     parameters.append(password_len)

#     upper = input("Would you like uppercase letters yes or no: ").lower()
#     if upper[0] == 'y':
#         parameters.append(True)
#     else:
#         parameters.append(False)
#     digits = input("Would you like any digits: ").lower()
#     if digits[0] == 'y':
#         parameters.append(True)
#     else:
#         parameters.append(False)
#     char = input("Would yo like any special characters: ").lower()
#     if char[0] == 'y':
#         parameters.append(True)
#     else:
#         parameters.append(False)
#     return parameters
    


app.run(debug=True)