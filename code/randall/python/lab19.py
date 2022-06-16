# lab19 Trivia API

import requests
import html

class Trivia:
    def __init__(self):
        self.questions = self.get_questions()
        self.score = 0
        self.current_question = 0

    def get_questions(self, amount=10, category=18, question_type="boolean"):
        #Call the Trivia API and format the response
        url = f"https://opentdb.com/api.php?amount={amount}&category={category}&type={question_type}"
        response = requests.get(url)

        # convert raw response data to Python and pull out the list at the key of 'results'
        results = response.json()["results"]

        questions = []
        for result in results:
            question = {
                "text": html.unescape(result["question"]),  # format the text of the question
                "correct_answer": result["correct_answer"],
                "incorrect_answers": result["incorrect_answers"][0],  # pull the string out of the list
                "category": result["category"],
                "type": result["type"],
                "user_answer": None,  # to track the user's answer to this question
                "was_answered_correctly": False,  # depicts whether the question was answered correctly by the user
            }

            # add the question to the list of questions
            questions.append(question)

        return questions

    def correct_answer(self, question, user_answer):
        """Return a boolean indicating if the user_answer is the correct_answer for the question"""
        return question["correct_answer"] == user_answer

    @property
    def all_questions(self):
        """Return the length of the questions list"""
        return len(self.questions)

    def __str__(self):
        return f"Question {self.current_question + 1} of {self.all_questions}"

if __name__ == "__main__":
    game = Trivia()  # instantiate the Trivia class

    for question in game.questions:
        print(game)
        print(question["text"])
        game.current_question += 1  # increment question count

        # ask the user for their answer
        answer = input("True or False: ").capitalize()  # true -> True, fAlSe -> False

        # ensure the user is entering True or False
        while answer not in ["True", "False"]:
            print("Valid responses: True, False")
            answer = input(
                "True or False: "
            ).capitalize()  # true -> True, fAlSe -> False

        print()

        if game.correct_answer(question, answer):
            game.score += 1
            question["was_answered_correctly"] = True

    # display the outcome of the game to the user
    message = f"You got {game.score} out of {game.all_questions} correct!"
    print(message)

    display_results = input("\nDo you want to see your results? y/n: ").lower()
    if display_results == "y":
        for question in game.questions:
            symbol = (
                "x" if question["was_answered_correctly"] else "+"
            )
            print(f"{symbol} | {question['text']}")