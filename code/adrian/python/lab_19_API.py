# Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean. 
# This will return a list of 10 true/false computer questions. Ask the user each question, ask them for their answer, and keep track of the score. 
# At the end show them how many they got correct/incorrect.
# Certain characters in the question text are encoded, to decode them you'll have to use the html module's unescape method.

import requests
import html


def trivia():

    response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")

    trivia = response.json()

    correct = 0

    for i, triv in enumerate(trivia["results"]):
        decoded = html.unescape(triv['question'])
        print(f"{i+1}. {decoded}")

        answer = input("Enter True or False: ")
        answer = answer.title()

        if answer[0] == triv.get('correct_answer')[0]:
            correct += 1

    print(f"{correct} correct answers!")

trivia()