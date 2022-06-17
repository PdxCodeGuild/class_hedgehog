import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?Limit=151")

pokemon = response.json()


response = requests.get("https://opentdb.com/api.php?amount=1&type=boolean")



print(response.json())






for i, mon in enumerate(pokemon["results"]):
    print(f"N")

posts = response.json()

print(len(posts))



