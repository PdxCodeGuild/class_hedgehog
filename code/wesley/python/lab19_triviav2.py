import requests
import html

difficulties = [
    { 'parameter': 'any', 'name': 'Any Difficulty'},
    { 'parameter': 'easy', 'name': 'Easy' },
    { 'parameter': 'medium', 'name': 'Medium' },
    { 'parameter': 'hard', 'name': 'Hard' }
]

diff = input("Select your difficulty! any/easy/medium/hard \n -> ")

types = [
    { 'parameter': 'any', 'name': 'Any Type'},
    { 'parameter': 'multiple', 'name': 'Multiple Choice' },
    { 'parameter': 'boolean', 'name': 'True / False' }
]

typ = input("Select your type! any/multiple/boolean \n ->")

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

cat = input(f"Select your category! any/9-32 \n-> ")

if cat == "any" and diff == "any" and typ == "any":
    response = requests.get('https://opentdb.com/api.php?amount=10')
elif cat == "any" and typ == "any":
    response = requests.get(f'https://opentdb.com/api.php?amount=10&difficulty={diff}')
elif diff == "any" and typ == "any":
    response = requests.get(f'https://opentdb.com/api.php?amount=10&category={cat}')
elif cat == "any" and diff == "any":
    response = requests.get(f'https://opentdb.com/api.php?amount=10&type={typ}')
elif typ == "any":
    response = requests.get(f'https://opentdb.com/api.php?amount=10&category={cat}&difficulty={diff}')
elif cat == "any":
    response = requests.get(f'https://opentdb.com/api.php?amount=10&difficulty={diff}&type={typ}')
elif diff == "any":
    response = requests.get(f'https://opentdb.com/api.php?amount=10&category={cat}&type={typ}')
else:
    response = requests.get(f'https://opentdb.com/api.php?amount=10&category={cat}&difficulty={diff}&type={typ}')

quests = response.json()
correct = 0 
incorrect = 0

for i, q in enumerate(quests["results"]):
    print(html.unescape(q['question']))
    answer = input("Type your answer \n -> ")
    if answer.title() == q['correct_answer']:
        print('Correctomundo')
        correct += 1
    else:
        print("INCORRECT ANSWER")
        incorrect += 1

print(f"You got {correct} right, and {incorrect} wrong!")
