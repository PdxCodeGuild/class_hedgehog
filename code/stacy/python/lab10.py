import requests
import time

""" Version 1 """

# def main():
#     packaged_request = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
#     unpacked_request = packaged_request.json()
#     joke = unpacked_request['joke']
#     if '?' in joke:
#         question_and_answer = joke.split('? ')
#         print(question_and_answer[0]+'?')
#         time.sleep(5)
#         print(question_and_answer[1])
#     else:
#         print(joke)
# main()

""" Version 2 """

def main():
    while True:
        search_term = input("Enter a search term or 'done' to quit. \n\t> ").lower()
        if search_term.lower().replace(' ','') == 'done':
            print('Goodbye!')
            break
        else: 
            packaged_request = requests.get(f'https://icanhazdadjoke.com/search?term={search_term}', headers={'Accept': 'application/json'})
            unpacked_request = packaged_request.json()
            # print(unpacked_request)
            jokes = unpacked_request['results']
            while True:
                for joke in jokes:
                    if '?' in joke['joke']:
                        question_and_answer = joke['joke'].split('? ')
                        print(question_and_answer[0]+'?')
                        time.sleep(2)
                        print(question_and_answer[1])
                        keep_playing = input("Would you like to hear another joke? y/n \n\t> ").lower()
                        if keep_playing[0] == 'n':
                            break
                    else:
                        print(joke['joke'])
                        keep_playing = input("Would you like to hear another joke? y/n \n\t> ").lower()
                    if keep_playing[0] == 'n':
                        break
                if keep_playing[0] == 'n':
                    break
        if keep_playing[0] == 'n':
                break
main()

#https://icanhazdadjoke.com/search
'''
Dad Joke API
Use the Dad Joke API to get a dad joke and display it to the user. You may want to also use time.sleep to add suspense.

Part 1
Use the requests library to send an HTTP request to https://icanhazdadjoke.com/ with the accept header as application/json. This will return a dad joke in JSON format. You can then use the .json() method on the response to get a dictionary. Get the joke out of the dictionary and show it to the user.

Part 2 (optional)
Add the ability to "search" for jokes using another endpoint. Create a REPL that allows one to enter a search term and go through jokes one at a time. You can also add support for multiple pages.
'''