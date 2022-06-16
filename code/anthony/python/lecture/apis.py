import requests

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")

pokemon = response.json()

for i, mon in enumerate(pokemon["results"]):
    print(f"No. {i+1}\t\t{mon['name']}")

choice = input("Enter pokemon number to get more information: ")

response2 = requests.get(f"https://pokeapi.co/api/v2/pokemon/{choice}/")
print(response2.json())
