# import requests

# response = requests.get(" ")

# photos = response.json()

# photos = input(" ")

# import requests

# response = requests.get('https://api.ipify.org')
# # print("Bruce is cool",dir(response))

# response = requests.get('https://api.jokes.one', params={'format': 'json'})
# print(response.content.jokes) # https://api.ipify.org/?format=json

# ________________________________________________________________________________________

import requests 
import json


# print(response) 

def jokes():
    url = 'https://icanhazdadjoke.com/search'
    payload = {'term': 'dad'}
    response = requests.get(url, headers={'Accept': 'application/json'}, params=payload)
    # print(response.text)
    data = json.loads(response.text)

    result = data["results"]


    return result

search_results = jokes()

print(search_results[0]['joke'])




#{dic}

#[list]