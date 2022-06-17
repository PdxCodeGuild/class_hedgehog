''' Version 1 '''

# def main():        
#     import requests
#     import html

#     trivia = requests.get('https://opentdb.com/api.php?amount=10&category=18&type=boolean')
#     trivia_unwrapped = trivia.json()
#     questions = trivia_unwrapped['results']

#     correct_answers = 0
#     for question in questions:
#         print(html.unescape(question.get('question')))
#         answer = input("True or False?: \t\n-> ").title().replace(' ','')
#         if answer[0] == question.get('correct_answer')[0]:
#             correct_answers += 1
#     print(f'You got {correct_answers} answers correct.')

# main()

#########################################################################################################
''' Version 2 '''

import requests
import html
from random import choice,randint,shuffle

def choose_option(list_of_options):
    for option in list_of_options:
        print(option)
    user_choice = input('\t> ').title().replace(' ','')
    if user_choice not in list_of_options:
        if user_choice.isnumeric():
            if int(user_choice) in range(9,33):
                return user_choice
        return choose_option(list_of_options)
    elif user_choice == 'Any':
        list_of_options.pop(0)
        if list_of_options[0][0] == '9':
            user_choice = str(randint(9,32))
        else:
            user_choice = choice(list_of_options)
    return user_choice.lower().replace(' ','')

def choose_your_questions():
    print("Choose a difficulty: ")
    difficulty = choose_option(["Any", "Easy", "Medium", "Hard"])
    print("Choose a tpye of question: ")
    type = choose_option(["Any", "Multiple", "Boolean"])
    print("Choose a category by number: ")
    category = choose_option(["Any", "9   General Knowledge", "10  Entertainment: Books", "11  Entertainment: Film", "12  Entertainment: Music", "13  Entertainment: Musicals & Theatres", "14  Entertainment: Television", "15  Entertainment: Video Games", "16  Entertainment: Board Games", "17  Science & Nature", "18  Science: Computers", "19  Science: Mathematics", "20  Mythology", "21  Sports", "22  Geography", "23  History", "24  Politics", "25  Art", "26  Celebrities", "27  Animals", "28  Vehicles", "29  Entertainment: Comics", "30  Science: Gadgets", "31  Entertainment: Japanese Anime & Manga", "32  Entertainment: Cartoon and Animation"]) 
    choices = [difficulty, type, category]
    return choices

def main():        

    choices = choose_your_questions()
    trivia = requests.get(f'https://opentdb.com/api.php?amount=10&difficulty={choices[0]}&category={choices[2]}&type={choices[1]}')

    trivia_unwrapped = trivia.json()
    questions = trivia_unwrapped['results']
    
    if questions == []:
        print("Data not retrieved")
        return
    correct_answers = 0
    if choices[1] == 'boolean':
        for question in questions:
            print(html.unescape(question.get('question')))
            answer = input("True or False?: \t\n-> ").title().replace(' ','')
            if answer[0] == question.get('correct_answer')[0]:
                correct_answers += 1
    elif choices[1] == 'multiple':
        for question in questions:
            answers = []
            answers.append(html.unescape(question.get('correct_answer')))
            for incorrect_answer in question.get('incorrect_answers'):
                answers.append(html.unescape(incorrect_answer))
            print(html.unescape(question.get('question')))
            shuffle(answers)
            for index, answer in enumerate(answers):
                print((f'{index}: {answer}'))
            user_answer = int(input("Enter your answer: \n\t> "))
            if answers[user_answer] == html.unescape(question.get('correct_answer')):
                correct_answers += 1        
    elif choices[2] == 'any':
        for question in questions:
            answers = []
            answers.append(html.unescape(question.get('correct_answer')))
            for incorrect_answer in question.get('incorrect_answers'):
                answers.append(html.unescape(incorrect_answer))
            print(html.unescape(question.get('question')))
            shuffle(answers)
            for index, answer in enumerate(answers):
                print((f'{index}: {answer}'))
            user_answer = int(input("Enter your answer: \n\t> "))            
            if answers[user_answer] == html.unescape(question.get('correct_answer')):
                correct_answers += 1     

    print(f'You got {correct_answers} answers correct.')

main()


"""
Trivia API
Let's use the Open Trivia Database API to a write a quiz program.

Part 1
Send a request to the following url: https://opentdb.com/api.php?amount=10&category=18&type=boolean. This will return a list of 10 true/false computer questions. Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

Certain characters in the question text are encoded, to decode them you'll have to use the html module's unescape method.

import html
print(html.unescape('&quot;hello&amp;world&quot;')) # "hello&world"


Part 2 (optional)
The API has many more options for different difficulties, different categories, and both true/false and multiple choice questions. Below are list of dictionaries containing the parameter name (what gets put into the query string) and a friendly name to show the user. Prompt the user for each of these parameters, and include them in the request to get the list of questions. Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

difficulties = [
    { 'parameter': 'any', 'name': 'Any Difficulty'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]

types = [
    { 'parameter': 'any', 'name': 'Any Type'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]

categories = [
    { 'parameter': 'any', 'name': 'Any Category' },
    { 'parameter': '9', 'name': 'General Knowledge' },
    { 'parameter': '10', 'name': 'Entertainment: Books' },
    { 'parameter': '11', 'name': 'Entertainment: Film' },
    { 'parameter': '12', 'name': 'Entertainment: Music' },
    { 'parameter': '13', 'name': 'Entertainment: Musicals &amp; Theatres' },
    { 'parameter': '14', 'name': 'Entertainment: Television' },
    { 'parameter': '15', 'name': 'Entertainment: Video Games' },
    { 'parameter': '16', 'name': 'Entertainment: Board Games' },
    { 'parameter': '17', 'name': 'Science &amp; Nature' },
    { 'parameter': '18', 'name': 'Science: Computers' },
    { 'parameter': '19', 'name': 'Science: Mathematics' },
    { 'parameter': '20', 'name': 'Mythology' },
    { 'parameter': '21', 'name': 'Sports' },
    { 'parameter': '22', 'name': 'Geography' },
    { 'parameter': '23', 'name': 'History' },
    { 'parameter': '24', 'name': 'Politics' },
    { 'parameter': '25', 'name': 'Art' },
    { 'parameter': '26', 'name': 'Celebrities' },
    { 'parameter': '27', 'name': 'Animals' },
    { 'parameter': '28', 'name': 'Vehicles' },
    { 'parameter': '29', 'name': 'Entertainment: Comics' },
    { 'parameter': '30', 'name': 'Science: Gadgets' },
    { 'parameter': '31', 'name': 'Entertainment: Japanese Anime &amp; Manga' },
    { 'parameter': '32', 'name': 'Entertainment: Cartoon &amp; Animations' }
]

"""