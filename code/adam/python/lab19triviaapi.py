import requests
import html
# Let's use the [Open Trivia Database API](https://opentdb.com/api_config.php) to a write a quiz program.

# ## Part 1

# Send a request to the following url: `https://opentdb.com/api.php?amount=10&category=18&type=boolean`. This will return a list of 10 true/false computer questions. 
# Ask the user each question, ask them for their answer, and keep track of the score. At the end show them how many they got correct/incorrect.

# Certain characters in the question text are [encoded](https://en.wikipedia.org/wiki/Character_encodings_in_HTML#Character_references), 
# to decode them you'll have to use the `html` module's `unescape` method.

# ```python
# import html
# print(html.unescape('&quot;hello&amp;world&quot;')) # "hello&world"
# ```
response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean")

trivia = response.json()



correct = 0
incorrect = 0  
for i, triv in enumerate(trivia["results"]):
    print("\tAnswer True or False")
    question = input(html.unescape(f"Question {i + 1}: \t {triv['question']}")).title()
    if question == triv["correct_answer"]:
        correct +=1
    else:
        incorrect +=1
    print(f"""Number correct:{correct}
              Number Incorrect: {incorrect}   """)
#print(trivia["results"])

# print(trivia)
