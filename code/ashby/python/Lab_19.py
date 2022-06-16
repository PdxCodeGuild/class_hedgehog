import requests
import html
def main():

    response = requests.get("https://opentdb.com/api.php?amount=10&category=18&type=boolean").json()

#print(response)

    results = response["results"]

    #print(results)
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

main()