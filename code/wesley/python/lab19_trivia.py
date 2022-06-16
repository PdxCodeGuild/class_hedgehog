import requests
import html


response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')

quests = response.json()

correct = 0 
incorrect = 0

for i, q in enumerate(quests["results"]):
    print(html.unescape(q['question']))
    answer = input("True or False? \n -> ")
    if answer.title() == q['correct_answer']:
        print('Correctomundo')
        correct += 1
    else:
        print("INCORRECT ANSWER")
        incorrect += 1

print(f"You got {correct} right, and {incorrect} wrong!")
