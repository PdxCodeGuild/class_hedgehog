import requests
import html
def main_1():

    response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean").json()



    results = response["results"]

    
    player_score = 0
    for result in results:
        print (html.unescape(result["question"]))
        player_input = input("Enter if this is True or False: ").title()
        if player_input == result["correct_answer"]:
            print("Good job, you got it correct!")
            player_score +=1
        else:
            print("Oof, maybe the next one will go better.")

    print(f"You got {player_score} question(s) correct!")

#main_1()


"""Version 2 starts here"""

def generate_trivia_address():
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

    print("Hello! Select a difficulty from below please!")
    for i, x in enumerate(difficulties):
        print(f"{i} {x['name']}")
    user_input =int( input("Enter your number choice here: "))
    difficulty = difficulties[user_input]["parameter"]
    if user_input:
        difficulty = "&difficulty=" + difficulties[user_input]["parameter"]
    else:
        difficulty = ""

    print("please choose a question type: ")
    for i, x in enumerate(types):
        print(f"{i} {x['name']}")
    user_input = int(input("Enter your number choice here: "))
    type = types[user_input]["parameter"]
    if user_input:
        type = "&type=" + types[int(user_input)]["parameter"]
    else:
        type = ""

    print("please choose a question category: ")
    for i, x in enumerate(categories):
        print(f"{i} {x['name']}")
    user_input = int(input("Enter your number choice here: "))
    if user_input:
        category = "&category=" + categories[user_input]["parameter"]
    else:
        category = ""
    address = "https://opentdb.com/api.php?amount=10" + category + difficulty + type 

    return address


def trivia(address = "https://opentdb.com/api.php?amount=10&category=18&type=boolean"):    
    response = requests.get(address).json()


    #Variable management
    results = response["results"]

    #player score counter
    player_score = 0
    #pulls questions, formats, and checks answers against provided answers in API
    for i, result in enumerate(results):
        if result["type"] == "multiple":
            answer_pool = [x for x in result["incorrect_answers","correct_answer"]]
            pass
        else:
            print (f"\n{i+1}. {html.unescape(result['question'])}")
            player_input = input("Enter if this is true or false: ").title()
            if player_input == result["correct_answer"]:
                print("Good job, you got it correct!")
                player_score +=1
            else:
                print("Oof, maybe the next one will go better.")
#final statement / score
    print(f"\nYou got {player_score} question(s) correct!")




def main():
    #pulling data for query
    print(f"""
    Hello, welcome to the fantastic trivia game!
              Here are your options!
              
              1. 10 random questions
              2. Choose your category
                      3. exit
                    """)

    while True:
        try:
            user_choice = int(input("Enter your selection here: "))
        except TypeError:
            print("Please try again.")
            continue
        if user_choice == 1:
            trivia()
        elif user_choice == 2:
            print("Future content")
            trivia(generate_trivia_address())
        elif user_choice ==3:
            print("Goodbye, come again!")
            break
        else:
            print("I am afraid that is not an option, please try again.")


            
    
main()