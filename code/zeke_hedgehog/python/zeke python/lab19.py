#Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean. 
#This will return a list of 10 true/false computer questions. Ask the user each question, ask them 
#for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

#Certain characters in the question text are encoded, to decode them you'll have to use the html module's unescape method.

#import html
#print(html.unescape('&quot;hello&amp;world&quot;')) # "hello&world"

import requests
import html

def trivia_api():
    #Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean.
    trivia_requests = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")
    trivia_question = trivia_requests.json()
    trivia_questions = trivia_question["results"]

    #print(trivia_questions)

    #starting point of correct and incorrect 
    correct = 0
    incorrect = 0


    for question in trivia_questions: 
        #print question
        print(html.unescape(question["question"]))
         #ask user a boolean question with .title to return an upper case
        answer = input('Enter "True" or "False": ').title()
        #determine if the answer is correct
        if answer == question["correct_answer"]:
            print("You are correct")
        #track score
            correct +=1
        else:
            print("You are incorrect")
            incorrect +=1
    print(f"total correct {correct} & total incorrect {incorrect} ")

trivia_api()