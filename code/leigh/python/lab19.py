# Lab 19
# Trivia API
# Leigh Fair-Smiley
# 6/15/2022

import requests
import html

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

print("Difficulties:")
for i, difficulty in enumerate(difficulties):
    print(i, difficulty['name'])
difficulty_choice = int(input("Please enter difficulty: "))
difficulty_choice = difficulties[difficulty_choice]['parameter']
print()
print("types:")
for i, type in enumerate(types):
    print(i, type['name'])
type_choice = int(input("Please enter type: "))
type_choice = types[type_choice]['parameter']
print()
print("categories:")
for i, category in enumerate(categories):
    print(i, category['name'])
category_choice = int(input("Please enter category num: "))
category_choice = categories[category_choice]['parameter']
print()
response = requests.get(f"https://opentdb.com/api.php?amount=10&category={category_choice}&difficulty={difficulty_choice}&type={type_choice}")

score = 0
for quest in response.json()["results"]:
    print(html.unescape(quest['question']))
    answer = input("Answer: ")
    if answer == quest['correct_answer']:
        score += 1

print(f"You got {score} out of 10 Correct")