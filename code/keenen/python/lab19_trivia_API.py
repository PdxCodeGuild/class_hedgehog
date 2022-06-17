
import requests 
import html
from colorama import Fore, Style

def main():


    response = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
    # print(response)

    trivia = response.json()
    # print(trivia['results'])

    questions = trivia['results']
    # print(questions)

    print(Fore.RED + '\n*** The following questions are True/False. Please enter "T" or "F" ***')
    print(Style.RESET_ALL)

    correct = 0
    incorrect = 0

    for i, q in enumerate(trivia['results']):
        print(html.unescape(q['question']))
        answer = input('\nT or F? \n> ').title()
        # print(answer)
       
    for question in questions:
        if answer[0] == question.get('correct_answer')[0]: 
            correct += 1
        else:
            incorrect += 1
    
    print(Fore.GREEN + 'Correct:'+ Style.RESET_ALL,correct)
    print(Fore.RED + 'Incorrect:'+ Style.RESET_ALL,incorrect)

main()